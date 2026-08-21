# Library Management System using Object-Oriented Programming

# ---------------- Book Class ---------------- #

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None

    def display_book(self):
        status = "Issued" if self.is_issued else "Available"

        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")

        if self.is_issued:
            print(f"Issued To : {self.issued_to.name}")

        print("-" * 30)


# ---------------- Patron Class ---------------- #

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name

    def display_patron(self):
        print(f"Patron ID : {self.patron_id}")
        print(f"Name      : {self.name}")
        print("-" * 30)


# ---------------- Library Class ---------------- #

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add Book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    # Add Patron
    def add_patron(self, patron):
        self.patrons.append(patron)
        print("Patron added successfully!")

    # Display Books
    def display_books(self):
        if len(self.books) == 0:
            print("No books in library.")
        else:
            print("\n------ Library Books ------")
            for book in self.books:
                book.display_book()

    # Display Patrons
    def display_patrons(self):
        if len(self.patrons) == 0:
            print("No patrons registered.")
        else:
            print("\n------ Library Patrons ------")
            for patron in self.patrons:
                patron.display_patron()

    # Search Book
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # Search Patron
    def search_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    # Issue Book
    def issue_book(self, book_id, patron_id):
        book = self.search_book(book_id)
        patron = self.search_patron(patron_id)

        if book is None:
            print("Book not found.")
            return

        if patron is None:
            print("Patron not found.")
            return

        if book.is_issued:
            print("Book is already issued.")
        else:
            book.is_issued = True
            book.issued_to = patron
            print(f"Book issued successfully to {patron.name}.")

    # Return Book
    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            print("Book not found.")
            return

        if not book.is_issued:
            print("Book was not issued.")
        else:
            print(f"Book returned by {book.issued_to.name}.")
            book.is_issued = False
            book.issued_to = None


# ---------------- Main Program ---------------- #

library = Library()

while True:

    print("\n====== Library Management System ======")
    print("1. Add Book(s)")
    print("2. Add Patron(s)")
    print("3. Display Books")
    print("4. Display Patrons")
    print("5. Search Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Add Books
    if choice == "1":

        n = int(input("How many books do you want to add? "))

        for i in range(n):
            print(f"\nEnter details of Book {i+1}")

            book_id = int(input("Book ID : "))
            title = input("Title : ")
            author = input("Author : ")

            library.add_book(Book(book_id, title, author))

    # Add Patrons
    elif choice == "2":

        n = int(input("How many patrons do you want to add? "))

        for i in range(n):
            print(f"\nEnter details of Patron {i+1}")

            patron_id = int(input("Patron ID : "))
            name = input("Name : ")

            library.add_patron(Patron(patron_id, name))

    # Display Books
    elif choice == "3":
        library.display_books()

    # Display Patrons
    elif choice == "4":
        library.display_patrons()

    # Search Book
    elif choice == "5":

        book_id = int(input("Enter Book ID : "))

        book = library.search_book(book_id)

        if book:
            print("\nBook Found")
            book.display_book()
        else:
            print("Book not found.")

    # Issue Book
    elif choice == "6":

        book_id = int(input("Enter Book ID : "))
        patron_id = int(input("Enter Patron ID : "))

        library.issue_book(book_id, patron_id)

    # Return Book
    elif choice == "7":

        book_id = int(input("Enter Book ID : "))
        library.return_book(book_id)

    # Exit
    elif choice == "8":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")