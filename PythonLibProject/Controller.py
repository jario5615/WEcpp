import mysql.connector

class Controller:
    import mysql

    def __init__(self, filename):
        self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          #database="librarydatabase"
        )
        self.mycursor = self.mydb.cursor()
        with open(filename, "r") as f:
            for query in f.read().split(";")[:-1]:
                self.mycursor.execute(query+";", multi=True)
                self.mydb.commit()
    def searchByAuthor(self, name: str):
        '''
        firstname = name.split(" ")[0]
        lastname = name.split(" ")[1]
        '''
        query = f"""
        SELECT book.bookid, book.title, CONCAT (author.firstname, " ", author.lastname) as name, genre.genrename
        FROM book
        JOIN author on author.authorid = book.authorid
        JOIN genre ON book.genreid = genre.genreid
        WHERE CONCAT (author.firstname, " ", author.lastname) LIKE '%{name}%';
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def searchByTitle(self, title: str):
        query = f"""
        SELECT book.bookid, book.title, CONCAT (author.firstname, " ", author.lastname) as name, genre.genrename
        FROM book
        JOIN author ON book.authorid = author.authorid
        JOIN genre ON book.genreid = genre.genreid
        WHERE book.title LIKE '%{title}%';
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def searchByGenre(self, genre: str):
        query = f"""
        SELECT book.bookid, book.title, CONCAT (author.firstname, " ", author.lastname) as name, genre.genrename
        FROM book
        JOIN author ON book.authorid = author.authorid
        JOIN genre ON book.genreid = genre.genreid
        WHERE genre.genrename = '{genre}';
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def getSynopsis(self, bookId):
        query = f"""
        SELECT book.title, CONCAT (author.firstname, " ", author.lastname) as name, book.synopsis
        FROM book
        JOIN author ON book.authorid = author.authorid
        WHERE book.bookid = '{bookId}'
        """
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def addThing(self, theThing, kwargs):
        keys = []
        values = []
        for k, v in kwargs.items():
            if v is not None and v != "":
                keys.append(k)
                values.append(f"'{v}'")
        query = f"""
                INSERT INTO {theThing}({", ".join(keys)})
                VALUES ({", ".join(values)});
                """
        try:
            self.mycursor.execute(query)
            self.mydb.commit()
        except Exception as e:
            return e

    def deleteThing(self, thing, thingId):
        query = f"""
        DELETE FROM {thing}
        WHERE {thing}id = {thingId};"""
        self.mycursor.execute(query)

if __name__ == "__main__":

    c = Controller("LibraryDatabaseTest.sql")
    a = c.searchByAuthor("king")
    print(a)