class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
# Derived class for EBooks
class EBook(Book):
    def _init_(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f" {self.title} by {self.author},(File size: {self.file_size} MB)"

# Derived class for PrintBooks 
class PrintBook(Book):
    def _init_(self, title, author, page_count): 
         super().__init__(title, author)
         self.page_count = page_count
    
    def __str__(self):
        return f" {self.title} by {self.author}, (Pages: {self.page_count})"
    
  # Derived class for Library
class Library ():
    def _init_(self):
        self.books = []

    def add_book(self, books):    
        if isinstance (books, Book):
            self.book.append(books)
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)


from library_system import Book, EBook, PrintBook, Library
               

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("The Art of Seduction", "Daniel Steel")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()


