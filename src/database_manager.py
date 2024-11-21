import sqlite3
from typing import List, Dict, Union, Optional
from .animation import Animation
from .validation_db import (
    is_unique_username,
    is_unique_book_title,
    is_valid_year
    )


class DatabaseManager:
    """Класс для управления базой данных SQLite."""

    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row  # Используем словарь для строк
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self) -> None:
        """Создает таблицы в базе данных."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.conn.commit()

    def add_user(self, username: str, password: str) -> None:
        """Добавляет пользователя в базу данных."""
        if not is_unique_username(self.cursor, username):
            print("Пользователь с таким именем уже существует.")
            return

        self.cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password))
        self.conn.commit()

    def get_user_id(self, username: str) -> Optional[int]:
        """Получает ID пользователя по имени."""
        self.cursor.execute(
            'SELECT id FROM users WHERE username = ?', (username,))
        result = self.cursor.fetchone()
        return result['id'] if result else None

    def authenticate_user(
            self,
            username: str,
            password: str
            ) -> Optional[int]:
        """Аутентифицирует пользователя."""
        self.cursor.execute(
            'SELECT id FROM users WHERE username = ? AND password = ?',
            (username, password))
        result = self.cursor.fetchone()
        return result['id'] if result else None

    def add_book(
            self,
            user_id: int,
            title: str,
            author: str,
            year: str
            ) -> None:
        """Добавляет книгу в базу данных."""
        if not is_unique_book_title(self.cursor, user_id, title):
            print("Книга с таким названием уже существует.")
            return

        if not is_valid_year(year):
            print("Неверный год издания.")
            return

        self.cursor.execute('''
            INSERT INTO books (user_id, title, author, year, status)
            VALUES (?, ?, ?, ?, 'в наличии')
        ''', (user_id, title, author, year))
        self.conn.commit()
        Animation.animate_success("Книга успешно добавлена")

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу из базы данных."""
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.conn.commit()
        Animation.animate_success("Книга успешно удалена")

    def search_book(
            self,
            user_id: int,
            query: str
    ) -> List[Dict[str, Union[int, str]]]:
        """Ищет книги в базе данных."""
        self.cursor.execute('''
            SELECT * FROM books WHERE user_id = ? AND (title LIKE ? OR author LIKE ? OR year LIKE ?)
        ''', (user_id, f'%{query}%', f'%{query}%', f'%{query}%'))
        return [dict(row) for row in self.cursor.fetchall()]

    def display_books(self, user_id: str) -> None:
        """Отображает все книги пользователя."""
        self.cursor.execute(
            'SELECT * FROM books WHERE user_id = ?',
            (user_id,)
        )
        books = self.cursor.fetchall()
        if books:
            print("Список всех книг:")
            for book in books:
                print(f"""
                    ID: {book['id']},
                    Название: {book['title']},
                    Автор: {book['author']},
                    Год: {book['year']},
                    Статус: {book['status']}
            """)
        else:
            print("Библиотека пуста.")

    def change_status(self, book_id: str, new_status: str) -> None:
        """Изменяет статус книги в базе данных."""
        self.cursor.execute(
            'UPDATE books SET status = ? WHERE id = ?', (new_status, book_id))
        self.conn.commit()
        Animation.animate_success("Статус книги успешно изменен")
