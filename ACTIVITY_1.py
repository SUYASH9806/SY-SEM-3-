class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Borrowed"
        print(
            f"ID: {self.book_id} | Title: {self.title} | "
            f"Author: {self.author} | Category: {self.category} | "
            f"Status: {status}"
        )


class Member:
    MAX_BOOKS = 5

    def __init__(self, member_id, name, contact):
        self.member_id = member_id
        self.name = name
        self.contact = contact
        self.borrowed_books = []

    def borrow_book(self, book_id):
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            return False
        self.borrowed_books.append(book_id)
        return True

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def display(self):
        books = ", ".join(map(str, self.borrowed_books))
        if not books:
            books = "None"

        print(
            f"ID: {self.member_id} | Name: {self.name} | "
            f"Contact: {self.contact} | Borrowed Books: {books}"
        )


# Inheritance
class Librarian(Member):
    def __init__(self, member_id, name, contact, employee_id):
        super().__init__(member_id, name, contact)
        self.employee_id = employee_id

    def display(self):
        print(
            f"Librarian ID: {self.member_id} | Name: {self.name} | "
            f"Contact: {self.contact} | Employee ID: {self.employee_id}"
        )


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # Book management
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
            return

        self.books[book.book_id] = book
        print("Book added successfully.")

    def remove_book(self, book_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if not self.books[book_id].is_available:
            print("Cannot remove a borrowed book.")
            return

        del self.books[book_id]
        print("Book removed successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n--- All Books ---")
        for book in self.books.values():
            book.display()

    def search_book(self, search):
        found = False

        for book in self.books.values():
            if (
                str(book.book_id).lower() == search.lower()
                or book.title.lower() == search.lower()
                or book.author.lower() == search.lower()
            ):
                book.display()
                found = True

        if not found:
            print("No matching book found.")

    # Member management
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member ID already exists.")
            return

        self.members[member.member_id] = member
        print("Member registered successfully.")

    def remove_member(self, member_id):
        if member_id not in self.members:
            print("Member not found.")
            return

        member = self.members[member_id]

        if member.borrowed_books:
            print("Cannot remove a member who has borrowed books.")
            return

        del self.members[member_id]
        print("Member removed successfully.")

    def display_members(self):
        if not self.members:
            print("No members registered.")
            return

        print("\n--- All Members ---")
        for member in self.members.values():
            member.display()

    # Borrowing
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.is_available:
            print("Book is already borrowed.")
            return

        if len(member.borrowed_books) >= Member.MAX_BOOKS:
            print("Member has reached the maximum borrowing limit.")
            return

        member.borrow_book(book_id)
        book.is_available = False

        print(f"'{book.title}' borrowed successfully.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        member = self.members[member_id]
        book = self.books[book_id]

        if book_id not in member.borrowed_books:
            print("This member did not borrow this book.")
            return

        member.return_book(book_id)
        book.is_available = True

        print(f"'{book.title}' returned successfully.")

    def display_borrowed_books(self):
        found = False

        print("\n--- Borrowed Books ---")

        for book in self.books.values():
            if not book.is_available:
                book.display()
                found = True

        if not found:
            print("No books are currently borrowed.")

    def display_available_books(self):
        found = False

        print("\n--- Available Books ---")

        for book in self.books.values():
            if book.is_available:
                book.display()
                found = True

        if not found:
            print("No books are currently available.")


def add_sample_data(library):
    # Sample books
    library.add_book(Book(101, "Python Programming", "John Smith", "Programming"))
    library.add_book(Book(102, "Data Structures", "Robert Brown", "Computer Science"))
    library.add_book(Book(103, "Clean Code", "Robert Martin", "Programming"))
    library.add_book(Book(104, "Database Systems", "James Anderson", "Database"))

    # Sample members
    library.add_member(Member(1, "Alice", "9876543210"))
    library.add_member(Member(2, "Bob", "9123456780"))


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    library = Library()

    # Add sample data
    add_sample_data(library)

    while True:
        print("\n================================")
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("================================")
        print("1.  Add Book")
        print("2.  Remove Book")
        print("3.  Display All Books")
        print("4.  Search Book")
        print("5.  Register Member")
        print("6.  Remove Member")
        print("7.  Display All Members")
        print("8.  Borrow Book")
        print("9.  Return Book")
        print("10. Display Borrowed Books")
        print("11. Display Available Books")
        print("12. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = get_integer("Enter Book ID: ")
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author: ").strip()
            category = input("Enter Category: ").strip()

            if not title or not author or not category:
                print("All book details are required.")
                continue

            book = Book(book_id, title, author, category)
            library.add_book(book)

        elif choice == "2":
            book_id = get_integer("Enter Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            search = input(
                "Enter Book ID, Title, or Author to search: "
            ).strip()

            if search:
                library.search_book(search)
            else:
                print("Search value cannot be empty.")

        elif choice == "5":
            member_id = get_integer("Enter Member ID: ")
            name = input("Enter Member Name: ").strip()
            contact = input("Enter Contact Number: ").strip()

            if not name or not contact:
                print("All member details are required.")
                continue

            member = Member(member_id, name, contact)
            library.add_member(member)

        elif choice == "6":
            member_id = get_integer("Enter Member ID to remove: ")
            library.remove_member(member_id)

        elif choice == "7":
            library.display_members()

        elif choice == "8":
            member_id = get_integer("Enter Member ID: ")
            book_id = get_integer("Enter Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "9":
            member_id = get_integer("Enter Member ID: ")
            book_id = get_integer("Enter Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "10":
            library.display_borrowed_books()

        elif choice == "11":
            library.display_available_books()

        elif choice == "12":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please select 1-12.")


if __name__ == "__main__":
    main()
