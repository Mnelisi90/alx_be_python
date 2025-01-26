class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to indicate when a Book instance is being deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for end-user readability."""
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation suitable for debugging or recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)  # Uses __str__
    print(repr(my_book))  # Uses __repr__
    del my_book  # Uses __del__

if __name__ == "__main__":
    main()        