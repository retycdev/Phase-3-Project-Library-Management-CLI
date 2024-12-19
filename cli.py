from database import SessionLocal
from models import Book, Borrower, Loan
from datetime import date

session = SessionLocal()

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Add a Borrower")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            add_borrower()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    copies = int(input("Enter number of copies: "))

    book = Book(title=title, author=author, copies_available=copies)
    session.add(book)
    session.commit()
    print(f"Book '{title}' added successfully!")
def view_books():
    books = session.query(Book).all()
    for book in books:
        print(f"{book.id}: {book.title} by {book.author} ({book.copies_available} copies available)")
