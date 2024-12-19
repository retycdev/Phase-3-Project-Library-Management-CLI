# Library Management System

## Project Description
The **Library Management System** is a Command-Line Interface (CLI) application developed in Python to streamline the management of books, borrowers, and loan records for a small library. This project leverages **SQLAlchemy ORM** to handle database operations and ensures best practices in Python programming, including proper package structure, virtual environment setup, and use of Python collections such as lists, dictionaries, and tuples.

This project is part of a phase 3 assignment, focusing on practical implementation of CLI tools and database integration.

---

## Features
- **Books Management**
  - Add new books with title, author, and number of copies.
  - View a list of all books in the library.
  - Delete books from the library.
- **Borrowers Management**
  - Add new borrowers with name and email.
  - View a list of all borrowers and their active loans.
  - Delete borrowers (only if they have no active loans).
- **Loans Management**
  - Borrow books by associating a borrower with a book.
  - Return borrowed books, updating availability.
  - Delete loans.
- **Database Integrity**
  - Ensure relational integrity between books, borrowers, and loans.
  - Automatically handle availability of books upon borrowing and returning.

---

## Project Structure
The project is organized into a modular structure:

```
library_management/
├── cli.py             # Main CLI interface for user interaction
├── database.py        # Database setup and SQLAlchemy engine configuration
├── models.py          # ORM models for Book, Borrower, and Loan
├── Pipfile            # Pipenv configuration for dependencies
├── library.db         # SQLite database (generated after first run)
└── README.md          # Project documentation
```

---

## Technologies Used
- **Python**
  - Core programming language for the application.
- **SQLAlchemy ORM**
  - For database management and handling relationships between tables.
- **SQLite**
  - Lightweight, file-based database for storage.
- **Pipenv**
  - For dependency management and virtual environment.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Pipenv (Install using `pip install pipenv`)

### Steps to Set Up
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

Upon running the application, you will see a menu with the following options:

```
Library Management System
1. Add a Book
2. View Books
3. Add a Borrower
4. View Borrowers
5. Borrow a Book
6. Return a Book
7. Delete a Borrower
8. Delete a Book
9. Delete a Loan
10. Exit
```

### Example Workflows
#### Adding a Book
1. Select **Option 1**.
2. Enter the book title, author, and number of copies when prompted.

#### Borrowing a Book
1. Select **Option 5**.
2. Enter the borrower ID and book ID to create a loan.

#### Returning a Book
1. Select **Option 6**.
2. Provide the loan ID to mark the book as returned.

#### Viewing Borrowers
1. Select **Option 4**.
2. See a list of all borrowers and their active loans.

---

## Database Structure
The application uses a relational database with three tables:

1. **Books**
   - `id` (Primary Key)
   - `title`
   - `author`
   - `copies_available`

2. **Borrowers**
   - `id` (Primary Key)
   - `name`
   - `email`

3. **Loans**
   - `id` (Primary Key)
   - `book_id` (Foreign Key)
   - `borrower_id` (Foreign Key)
   - `date_borrowed`
   - `date_returned`

---

## Best Practices Followed
- **Modular Code**: Separate files for CLI logic, models, and database configuration.
- **SQLAlchemy ORM**: Ensures easy database management with proper relationships.
- **Virtual Environment**: Dependencies isolated using Pipenv.
- **Error Handling**: Includes checks for invalid operations (e.g., deleting a borrower with active loans).

---

## Future Enhancements
- Add user authentication for secure access.
- Introduce reporting features to view loan history over time.
- Add support for overdue book notifications.

---


