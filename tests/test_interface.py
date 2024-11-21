import unittest
from unittest.mock import patch
from src.interface import Interface
from src.database_manager import DatabaseManager
from src.json_manager import JsonManager

class TestInterface(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_choose_storage_sqlite(self, mock_input):
        storage = Interface.choose_storage()
        self.assertEqual(storage, 'sqlite')

    @patch('builtins.input', side_effect=['2'])
    def test_choose_storage_json(self, mock_input):
        storage = Interface.choose_storage()
        self.assertEqual(storage, 'json')

    @patch('builtins.input', side_effect=['test_user', 'test_password'])
    def test_create_user_sqlite(self, mock_input):
        db_manager, user_id = Interface.create_user('sqlite',)
        self.assertIsInstance(db_manager, DatabaseManager)
        self.assertIsNotNone(user_id)

    @patch('builtins.input', side_effect=['test_user', 'test_password'])
    def test_create_user_json(self, mock_input):
        json_manager, user_id = Interface.create_user('json')
        self.assertIsInstance(json_manager, JsonManager)
        # self.assertEqual(user_id, 1)

    @patch('builtins.input', side_effect=['test_user', 'test_password'])
    def test_authenticate_user_sqlite(self, mock_input):
        # Создаем пользователя перед аутентификацией
        db_manager, user_id = Interface.create_user('sqlite')
        self.assertIsInstance(db_manager, DatabaseManager)
        self.assertIsNotNone(user_id)

        # Теперь пробуем аутентифицироваться
        db_manager, user_id = Interface.authenticate_user('sqlite')
        self.assertIsInstance(db_manager, DatabaseManager)
        self.assertIsNotNone(user_id)

    @patch('builtins.input', side_effect=['test_user', 'test_password'])
    def test_authenticate_user_json(self, mock_input):
        # Создаем пользователя перед аутентификацией
        json_manager, user_id = Interface.create_user()
        self.assertIsInstance(json_manager, JsonManager)
        # self.assertEqual(user_id, 1)

        # Теперь пробуем аутентифицироваться
        json_manager, user_id = Interface.authenticate_user()
        self.assertIsInstance(json_manager, JsonManager)
        # self.assertEqual(user_id, 1)

if __name__ == '__main__':
    unittest.main()