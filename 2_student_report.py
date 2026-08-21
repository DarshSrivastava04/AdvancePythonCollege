# Decorator
def format_report(func):
    def wrapper(self):
        print("\n" + "=" * 40)
        print("     LIBRARY MANAGEMENT REPORT")
        print("=" * 40)

        func(self)

        print("=" * 40)
        print("         END OF REPORT")
        print("=" * 40)

    return wrapper


class LibraryReport:

    def __init__(self, library_name):
        self.library_name = library_name
        self.report = []

    def add_data(self, detail):
        self.report.append(detail)

    @format_report
    def generate_report(self):
        print("Library Name :", self.library_name)
        print()

        for item in self.report:
            print(item)


# Main Program
library = input("Enter Library Name: ")

report = LibraryReport(library)

date = input("Enter Report Date: ")
librarian = input("Enter Librarian Name: ")
books = input("Enter Total Books: ")
issued = input("Enter Books Issued: ")
returned = input("Enter Books Returned: ")
available = input("Enter Books Available: ")
members = input("Enter Total Members: ")
new_books = input("Enter New Books Added: ")
fine = input("Enter Fine Collected: ")
popular = input("Enter Most Borrowed Book: ")

report.add_data("Report Date : " + date)
report.add_data("Librarian : " + librarian)
report.add_data("Total Books : " + books)
report.add_data("Books Issued : " + issued)
report.add_data("Books Returned : " + returned)
report.add_data("Books Available : " + available)
report.add_data("Total Members : " + members)
report.add_data("New Books Added : " + new_books)
report.add_data("Fine Collected : ₹" + fine)
report.add_data("Most Borrowed Book : " + popular)

report.generate_report()