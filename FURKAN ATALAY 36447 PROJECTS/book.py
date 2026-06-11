class Book:
    def _init_(self, title, isbn, author):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.is_available = True

    def _str_(self):
        return f"'{self.title}' (ISBN: {self.isbn})"