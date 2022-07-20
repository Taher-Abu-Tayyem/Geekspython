class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    def remove_book(self, bookName):
        self.centraLibrary.remove(bookName)
        if bookName in self.books:
            print("You have borrow a {bookName} book. Return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been borrow by someone else. Please borrow another book available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")


class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = ["English", "arabic", "design", "programing"]
    student = Student()
    Clients = ["taher", "tareq", "ahmed", "mohaund"]
    librarian = ["tareq", "ahmed"]
    while True:
        welcomeMsg = '''\n ====== Book Library System+ ======
        Please choose an option:
        1. Display all the books
        2. Borrow book
        3. Return book
        4. Exit 
        5. Add book
        6. Add Client
        7. Display all the Clients
        8. Add librarian
        9. Display all the librarian
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            print(centraLibrary)

        elif a == 2:
            centraLibrary.remove(student.requestBook())
        elif a == 3:
            centraLibrary.append(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        elif a == 5:
            Book_name = input("enter the book name")
            centraLibrary.append(Book_name)
        elif a == 6:
            Client_name = input("enter the Client name")
            Clients.append(Client_name)
        elif a == 7:
            print(Clients)
        elif a == 8:
            librarian_name = input("enter the librarian name")
            librarian.append(librarian_name)
        elif a == 9:
            print(librarian)

        else:
            print("Invalid Choice!")
