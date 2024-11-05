class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __int__(self):
        return f"The title is {self.title}, the author is {self.author}"

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Copies Available: {self.copies_available}")





#child class/ derived class

class Librarybook(Book):
    def __init__(self, title, author, isbn, copies_available):
        super().__init__(title, author)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -=1
            return f"{self.title} borrowed. copies left {self.copies_available}"
        else:
            return f"No. of copies {self.title} available"
    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. copies left {self.copies_available}"

#usage
book1 = Librarybook("Python Programming", "John Doe", "978-3-16-148410-0", 3)
print(book1.display_info())
print(book1.borrow_book())

print(book1.return_book())


