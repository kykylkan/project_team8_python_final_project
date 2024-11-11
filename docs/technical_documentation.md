# Технічна документація Assistant Bot

## AddressBook (address_book.py)

```python
class AddressBook(UserDict):
    """
    Клас для управління адресною книгою.

    Успадковується від UserDict для реалізації словника контактів.

    Attributes:
        data (dict): Словник для зберігання записів, де ключ - ім'я контакту
    """

    def add_record(self, record):
        """
        Додає новий запис до адресної книги.

        Args:
            record (Record): Об'єкт запису для додавання

        Returns:
            str: Повідомлення про успішне додавання контакту
        """
        pass

    def find(self, name):
        """
        Пошук запису за ім'ям контакту.

        Args:
            name (str): Ім'я контакту для пошуку

        Returns:
            Record or None: Знайдений запис або None, якщо запис не знайдено
        """
        pass

    def get_upcoming_birthdays(self, days=7):
        """
        Повертає список контактів, у яких день народження у найближчі дні.

        Args:
            days (int, optional): Кількість днів для перевірки. За замовчуванням 7.

        Returns:
            list: Список словників з інформацією про майбутні дні народження
                 Кожен словник містить:
                 - name: ім'я контакту
                 - congratulation_date: дата привітання
        """
        pass
```

## Record (record.py)

```python
class Record:
    """
    Клас для зберігання інформації про контакт.

    Attributes:
        name (Name): Ім'я контакту
        phones (list): Список телефонних номерів
        birthday (Birthday or None): Дата народження контакту
        email (Email or None): Email контакту
    """

    def add_phone(self, phone_number):
        """
        Додає номер телефону до контакту.

        Args:
            phone_number (str): Номер телефону для додавання

        Returns:
            str: Повідомлення про успішне додавання або помилку

        Raises:
            ValueError: Якщо формат номера неправильний
        """
        pass

    def edit_phone(self, old_phone, new_phone):
        """
        Змінює існуючий номер телефону.

        Args:
            old_phone (str): Старий номер телефону
            new_phone (str): Новий номер телефону

        Returns:
            str: Повідомлення про успішну зміну або помилку

        Raises:
            ValueError: Якщо старий номер не знайдено або новий має неправильний формат
        """
        pass
```

## NotesManager (note_manager.py)

```python
class NotesManager:
    """
    Клас для управління нотатками.

    Attributes:
        notes (list): Список об'єктів Note
    """

    def add_note(self, author, title, text, tags=None):
        """
        Створює та додає нову нотатку.

        Args:
            author (str): Автор нотатки
            title (str): Заголовок нотатки
            text (str): Текст нотатки
            tags (str, optional): Теги, розділені комами

        Returns:
            str: Повідомлення про успішне створення нотатки

        Raises:
            ValueError: Якщо обов'язкові поля порожні
        """
        pass

    def search_notes(self, search_term):
        """
        Пошук нотаток за ключовим словом.

        Пошук виконується по всіх полях нотатки: автор, заголовок, текст та теги.

        Args:
            search_term (str): Пошуковий запит

        Returns:
            str: Відформатований список знайдених нотаток

        Raises:
            ValueError: Якщо пошуковий запит порожній
            KeyError: Якщо нотатки не знайдено
        """
        pass
```

## Декоратори (functionality.py)

```python
def input_error(func):
    """
    Декоратор для обробки помилок у функціях роботи з контактами.

    Обробляє наступні винятки:
    - KeyError: Коли ключ не знайдено
    - ValueError: При неправильному форматі даних
    - IndexError: При неправильному індексі
    - Exception: Для всіх інших винятків

    Args:
        func (callable): Функція, що декорується

    Returns:
        callable: Обгорнута функція з обробкою помилок

    Example:
        @input_error
        def add_contact(args, book):
            name, phone = args
            # Додавання контакту
    """
    pass
```

## Функції роботи з даними (functionality.py)

```python
def save_data(book, filename="addressbook.pkl"):
    """
    Зберігає адресну книгу у файл.

    Args:
        book (AddressBook): Об'єкт адресної книги для збереження
        filename (str, optional): Ім'я файлу. За замовчуванням "addressbook.pkl"

    Raises:
        ValueError: При помилці збереження
    """
    pass

def load_data(filename="addressbook.pkl"):
    """
    Завантажує адресну книгу з файлу.

    Args:
        filename (str, optional): Ім'я файлу. За замовчуванням "addressbook.pkl"

    Returns:
        AddressBook: Завантажена адресна книга або нова, якщо файл не знайдено

    Raises:
        ValueError: При помилці завантаження
    """
    pass
```

## Валідація полів (check_classes)

### Email (email.py)

```python
class Email(Field):
    """
    Клас для валідації email адреси.

    Перевіряє відповідність email формату username@domain.tld

    Example:
        >>> email = Email("user@example.com")
        >>> email.check_email()
        True
    """

    def check_email(self):
        """
        Перевіряє коректність формату email.

        Returns:
            bool: True якщо email коректний, False в іншому випадку
        """
        pass
```

### Birthday (birthday.py)

```python
class Birthday(Field):
    """
    Клас для валідації та зберігання дати народження.

    Приймає дату у форматі DD.MM.YYYY

    Example:
        >>> birthday = Birthday("25.12.1990")
        >>> birthday.check_birthday()
        datetime.date(1990, 12, 25)
    """

    def check_birthday(self):
        """
        Перевіряє та перетворює рядок дати в об'єкт datetime.date.

        Returns:
            datetime.date: Об'єкт дати

        Raises:
            ValueError: Якщо формат дати неправильний
        """
        pass
```
