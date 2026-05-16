# Library management system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Checked out"
            print(f"{book} - {status}")
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You have checked out '{book}'")
                return
        print(f"Sorry, '{title}' is not available.")

library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.display_books()
library.check_out_book("The Great Gatsby")
library.display_books()


