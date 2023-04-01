
# Part 1

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.checked_out_copies = 0
        
    def get_title(self):
        return self.title
        
    def get_author(self):
        return self.author
        
    def get_total_copies(self):
        return self.total_copies
        
    def get_available_copies(self):
        return self.total_copies - self.checked_out_copies
    
    def checkout(self):
        if self.get_available_copies() > 0:
            self.checked_out_copies += 1
            return "You have checked out this book."
        else:
            return "No copies of this book are available."
    
    def return_book(self):
        if self.checked_out_copies > 0:
            self.checked_out_copies -= 1
            return "You have returned this book."
        else:
            return "No copies of this book are checked out."
            
# Part 2

class Person:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def get_name(self):
        return self.name
    
    def check_out_book(self, book):
        if len(self.books) < 3:
            self.books.append(book)
            return "You have checked out this book."
        else:
            return "You have reached the maximum number of checked out books."
        
    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return "You have returned this book"
        else:
            return "You did not check out this book."

# Part 3

class Library:
    def __init__(self):
        self.persons = []
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return "You added this book."

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return "You removed this book."
        else:
            return "Cannot remove book. It is checked out."
    
    def find_book(self, title):
        self.book_finds = []
        for book in self.books:
            if title == book.get_title():
                self.book_finds.append(title)
        return self.book_finds

    def get_total_books(self): 
        return len(self.books)
    
    def get_available_books(self):
        return self.get_total_books() - self.get_checked_out_books()
    
    def get_checked_out_books(self):
        self.checked_out = 0
        for book in self.books:
            if book.get_available_copies() == 0:
                self.checked_out += 1
        return self.checked_out
    
    def get_borrowed_books(self, person):
        return person.books
    
    def check_out_book(self, person, book):
        if book.get_available_copies() > 0 and book in self.books:
            book.checked_out_copies += 1
            return person.check_out_book(book)
        else:
            return "This book is not in the Library or no copies are available."

    def return_book(self, person, book):
        if book.checked_out_copies() > 0 and book in self.books:
            book.checked_out_copies -= 1
            return person.return_book(book)
        else:
            return "This book is not the Library or you did not check out this book."
        

myBook = Book("Hello World", "Greg", 5)
myBook2 = Book("Hello Space", "Anna", 7)
myBook3 = Book("Kings and Queens", "Joe", 8)
myBook4 = Book("Knights and Soldiers", "Trey", 3)
myBook5 = Book("Servants and Merchants", "Jack", 4)
myBook6 = Book("Peasants and Slaves", "Martin", 12)

myPerson = Person("Bob")
myPerson2 = Person("Amy")
myPerson3 = Person("Bill")
myPerson4 = Person("Toad")

myLibrary = Library()
myLibrary.add_book(myBook)
myLibrary.add_book(myBook2)
myLibrary.add_book(myBook3)
myLibrary.add_book(myBook4)
myLibrary.add_book(myBook5)
myLibrary.add_book(myBook6)