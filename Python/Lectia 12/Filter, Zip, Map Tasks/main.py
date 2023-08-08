books = [
    {
        "title": "The Golden Compass",
        "author": "Phillip Pullman",
        "genre": "Fantasy"
    },
    {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "genre": "Drama"
    },
    {
        "title": "The Subtle Knife",
        "author": "Phillip Pullman",
        "genre": "Fantasy"
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Sci-fi"
    },
    {
        "title": "The Boy in the Striped Pyjamas",
        "author": "Mark Herman",
        "genre": "Drama"
    },
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy"
    },
    {
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "genre": "Fantasy"
    }
]


def filter_by_genre(book, genre):
    return book["genre"] == genre


def filter_by_author(book, author):
    return book["author"] == author


def book_to_string(book):
    return f"{book['title']} by {book['author']} ({book['genre']})"


fantasy_book = list(filter(lambda book: filter_by_genre(book, "Fantasy"), books))
rowling_books = list(filter(lambda book: filter_by_author(book, "J.K. Rowling"), books))

books_frumos = list(map(book_to_string, books))
print("All books:")
for book in books_frumos:
    print(book)

print("\nFantasy Books:")
for book in fantasy_book:
    print(book_to_string(book))

print("\nRowling Books:")
for book in rowling_books:
    print(book_to_string(book))