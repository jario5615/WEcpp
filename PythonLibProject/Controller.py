import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="librarydatabase"
)
mycursor = mydb.cursor()
def searchByAuthor(name):
    firstname = name.split(" ")[0]
    lastname = name.split(" ")[1]
    query = f"""
    SELECT book.*, author.firstname, author.lastname
    FROM book
    JOIN author on author.authorid = book.authorid
    WHERE author.firstname = '{firstname}' AND author.lastname = '{lastname}';
    """
    mycursor.execute(query)
    return mycursor.fetchall()
def searchByTitle(title: str):
    query = f"""
    SELECT book.*, author.firstname, author.lastname
    FROM book
    JOIN author ON book.authorid = author.authorid
    WHERE book.title = '{title}';
    """
    mycursor.execute(query)
    return mycursor.fetchall()
def searchByGenre(genre: str):
    query = f"""
    SELECT book.*, author.firstname, author.lastname
    FROM book
    JOIN author ON book.authorid = author.authorid
    JOIN genre ON book.genreid = genre.genreid
    WHERE genre.genrename = '{genre}';
    """
    mycursor.execute(query)
    return mycursor.fetchall()
    print(genre)
def getSynopsis(bookId):
    query = f"""
    SELECT book.title, author.firstname, author.lastname, book.synopsis
    FROM book
    JOIN author ON book.authorid = author.authorid
    WHERE book.bookid = '{bookId}'
    """
    mycursor.execute(query)
    return mycursor.fetchall()
    print(genre)
def addAuthor(name):
    print(name)
def deleteAuthor(authorId):
    print(authorId)
def addBook(name):
    print(name)
def deleteBook(bookId):
    print(bookId)

if __name__ == "__main__":
    a = getSynopsis("1")
    for x in a:
        print(x)