import csv

# Validate input information
def book_validate():
    # User input book title
    title = input("Please, input book title: ").title()
    if len(title) == 0:
        print("Title can't be empty!")
        return
    # User input book author
    author = input("Please, input book author: ").title()
    if len(author) == 0:
        print("Author can't be empty!")
        return
    # Try user input integer for years
    try:
        year = int(input("Please, input book publish year: "))
    except ValueError:
        print("Input year is not correct!")
        return
    # If every input is valid, return information
    return title, author, year

# Validate user answers
def answer_validate(answer):
    # Dict for operations
    answers_dict = {
        "y" : "yes",
        "yes" : "yes",
        "a" : library.append,
        "append" : library.append,
        "s" : library.search,
        "search" : library.search,
        "i" : library.append,
        "info" : library.append,
    }
    
    # Check if answer parameter is in dictionary and return it
    if answer in answers_dict:
        return answers_dict[answer]

# This is search function
def search_title(title, lst):
    for obj in lst:
        if obj.title == title:
            return obj
    return False

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
    
    # This method adds book in the library
    def append(self):
        print("\nAdding book...")
        # Used while loop if user wants to add more and more books
        while True:
            # Try to unpack variables from book validation function
            try:
                title, author, year = book_validate()
            except:
                answer = input("Try again? y/n ").lower()
                # If inputted info is not valid, ask user wants or not add book again
                if not answer_validate(answer) == "yes":
                    break
            else:
                # If get valid info, add book object in the library
                new_book = Book(title, author, year)
                self.book_list.append(new_book)
                print("\nBook added\n")
                answer = input("Do you want to add more book? y/n ")
                # Prompt user, wants or not add book again
                if not answer_validate(answer) == "yes":
                    break
                
    # This method will search book in the library based title given by user
    def search(self):
        # Checking if library is empty or not
        if self.empty():
            print("Library is empty")
        else:
            book_title = input("\nPlease, input book title for search: ").title()
            book = search_title(book_title, self.book_list)
            if book:
                print(f"The book you search, there is in the library -> {book}")
                # If there is book in the library, prompt user wants search again or not
                answer = input("Do you want to search again? ")
                if answer_validate(answer) == "yes":
                    self.search()
            else:
                print("There is not a book in the library")
                # If there is not book in the library, prompt user wants add book or not
                answer = input("Do you want add it to library? ")
                if answer_validate(answer) == "yes":
                    self.append()
        
    # This method prints all books information in library
    def display_books(self):
        # Checking if library is empty or not
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
        csv_list = [{"title" : book.title, "author" : book.author, "year" : book.year} for book in self.book_list]
        headers = ["title", "author", "year"]
        with open("Library.csv", "a+", newline="") as books:
            books.seek(0)
            writer = csv.DictWriter(books, fieldnames=headers)
            if len(books.readlines()) == 0:
                writer.writeheader()
            writer.writerows(csv_list)
            
# Create bookmanager object
library = BookManager()

# Manually add books
library.append()

# Ask user what operation wants
answer = input("What do you want to do with library? ").strip().lower()

# Call library methods based user inputted command
try:
    answer_validate(answer)()
except TypeError:
    print("Please, inpute valid command!")

# Finally add books to csv file
library.create_books_file()