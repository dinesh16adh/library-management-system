class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = {}

    def print_books(self):
        print("books:")
        for book, category in self.books.items():
            print(f"- {book},(category:{category},)")

    def add_book(self, book, category):
        self.books[book] = category
        self.no_of_books += 1

    def get_no_of_books(self):
        return self.no_of_books


library = Library()
while True:
    print("enter a book name (enter 'q' to quit and get the total info):")
    book = input()
    if book == "q":
        break
    print("enter the category of the book: ")
    category = input()
    library.add_book(book, category)

print(f"final number of books : {library.get_no_of_books()}")
library.print_books()
