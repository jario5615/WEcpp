from Controller import *
from prettytable import PrettyTable
from datetime import date

def printSearch(search):
    t = PrettyTable(["D", "Title", "Author ", " Genre"])
    for a in search:
        t.add_row(a)
    print(t)

def printSynop(search):
    t = PrettyTable(["Book Name", "Author ", "Synopsis"])
    for a in search:
        t.add_row(a)
    print(t)
control = Controller("LibraryDatabaseProd.sql")

choice = ""

while choice != "0":
    print("Library Program: ")
    print("1 - Search for book: ")
    print("2 - Get book synopsis by id")
    print("3 - Admin tasks ")
    print("0 - Quit")
    choice = input("Enter number of relevant operation: ")
    match choice:
        case "0":
            break
        case "1":
            print("Search:")
            print("1 - Search by Author")
            print("2 - Search by Title")
            print("3 - Search by Genre")
            subchoice = input("Enter Enter number of relevant operation: ")
            match subchoice:
                case "1":
                    search = input("Enter the search term for Author of Book: ")
                    printSearch(control.searchByAuthor(search))
                case "2":
                    search = input("Enter the search term for Title of Book: ")
                    printSearch(control.searchByTitle(search))
                case "3":
                    search = input("Enter the search term for Genre of Book: ")
                    printSearch(control.searchByGenre(search))
        case "2":
            search = input("Enter the ID of book you wish to get a synopsis of: ")
            printSynop(control.getSynopsis(search))
        case "3":
            password = input("Enter the admin password to continue: ")
            if password != "password": # TEMP ADMIN PASSWORD
                print("Incorrect password")
            else:
                #Admin stuff
                print("Admin Tasks:")
                print("1 - Add Author")
                print("2 - Delete Author")
                print("3 - Add Book")
                print("4 - Delete Book")
                print("5 - Add Genre")
                print("6 - Delete Genre")
                subchoice = input("Enter Enter number of relevant operation: ")
                match subchoice:
                    case "1":
                        id = int(input("Enter author id: "))
                        while id == "":
                            id = int(input("Enter author id: "))
                        firstname = input("Enter first name:")
                        while firstname == "":
                            firstname = input("Enter first name:")
                        middlename = input("Enter middle name (leave blank for null): ")
                        if middlename == "": middlename = None
                        lastname = input("Enter last name:")
                        while lastname == "":
                            lastname = input("Enter last name:")
                        gender = input("Enter Gender M/F: ")
                        if gender == "": gender = None
                        dob = input("Enter date of birth in format YYYY-MM-DD: ")
                        while True:
                            try:
                                date.fromisoformat(dob)
                                break
                            except Exception:
                                dob = input("Enter date of birth in format YYYY-MM-DD: ")
                        dod = input("Enter date of death in format YYYY-MM-DD: ")
                        while dod != "":
                            try:
                                date.fromisoformat(dod)
                                break
                            except Exception:
                                dod = input("Enter date of birth in format YYYY-MM-DD: ")
                        if dob == "": dob = None
                        insert = {"authorid": id, "firstname": firstname, "middlename": middlename, "lastname": lastname, "gender": gender, "dateofbirth": dob, "dateofdeath": dod}
                        print(control.addThing("author", insert))

                    case "2":
                        id = input("Enter ID of author to delete")
                        control.deleteThing("author", id)
                    case "3":
                        name = input("Enter name of book to add")
                        while name == "":
                            name = input("Enter name of book to add")
                        bookid = input("Enter the book ID")
                        while bookid == "":
                            bookid = input("Enter the book ID")
                        authorid = input("Enter the author ID")
                        while authorid == "":
                            authorid = input("Enter the author ID")
                        genreid = input("Enter the genre ID")
                        while genreid == "":
                            genreid = input("Enter the genre ID")
                        synop = input("Enter book synopsis")
                        pubdate = input("Enter publication date in format YYYY-MM-DD")
                        while pubdate != "":
                            try:
                                date.fromisoformat(pubdate)
                                break
                            except Exception:
                                pubdate = input("Enter publication date in format YYYY-MM-DD: ")
                        insert = {"bookid" : bookid, "authorid": authorid, "genreid": genreid, "title": name, "synopsis": synop, "publicationdate": pubdate}
                        message = str(control.addThing("book", insert))
                        if message.find("genre") != -1:
                            print("Book must have a valid genre id")
                        if message.find("author") != -1:
                            print("Book must have a valid author id")


                    case "4":
                        authorid = input("Enter ID of author to delete")
                        control.deleteThing("book", authorid)

                    case "5":
                        genreid = input("Enter genreid")
                        while genreid == "":
                            genreid = input("Enter genreid:")
                        genrename = input("Enter genre name")
                        while genreid == "":
                            genrename = input("Enter genre name:")
                        control.addThing("genre", {"genreid": genreid, "genrename": genrename})

                    case "6":
                        genreid = input("Enter ID of genre to delete")
                        control.deleteThing("genre", genreid)
