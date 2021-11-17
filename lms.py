import datetime
import os
# os.getcwd()

class LMS:
    """four module = "Display Books", "Return Books"
    "Issue Books", Add Books" """
    def __init__(self, list_of_books, library_name) :
        self.list_of_books = "book_list.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        