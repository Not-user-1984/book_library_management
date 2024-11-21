import json
import os
import random
import string
from typing import List, Dict, Union
from .animation import Animation
from .validation_json import (
    is_unique_username,
    is_unique_book_title,
    is_valid_year)


class JsonManager:
    """Класс для управления данными в JSON-файле."""

    @staticmethod
    def load_library(db_file) -> List[Dict[str, Union[int, str]]]:
        """Загружает библиотеку из JSON-файла."""
        if os.path.exists(db_file):
            with open(db_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    @staticmethod
    def save_library(
        library: List[Dict[str, Union[int, str]]],
        db_file
    ) -> None:
        """Сохраняет библиотеку в JSON-файл."""
        with open(db_file, 'w', encoding='utf-8') as file:
            json.dump(library, file, indent=4)

    @staticmethod
    def generate_id(items: List[Dict[str, Union[int, str]]]) -> int:
        """Генерирует уникальный ID для нового элемента."""
        if items:
            return max(item['id'] for item in items) + 1
        return 1

    @staticmethod
    def add_book(
        books: List[Dict[str, Union[int, str]]],
        title: str, author: str, year: str
    ) -> None:
        """Добавляет новую книгу в библиотеку."""
        if not is_unique_book_title(books, title):
            print("Книга с таким названием уже существует.")
            return

        if not is_valid_year(year):
            print("Неверный год издания.")
            return

        book = {
            'id': JsonManager.generate_id(books),
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        books.append(book)
        print(f"Книга '{title}' добавлена с ID {book['id']}.")
        Animation.animate_success("Книга успешно добавлена")

    @staticmethod
    def remove_book(
        books: List[Dict[str, Union[int, str]]],
        book_id: int
    ) -> None:
        """Удаляет книгу из библиотеки."""
        for book in books:
            if book['id'] == book_id:
                books.remove(book)
                Animation.animate_success("Книга успешно удалена")
                return
        print(f"Книга с ID {book_id} не найдена.")

    @staticmethod
    def search_book(
        books: List[Dict[str, Union[int, str]]],
        query: str
    ) -> List[Dict[str, Union[int, str]]]:
        """Ищет книги в библиотеке."""
        found_books = []
        for book in books:
            if query in book['title'] or query in book['author'] or query == book['year']:
                found_books.append(book)
        return found_books

    @staticmethod
    def display_books(books: List[Dict[str, Union[int, str]]]) -> None:
        """Отображает все книги в библиотеке."""
        if books:
            print("Список всех книг:")
            for book in books:
                print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
        else:
            print("Библиотека пуста.")

    @staticmethod
    def change_status(books: List[Dict[str, Union[int, str]]], book_id: int, new_status: str) -> None:
        """Изменяет статус книги."""
        for book in books:
            if book['id'] == book_id:
                book['status'] = new_status
                Animation.animate_success("Статус книги успешно изменен")
                return
        print(f"Книга с ID {book_id} не найдена.")

    @staticmethod
    def generate_user_id(users: List[Dict[str, Union[int, str]]]) -> str:
        """Генерирует уникальный ID для нового пользователя, включающий буквы и цифры."""
        characters = string.ascii_letters + string.digits
        while True:
            user_id = ''.join(random.choice(characters) for _ in range(8))
            if users is None:
                return user_id
            if not any(user is not None and user['id'] == user_id for user in users):
                return user_id

    @staticmethod
    def check_user_by_id(
        users: List[Dict[str, Union[int, str]]],
        user_id: int
    ) -> bool:
        """Проверяет существование пользователя по ID."""
        for user in users:
            if user['id'] == user_id:
                return True
        return False

    @staticmethod
    def create_user(
        users: List[Dict[str, Union[int, str]]],
        username: str, password: str
    ) -> None:
        """Создает нового пользователя."""
        if not is_unique_username(users, username):
            print("Пользователь с таким именем уже существует.")
            return None

        user_id = JsonManager.generate_user_id(users)
        user = {
            'id': user_id,
            'username': username,
            'password': password,
            'books': [],
        }
        users.append(user)
        print(f"Пользователь '{username}' создан с ID {user_id}.")
        Animation.animate_success("Пользователь успешно создан")
        return user_id
