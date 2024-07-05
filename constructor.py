class Book:
    
    #constructor
    def __init__(self, book_name):
        self.book_name =book_name
        print('My book name is ',book_name)

    def chapter1(self):
        print('You are reading the chapter 1')

    def current_reading(self):
        print('Currently I am reading the ',self.book_name)  



# creation of object
harry_potter = Book('harry potter')

harry_potter.chapter1()
harry_potter.current_reading()
