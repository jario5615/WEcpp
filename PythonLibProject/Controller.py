import mysql.connector

class Controller:
    import mysql

    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="librarydatabase"
        )
        self.mycursor = self.mydb.cursor()

    def searchByAuthor(self, name: str):
        '''
        firstname = name.split(" ")[0]
        lastname = name.split(" ")[1]
        '''
        query = f"""
        SELECT book.*, author.firstname, author.lastname
        FROM book
        JOIN author on author.authorid = book.authorid
        WHERE author.firstname LIKE  '%{name}%' OR author.lastname LIKE '%{name}%';
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def searchByTitle(self, title: str):
        query = f"""
        SELECT book.*, author.firstname, author.lastname
        FROM book
        JOIN author ON book.authorid = author.authorid
        WHERE book.title = '{title}';
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def searchByGenre(self, genre: str):
        query = f"""
        SELECT book.*, author.firstname, author.lastname
        FROM book
        JOIN author ON book.authorid = author.authorid
        JOIN genre ON book.genreid = genre.genreid
        WHERE genre.genrename = '{genre}';
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()
        print(genre)

    def getSynopsis(self, bookId):
        query = f"""
        SELECT book.title, author.firstname, author.lastname, book.synopsis
        FROM book
        JOIN author ON book.authorid = author.authorid
        WHERE book.bookid = '{bookId}'
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()
        print(genre)

    def addAuthor(self, name):
        print(name)

    def deleteAuthor(self, authorId):
        print(self, authorId)

    def addBook(self, name):
        print(self, name)

    def deleteBook(self, bookId):
        print(bookId)

'''
if __name__ == "__main__":
    a = getSynopsis("1")
    for x in a:
        print(x)
'''