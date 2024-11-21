# Управление библиотекой книг

Этот проект представляет собой программу для управления библиотекой книг. Пользователи могут добавлять, удалять, искать и изменять статус книг. Программа поддерживает две системы хранения данных: SQLite и JSON.

## Описание

Программа предоставляет пользовательский интерфейс для выполнения следующих действий:

1. **Регистрация и аутентификация пользователя**:
   - Пользователи могут зарегистрироваться и войти в систему.
   - Поддерживаются две системы хранения данных: SQLite и JSON.

2. **Управление книгами**:
   - **Добавление книги**: Пользователи могут добавлять книги в свою библиотеку, указывая название, автора и год издания.
   - **Удаление книги**: Пользователи могут удалять книги из своей библиотеки по ID.
   - **Поиск книги**: Пользователи могут искать книги по названию, автору или году издания.
   - **Отображение всех книг**: Пользователи могут просматривать все книги в своей библиотеке.
   - **Изменение статуса книги**: Пользователи могут изменять статус книги (например, "в наличии" или "выдана").

## Установка и запуск

1. **Клонируйте репозиторий**:
   ```bash
   git clone git@github.com:Not-user-1984/book_library_management.git
   cd book-library-management
   ```

2. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Запустите программу**:
   ```bash
   python run.py
   ```

## Структура проекта

- **`database_manager.py`**: Класс для управления базой данных SQLite.
- **`json_manager.py`**: Класс для управления данными в формате JSON.
- **`interface.py`**: Класс для взаимодействия с пользователем.
- **`main.py`**: Основной файл для запуска программы.
- **`animation.py`**: Класс для анимации сообщений (необязательный).

## Использование

1. **Выбор системы хранения данных**:
   - При запуске программы пользователь выбирает систему хранения данных (SQLite или JSON).

2. **Регистрация и вход**:
   - Пользователь может зарегистрироваться или войти в систему.

3. **Управление книгами**:
   - После входа пользователь может добавлять, удалять, искать и изменять статус книг.

## Пример работы

```bash
Выберите систему хранения данных (1 - SQLite, 2 - JSON): 1
Выберите действие (1 - Вход, 2 - Регистрация, 3 - Выход): 2
Введите имя пользователя: user1
Введите пароль: password1

Меню:
1. Добавить книгу
2. Удалить книгу
3. Поиск книги
4. Отобразить все книги
5. Изменить статус книги
6. Выйти

Выберите действие: 1
Введите название книги: Приключения Тома Сойера
Введите автора книги: Марк Твен
Введите год издания книги: 1876
Книга успешно добавлена
```

## Тестирование

Для запуска тестов используйте следующую команду:

```bash
python run_tests.py
```
