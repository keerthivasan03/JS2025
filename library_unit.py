import unittest

class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book_title):
        self.collection.append(book_title)

    def has_book(self, book_titl):
        return book_titl in self.collection

# Unit test for the Library system
class TestLibrary(unittest.TestCase):

    def test_adding_book_to_library(self):
        # Arrange
        librry = Library()
        new_book = "Python Design Patterns"

        # Act
        librry.add_book(new_book)

        # Assert
        self.assertTrue(librry.has_book(new_book))

# Running the test
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
