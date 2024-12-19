from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    copies_available = Column(Integer, default=1)

class Borrower(Base):
    __tablename__ = 'borrowers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    borrower_id = Column(Integer, ForeignKey('borrowers.id'), nullable=False)
    loan_date = Column(Date, nullable=False)
    return_date = Column(Date)

    book = relationship('Book', back_populates='loans')
    borrower = relationship('Borrower', back_populates='loans')

Book.loans = relationship('Loan', back_populates='book', cascade='all, delete')
Borrower.loans = relationship('Loan', back_populates='borrower', cascade='all, delete')
