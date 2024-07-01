import unittest
import os
from library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library('test_library.json')

    def tearDown(self):
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')

    def test_add_book(self):
        self.library.add_book('Test Book', 'Test Author')
        books = self.library.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], 'Test Book')
        self.assertEqual(books[0]['author'], 'Test Author')

    def test_delete_book(self):
        self.library.add_book('Test Book', 'Test Author')
        self.library.delete_book('Test Book')
        books = self.library.list_books()
        self.assertEqual(len(books), 0)

    def test_list_books(self):
        self.library.add_book('Test Book 1', 'Test Author 1')
        self.library.add_book('Test Book 2', 'Test Author 2')
        books = self.library.list_books()
        self.assertEqual(len(books), 2)

    def test_find_book(self):
        self.library.add_book('Test Book', 'Test Author')
        book = self.library.find_book('Test Book')
        self.assertIsNotNone(book)
        self.assertEqual(book['title'], 'Test Book')
        self.assertEqual(book['author'], 'Test Author')

if __name__ == '__main__':
    unittest.main()
