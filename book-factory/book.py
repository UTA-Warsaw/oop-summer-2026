import random


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"


def generate_random_book():
    titles = ["Sun", "Moon", "Ocean", "Forest", "City"]
    authors = ["Alice", "Bob", "Charlie", "Diana"]

    return Book(
        random.choice(titles),
        random.choice(authors),
        random.randint(80, 600),
    )


if __name__ == "__main__":
    book = generate_random_book()
    print(book)
    
