import unittest
import os
import sqlite3
from src.interface import Interface


class TestRunner:
    @staticmethod
    def run_tests():
        # Очистка тестовой базы данных перед запуском тестов
        test_db_file = 'test_library.db'
        if os.path.exists(test_db_file):
            os.remove(test_db_file)

        # Запуск тестов
        test_suite = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == '__main__':
    TestRunner.run_tests()
