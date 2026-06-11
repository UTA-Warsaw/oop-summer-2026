from book import Book
from author import Author
from employee import Employee
from user import User


class Library:
    def _init_(self, library_name):
        self.library_name = library_name
        self.books = []
        self.employees = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee hired: {employee.name}")


if _name_ == "_main_":
    my_lib = Library("Biblioteka Uniwersetycka")
    writer = Author("Andrzej Sapkowski", "Polish fantasy writer")
    b1 = Book("The Witcher", "978-0316029131", writer)
    e1 = Employee("Marek", 101, "Librarian")
    u1 = User("Ivan", 501)

    my_lib.add_book(b1)
    my_lib.add_employee(e1)

    print(f"\nWelcome to {my_lib.library_name}!")
    print(f"Staff on duty: {e1}")
    print(f"Newest user: {u1}")

    input("\nPress Enter to exit...")