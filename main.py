from book import Book
from library import Library

book_one = Book("J.K. Rowling" , "Harry Potter and the Sorcerer's Stone")
print(f'I am reading {book_one.title} by {book_one.author}')


book_two = Book("J.K. Rowling", "Harry Potter and the Chamber of Secrets")
print(f'I am reading {book_two.title} by {book_two.author}')

nss_library = Library("The NSS Library")
print(nss_library.name)

nss_library.add_book(book_one)
nss_library.add_book(book_two)
