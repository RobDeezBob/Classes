
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

    def get_checked_out_books(self):
        return self.books

# Part 3 Unfinshed

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
        if title in self.books:
            self.book_finds.append(title)
        return self.book_finds

    def get_total_books(self):
        return len(self.books)
    
    def get_available_books(self):
        return self.get_total_books() - self.get_checked_out_books()
    
    def get_checked_out_books(self):
        return ""
    
    def get_borrowed_books(self, person):
        return person.get_checked_out_books()
    
    def check_out_book(self, person, book):
        return ""
    def return_book(self, person, book):
        return ""

myLibrary = Library()
myLibrary.add_book("Hello World")
myLibrary.add_book("Hello Space")
myLibrary.add_book("Kings and Queens")
myLibrary.add_book("Knights and Soldiers")
myLibrary.add_book("Servants and Merchants")
myLibrary.add_book("Peasants and Slaves")

myPerson = Person("Bob")
myPerson.check_out_book("Hello Space")
myPerson.check_out_book("Hello Servants and Merchants")
myPerson.check_out_book("Hello Servants and Merchants")

print(myLibrary.get_borrowed_books(myPerson))