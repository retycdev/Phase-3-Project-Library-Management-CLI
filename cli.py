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
        print("7. Delete a Book")
        print("8. Exit")

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
def add_borrower():
    name = input("Enter borrower's name: ")
    email = input("Enter borrower's email: ")

    borrower = Borrower(name=name, email=email)
    session.add(borrower)
    session.commit()
    print(f"Borrower '{name}' added successfully!")

def delete_borrower():
    borrower_id = int(input("Enter the ID of the borrower to delete: "))
    borrower = session.query(Borrower).get(borrower_id)

    if borrower:
        # Check if the borrower has active loans
        if borrower.loans:
            print("Borrower has active loans. Please delete the loans first.")
        else:
            session.delete(borrower)
            session.commit()
            print(f"Borrower '{borrower.name}' has been deleted successfully.")
    else:
        print("Borrower not found.")

def borrow_book():
    view_books()
    book_id = int(input("Enter book ID to borrow: "))
    borrower_id = int(input("Enter borrower ID: "))

    book = session.query(Book).get(book_id)
    if book.copies_available > 0:
        loan = Loan(book_id=book_id, borrower_id=borrower_id, loan_date=date.today())
        book.copies_available -= 1
        session.add(loan)
        session.commit()
        print(f"Book '{book.title}' borrowed successfully!")
    else:
        print("No copies available.")
def return_book():
    loan_id = int(input("Enter loan ID to return: "))
    loan = session.query(Loan).get(loan_id)

    if loan:
        book = session.query(Book).get(loan.book_id)
        book.copies_available += 1
        session.delete(loan)
        session.commit()
        print(f"Book '{book.title}' returned successfully!")
    else:
        print("Loan record not found.")
