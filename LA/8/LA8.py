class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(book1.title, book1.author)
print(book2.title, book2.author)

del book1.author

print(book2.title, book2.author)
