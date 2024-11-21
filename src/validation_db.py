import datetime


def is_unique_username(cursor, username):
    """Проверяет, что имя пользователя уникально."""
    cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    return cursor.fetchone() is None


def is_unique_book_title(cursor, user_id, title):
    """Проверяет, что название книги уникально для данного пользователя."""
    cursor.execute(
        'SELECT id FROM books WHERE user_id = ? AND title = ?',
        (user_id, title))
    return cursor.fetchone() is None


def is_valid_year(year):
    """Проверяет, что год находится в диапазоне от 0 до текущего года."""
    current_year = datetime.datetime.now().year
    try:
        year = int(year)
        return 0 <= year <= current_year
    except ValueError:
        return False