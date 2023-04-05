
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
                    # TODO - send search term to core and return it to UI
                case "2":
                    search = input("Enter the search term for Title of Book: ")
                    # TODO - send search term to core and return it to UI
                case "3":
                    search = input("Enter the search term for Genre of Book: ")
                    # TODO - send search term to core and return it to UI
        case "2":
            subchoice = input("Enter the ID of book you wish to get a synopsis of: ")
            # TODO - return synopsis of book based on ID
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
                subchoice = input("Enter Enter number of relevant operation: ")
                match subchoice:
                    case "1":
                        name = input("Enter name of author to add")
                        # TODO - Take info for new author from user and send to core to add
                    case "2":
                        id = input("Enter ID of author to delete")
                        # TODO - Take ID of authour and send to core for deletion
                    case "3":
                        name = input("Enter name of book to add")
                        # TODO - Take info for new book from user and send to core to add
                    case "4":
                        id = input("Enter ID of author to delete")
                        # TODO - Take ID of book and send to core for deletion
