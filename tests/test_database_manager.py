import unittest
import sqlite3
from src.database_manager import DatabaseManager


class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db_file = 'test_library.db'
        self.db_manager = DatabaseManager(self.db_file)
        self.db_manager.add_user('test_user', 'test_password')
        self.user_id = self.db_manager.get_user_id('test_user')

    def tearDown(self):
        conn = sqlite3.connect(self.db_file)
        conn.execute('DROP TABLE IF EXISTS users')
        conn.execute('DROP TABLE IF EXISTS books')
        conn.close()
        del self.db_manager

    def test_add_user(self):
        self.assertIsNotNone(self.user_id)

    def test_add_book(self):
        self.db_manager.add_book(self.user_id, 'Test Book', 'Test Author', '2023')
        books = self.db_manager.search_book(self.user_id, 'Test Book')
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], 'Test Book')

    def test_remove_book(self):
        self.db_manager.add_book(self.user_id, 'Test Book', 'Test Author', '2023')
        books = self.db_manager.search_book(self.user_id, 'Test Book')
        book_id = books[0]['id']
        self.db_manager.remove_book(book_id)
        books = self.db_manager.search_book(self.user_id, 'Test Book')
        self.assertEqual(len(books), 0)

    def test_change_status(self):
        self.db_manager.add_book(self.user_id, 'Test Book', 'Test Author', '2023')
        books = self.db_manager.search_book(self.user_id, 'Test Book')
        book_id = books[0]['id']
        self.db_manager.change_status(book_id, 'выдана')
        books = self.db_manager.search_book(self.user_id, 'Test Book')
        self.assertEqual(books[0]['status'], 'выдана')

if __name__ == '__main__':
    unittest.main()