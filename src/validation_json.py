import datetime


def is_unique_username(users, username):
    """Проверяет, что имя пользователя уникально."""
    return not any(user['username'] == username for user in users)


def is_unique_book_title(books, title):
    """Проверяет, что название книги уникально."""
    return not any(book['title'] == title for book in books)


def is_valid_year(year):
    """Проверяет, что год находится в диапазоне от 0 до текущего года."""
    current_year = datetime.datetime.now().year
    try:
        year = int(year)
        return 0 <= year <= current_year
    except ValueError:
        return False