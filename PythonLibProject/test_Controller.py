from Controller import Controller
import re


def test_search_by_author() :
    controller = Controller("LibraryDatabaseTest.sql")
    # full name
    sk = controller.searchByAuthor("Stephen King")
    assert len(sk) == 4
    # verify 4 columns are returned
    assert len(sk[0]) == 4
    checkTitles(sk, False)
    # first name only
    sk = controller.searchByAuthor("Stephen")
    assert len(sk) == 4
    checkTitles(sk, False)
    # lastname
    sk = controller.searchByAuthor("King")
    assert len(sk) == 4
    checkTitles(sk, False)
    # other name
    other = controller.searchByAuthor("J")
    # verify all names containing j are returned (11 rows)
    assert len(other) == 11
    # verify stephen kings novels are not in this set
    checkTitles(other, True)
    # author not in database returns nothing
    notInDb = controller.searchByAuthor("grgergre")
    assert len(notInDb) == 0
    # empty string returns everything
    everything = controller.searchByAuthor("")
    assert len(everything) == 31


def checkTitles(books, assertFalse) :
    booktitles = [x[1] for x in books]
    expected = ['IT', 'The Shining', 'The Green Mile', 'Pet Sematary']
    if not assertFalse :
        for x in expected :
            assert x in booktitles
    else :
        for x in expected :
            assert x not in booktitles


def test_search_by_title() :
    controller = Controller("LibraryDatabaseTest.sql")
    booktitles = controller.searchByTitle("IT")  # all titles containing "it"
    assert len(booktitles) == 3
    assert len(booktitles[0]) == 4
    expected = ["Sense and Sensibility", "IT", "The Hobbit"]
    titles = [x[1] for x in booktitles]
    for x in expected:
        assert x in titles

    booktitle = controller.searchByTitle("")  # all books in the database
    assert len(booktitle) == 31

    booktitle = controller.searchByTitle("The Lord of the Rings")  # multiword title, should be only one
    assert len(booktitle) == 1
    assert len(booktitle[0]) == 4
    assert booktitle[0][1] == "The Lord of the Rings"


def test_search_by_genre() :
    controller = Controller("LibraryDatabaseTest.sql")
    bookgenre = controller.searchByGenre("Horror")
    assert len(bookgenre) == 5
    bookgenre = controller.searchByGenre("Romance")
    assert len(bookgenre) == 3
    booktitles = [x[1] for x in bookgenre]
    expected = ["Pride and Prejudice", "Sense and Sensibility", "The Edible Woman"]
    for x in expected :
        assert x in booktitles
    bookgenre = controller.searchByGenre("")
    assert len(bookgenre) == 0
    bookgenre = controller.searchByGenre("fefwfew")
    assert len(bookgenre) == 0


def test_get_synopsis() :
    controller = Controller("LibraryDatabaseTest.sql")
    synopsis = controller.getSynopsis(1)
    synopsis = re.sub('\W+', ' ', synopsis[0][2])
    expected = "Follows the turbulent relationship between Elizabeth Bennet,\
    the daughter of a country gentleman, and Fitzwilliam Darcy, a rich aristocratic landowner. \
    They must overcome the titular sins of pride and prejudice in order to fall in love and marry."
    expected = re.sub('\W+', ' ', expected)
    assert synopsis == expected
    # verify books with no synopsis return none
    synopsis = controller.getSynopsis(2)
    assert synopsis[0][2] is None
    # verify invalid book ids return an empty set
    synopsis = controller.getSynopsis(54)
    assert synopsis == []


def test_add_thing() :
    controller = Controller("LibraryDatabaseTest.sql")
    thing = "Book"
    d = {"bookid": 35, "authorid": 1, "genreid":2, "title": "TEST BOOK"}
    controller.addThing(thing, d)
    #verify the book was added
    book = controller.searchByTitle("TEST BOOK")
    assert len(book) == 1
    assert len(book[0]) == 4
    assert book[0][0] == 35
    assert book[0][1] == "TEST BOOK"
    assert book[0][2] == "Stephen King"
    assert book[0][3] == "Fantasy"

    #adding an invalid book (invalid query for table)
    thing = "Book"
    d = {"bookid" : 2, "authorid" : 66, "genreid" : 33, "title" : "FAIL BOOK", "FakeColumn": "should fail"}
    controller.addThing(thing, d)
    book = controller.searchByTitle("FAIL BOOK")
    assert len(book) == 0

    thing = "Author"
    d = {"authorid": 22, "firstname": "FIRST", "lastname": "LAST", "dateofbirth": "2020-1-1"}
    controller.addThing(thing, d)
    #to verify, testing if a book added to the author works
    thing = "Book"
    d = {"bookid" : 40, "authorid" : 22, "genreid" : 2, "title" : "TESTING AUTHOR"}
    controller.addThing(thing, d)
    book = controller.searchByTitle("TESTING AUTHOR")
    assert len(book) == 1
    assert len(book[0]) == 4
    assert book[0][0] == 40
    assert book[0][1] == "TESTING AUTHOR"
    assert book[0][2] == "FIRST LAST"
    assert book[0][3] == "Fantasy"

    thing = "Author"
    d = {"authorid" : 23, "lastname" : "SHOULD FAIL", "dateofbirth" : "2020", "fakecolumn": "INVALID DATA"}
    controller.addThing(thing, d)
    # to verify, testing if a book added to the author works
    thing = "Book"
    d = {"bookid" : 40, "authorid" : 23, "genreid" : 2, "title" : "TESTING AUTHOR FAIL"}
    controller.addThing(thing, d)
    book = controller.searchByTitle("TESTING AUTHOR FAIL")
    assert len(book) == 0

    thing = "Genre"
    d = {"genreid": 20, "genrename": "TEST GENRE"}
    controller.addThing(thing, d)
    # to verify, testing if a book added to the author works
    thing = "Book"
    d = {"bookid" : 41, "authorid" : 1, "genreid" : 20, "title" : "TESTING GENRE"}
    controller.addThing(thing, d)
    book = controller.searchByTitle("TESTING GENRE")
    assert len(book) == 1
    assert len(book[0]) == 4
    assert book[0][0] == 41
    assert book[0][1] == "TESTING GENRE"
    assert book[0][2] == "Stephen King"
    assert book[0][3] == "TEST GENRE"

    thing = "Genre"
    d = {"genreid" : 55, "genrename" : "TEST GENRE", "fakeColumn" : "INVALID DATA"}
    controller.addThing(thing, d)
    # to verify, testing if a book added to the author works
    thing = "Book"
    d = {"bookid" : 42, "authorid" : 1, "genreid" : 55, "title" : "TESTING GENRE FAIL"}
    controller.addThing(thing, d)
    book = controller.searchByTitle("TESTING GENRE FAIL")
    assert len(book) == 0

def test_delete_thing() :
    controller = Controller("LibraryDatabaseTest.sql")
    booktitle = controller.searchByTitle("The Lord of the Rings")  # get existing book
    assert len(booktitle) == 1  # verify it is there
    allbooks = controller.searchByTitle("")  # all books in the database
    assert len(allbooks) == 31

    controller.deleteThing("book", 6) #  delete using its id
    booktitle = controller.searchByTitle("The Lord of the Rings")
    assert len(booktitle) == 0  # verify it has been deleted
    allbooks = controller.searchByTitle("")  # all books in the database
    assert len(allbooks) == 30

    controller = Controller("LibraryDatabaseTest.sql") #  fresh database
    books = controller.searchByAuthor("Stephen King")
    assert len(books) == 4
    allbooks = controller.searchByTitle("")  # all books in the database
    assert len(allbooks) == 31

    controller.deleteThing("author", 1) # delete the author
    books = controller.searchByAuthor("Stephen King")
    assert len(books) == 0
    allbooks = controller.searchByTitle("")  # all books in the database
    assert len(allbooks) == 27

    controller = Controller("LibraryDatabaseTest.sql")  # fresh database
    books = controller.searchByGenre("Romance")
    assert len(books) == 3
    allbooks = controller.searchByTitle("")  # all books in the database
    assert len(allbooks) == 31

    controller.deleteThing("genre", 5)  # delete the genre
    books = controller.searchByGenre("Romance")
    assert len(books) == 0
    allbooks = controller.searchByTitle("")  # all books in the database
    assert len(allbooks) == 28



