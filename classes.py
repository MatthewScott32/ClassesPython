#Classes Lesson

#book_one= {   #doing this over and over is annoying, so make a class
 #   "title": "Harry Potter & the Sorcer's Stone",
 #   "author": "J.K. Rowling",
 #    "pages": 251,
#}

class Book: #example 1
    def __init__(self):
# Establish the properties of each book
# with a default value
        self.title = ""
        self.publisher = ""
        self.author = ""
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page


book_one = Book()
book_one.title = "Harry Potter and the Sorcerer's Stone"
book_one.author = "J.K. Rowling"
book_one.current_page = 1
print(f'I am reading {book_one.title} by {book_one.author}')

book_one.start_reading()

book_two = Book()
book_two.title = "Harry Potter and the Chamber of Secrets"
book_two.author = "J.K. Rowling"
book_two.current_page = 197
print(f'I am reading {book_two.title} by {book_two.author}')

book_two.start_reading()


class Book: #example 2
    def __init__(self, author, title):
# Establish the properties of each book
# with a default value
        self.title = title
        self.publisher = ""
        self.author = author
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page


book_one = Book("J.K. Rowling" , "Harry Potter and the Sorcerer's Stone")
print(f'I am reading {book_one.title} by {book_one.author}')

book_one.start_reading()

book_two = Book("J.K. Rowling", "Harry Potter and the Chamber of Secrets")
print(f'I am reading {book_two.title} by {book_two.author}')

book_two.start_reading()