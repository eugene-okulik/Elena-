class Book:
    mat_pages = 'paper'
    have_text = True

    def __init__(self, name_book, author, num_pages, isbn):
        self.name_book = name_book
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = False

    def reserve(self):
        self.reserved = True

    def __str__(self):
        status_reserved = 'Reserved' if self.reserved else "Not reserved"
        return (f'Name of the book: {self.name_book}, Author: {self.author}, Number of pages: {self.num_pages}, '
                f'ISBN: {self.isbn}, Material: {self.mat_pages}, {status_reserved}')


book_1 = Book('The Idiot', 'F.Dostoevsky', 1000, '1234567')
book_2 = Book('To kill a mockingbird', 'H.Lee', 544, '1234568')
book_3 = Book('1984', 'G.Orwell', 790, '1234569')
book_4 = Book('Pride and prejudice', 'J.Austen', 800, '1234570')
book_5 = Book('The Great Gatsby', 'F.Scott', 740, '1234571')
book_3.reserve()

print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)


class Textbook(Book):
    def __init__(self, name_book, author, num_pages, isbn, subject, grade, have_tasks):
        super().__init__(name_book, author, num_pages, isbn)
        self.subject = subject
        self.grade = grade
        self.have_tasks = have_tasks

    def __str__(self):
        status_reserved = 'Reserved' if self.reserved else ""
        return (f'Name of the book: {self.name_book}, Author: {self.author}, Number of pages: {self.num_pages}, '
                f'Subject: {self.subject}, Grade: {self.grade}, {status_reserved}')


textbook_1 = Textbook('Algebra', 'Ivanov', 250, '234567', "Math", 9, True)
textbook_2 = Textbook('Art', 'Petrov', 100, '234568', 'Art', 6, True)
textbook_3 = Textbook('Geography of Asia', 'Sidorov', 100, '234569', 'Geography', 8, True)
textbook_4 = Textbook('History', 'Kuznetsov', 150, '2334570', 'History', 7, False)
textbook_5 = Textbook('Testing', 'Okulik', 200, '234571', 'IT', 10, True)
textbook_5.reserve()

print(textbook_1)
print(textbook_2)
print(textbook_3)
print(textbook_4)
print(textbook_5)
