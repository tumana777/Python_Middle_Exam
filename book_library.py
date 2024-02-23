import csv

# Create book class
class Book:
    # Initialize parameters
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    # Magic method to return book class info instead displaying just object
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# Create bookmanager class
class BookManager:
    # At the beginning, book library is empty
    book_list = []
    
    # This method returns if library is empty or not
    def empty(self):
        return len(self.book_list) == 0
        
    # This method prints all books information in library
    def display_books(self):
        if self.empty():
            print("Library is empty")
        else:
            # Print books amount
            print(f"There are {len(self.book_list)} books in the library:")
            # Print all books info
            for book in self.book_list:
                print(book)
    
    # This method creates CSV file for library
    def create_books_file(self):
        csv_list = [[book.title, book.author, book.year] for book in self.book_list]
        with open("Library.csv", "w", newline="") as books:
            writer = csv.writer(books)
            writer.writerow(["Title", "Author", "Year"])
            writer.writerows(csv_list)