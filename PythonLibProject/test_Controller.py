from Controller import Controller
import re

def test_search_by_author() :
    controller = Controller()
    # full name
    sk = controller.searchByAuthor("Stephen King")
    assert len(sk) == 4
    # verify 8 columns are returned
    assert len(sk[0]) == 8
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
    booktitles = [x[3] for x in books]
    expected = ['IT', 'The Shining', 'The Green Mile', 'Pet Sematary']
    if not assertFalse :
        for x in expected :
            assert x in booktitles
    else :
        for x in expected :
            assert x not in booktitles


def test_search_by_title() :
    controller = Controller()
    booktitle = controller.searchByTitle("IT")  # single word title
    assert len(booktitle) == 1
    assert len(booktitle[0]) == 8
    assert booktitle[0][3] == "IT"

    booktitle = controller.searchByTitle("")  # empty
    assert len(booktitle) == 0

    booktitle = controller.searchByTitle("The Lord of the Rings")  # multiword title
    assert len(booktitle) == 1
    assert len(booktitle[0]) == 8
    assert booktitle[0][3] == "The Lord of the Rings"


def test_search_by_genre() :
    controller = Controller()
    bookgenre = controller.searchByGenre("Horror")
    assert len(bookgenre) == 5
    bookgenre = controller.searchByGenre("Romance")
    assert len(bookgenre) == 3
    booktitles = [x[3] for x in bookgenre]
    expected = ["Pride and Prejudice", "Sense and Sensibility", "The Edible Woman"]
    for x in expected:
        assert x in booktitles
    bookgenre = controller.searchByGenre("")
    assert len(bookgenre) == 0
    bookgenre = controller.searchByGenre("fefwfew")
    assert len(bookgenre) == 0


def test_get_synopsis() :
    controller = Controller()
    synopsis = controller.getSynopsis(1)
    synopsis =  re.sub('\W+',' ', synopsis[0][3])
    expected = "Follows the turbulent relationship between Elizabeth Bennet,\
    the daughter of a country gentleman, and Fitzwilliam Darcy, a rich aristocratic landowner. \
    They must overcome the titular sins of pride and prejudice in order to fall in love and marry."
    expected = re.sub('\W+',' ', expected)
    assert synopsis == expected