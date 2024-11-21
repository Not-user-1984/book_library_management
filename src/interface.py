from typing import Union
from .database_manager import DatabaseManager
from .json_manager import JsonManager

DATABASE_FILE = 'library.db'
JSON_FILE = 'test_library.json'


class Interface:
    """Класс для взаимодействия с пользователем."""

    @staticmethod
    def choose_storage(is_test: bool = False) -> str:
        """Выбор системы хранения данных."""
        while True:
            choice = input(
                "Выберите систему хранения данных (1 - SQLite, 2 - JSON): "
            )
            if choice in ['1', '2']:
                return 'sqlite' if choice == '1' else 'json'
            print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def create_user(
        storage: str,
        is_test: bool = False
    ) -> Union[DatabaseManager, JsonManager]:
        """Создание пользователя и инициализация системы хранения данных."""
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")

        if storage == 'sqlite':
            db_file = DATABASE_FILE
            db_manager = DatabaseManager(db_file)
            db_manager.add_user(username, password)
            user_id = db_manager.get_user_id(username)
            return db_manager, user_id

        db_file = JSON_FILE
        json_manager = JsonManager()
        library = json_manager.load_library(db_file)
        user_id = json_manager.create_user(library, username, password)
        json_manager.save_library(library, db_file)
        return json_manager, user_id

    @staticmethod
    def authenticate_user(
        storage: str,
        is_test: bool = False
    ) -> Union[DatabaseManager, JsonManager]:
        """Аутентификация пользователя."""
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")

        if storage == 'sqlite':
            db_file = DATABASE_FILE
            db_manager = DatabaseManager(db_file)
            user_id = db_manager.authenticate_user(username, password)
            if user_id:
                return db_manager, user_id
            else:
                print("Неверное имя пользователя или пароль.")
                return None, None
        else:
            db_file = JSON_FILE
            json_manager = JsonManager()
            library = json_manager.load_library(db_file)
            for user in library:
                if user['username'] == username and user['password'] == password:
                    return json_manager, user['id']
            print("Неверное имя пользователя или пароль.")
            return None, None

    @staticmethod
    def add_book_ui(
        manager: Union[DatabaseManager, JsonManager],
        user_id: str
    ) -> None:
        """Добавление книги через пользовательский интерфейс."""
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        if isinstance(manager, DatabaseManager):
            manager.add_book(user_id, title, author, year)
        else:
            db_file = JSON_FILE
            library = manager.load_library(db_file)
            try:
                user = next(u for u in library if u['id'] == user_id)
                manager.add_book(user['books'], title, author, year)
                manager.save_library(library, db_file)
            except StopIteration:
                print(f"Пользователь с ID {user_id} не найден.")

    @staticmethod
    def remove_book_ui(
        manager: Union[DatabaseManager, JsonManager],
        user_id: str
    ) -> None:
        """Удаление книги через пользовательский интерфейс."""
        book_id = int(input("Введите ID книги для удаления: "))
        if isinstance(manager, DatabaseManager):
            manager.remove_book(book_id)
        else:
            db_file = JSON_FILE
            library = manager.load_library(db_file)
            try:
                user = next(u for u in library if u['id'] == user_id)
                manager.remove_book(user['books'], book_id)
                manager.save_library(library, db_file)
            except StopIteration:
                print(f"Пользователь с ID {user_id} не найден.")

    @staticmethod
    def search_book_ui(
        manager: Union[DatabaseManager, JsonManager],
        user_id: str
    ) -> None:
        """Поиск книги через пользовательский интерфейс."""
        query = input("Введите название, автора или год издания для поиска: ")
        if isinstance(manager, DatabaseManager):
            found_books = manager.search_book(user_id, query)
        else:
            db_file = JSON_FILE
            library = manager.load_library(db_file)
            try:
                user = next(u for u in library if u['id'] == user_id)
                found_books = manager.search_book(user['books'], query)
            except StopIteration:
                print(f"Пользователь с ID {user_id} не найден.")
                return
        if found_books:
            print("Найденные книги:")
            for book in found_books:
                print(
                    f"""
                    ID: {book['id']},
                    Название: {book['title']},
                    Автор: {book['author']},
                    Год: {book['year']},
                    Статус: {book['status']}
            """)
        else:
            print("Книги не найдены.")

    @staticmethod
    def display_books_ui(
        manager: Union[DatabaseManager, JsonManager],
        user_id: str
    ) -> None:
        """Отображение всех книг через пользовательский интерфейс."""
        if isinstance(manager, DatabaseManager):
            manager.display_books(user_id)
        else:
            db_file = JSON_FILE
            library = manager.load_library(db_file)
            try:
                user = next(u for u in library if u['id'] == user_id)
                manager.display_books(user['books'])
            except StopIteration:
                print(f"Пользователь с ID {user_id} не найден.")

    @staticmethod
    def change_status_ui(
        manager: Union[DatabaseManager, JsonManager],
        user_id: str
    ) -> None:
        """Изменение статуса книги через пользовательский интерфейс."""
        book_id = int(input("Введите ID книги для изменения статуса: "))
        new_status = input("Введите новый статус (в наличии/выдана): ")
        if isinstance(manager, DatabaseManager):
            manager.change_status(book_id, new_status)
        else:
            db_file = JSON_FILE
            library = manager.load_library(db_file)
            try:
                user = next(u for u in library if u['id'] == user_id)
                manager.change_status(user['books'], book_id, new_status)
                manager.save_library(library, db_file)
            except StopIteration:
                print(f"Пользователь с ID {user_id} не найден.")

    @staticmethod
    def user_menu(
        manager: Union[DatabaseManager, JsonManager],
        user_id: str
    ) -> None:
        """Меню действий для аутентифицированного пользователя."""
        while True:
            print("\nМеню:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Поиск книги")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("6. Выйти")

            choice = input("Выберите действие: ")

            if choice == '1':
                Interface.add_book_ui(manager, user_id)
            elif choice == '2':
                Interface.remove_book_ui(manager, user_id)
            elif choice == '3':
                Interface.search_book_ui(manager, user_id)
            elif choice == '4':
                Interface.display_books_ui(manager, user_id)
            elif choice == '5':
                Interface.change_status_ui(manager, user_id)
            elif choice == '6':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def main(is_test: bool = False) -> None:
        """Основной цикл программы."""
        storage = Interface.choose_storage(is_test)

        while True:
            choice = input(
                "Выберите действие (1 - Вход, 2 - Регистрация, 3 - Выход): ")
            if choice == '1':
                manager, user_id = Interface.authenticate_user(
                    storage, is_test)
                if manager and user_id:
                    Interface.user_menu(manager, user_id)
                    break
            elif choice == '2':
                manager, user_id = Interface.create_user(storage, is_test)
                if manager and user_id:
                    Interface.user_menu(manager, user_id)
                    break
            elif choice == '3':
                print("Выход из программы.")
                return
            else:
                print("Неверный выбор. Попробуйте снова.")
