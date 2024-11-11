# Техническая документация Assistant Bot

## AddressBook (address_book.py)

```python
class AddressBook(UserDict):
    """
    Класс для управления адресной книгой.

    Наследуется от UserDict для реализации словаря контактов.

    Attributes:
        data (dict): Словарь для хранения записей, где ключ - имя контакта
    """

    def add_record(self, record):
        """
        Добавляет новую запись в адресную книгу.

        Args:
            record (Record): Объект записи для добавления

        Returns:
            str: Сообщение об успешном добавлении контакта
        """
        pass

    def find(self, name):
        """
        Поиск записи по имени контакта.

        Args:
            name (str): Имя контакта для поиска

        Returns:
            Record or None: Найденная запись или None, если запись не найдена
        """
        pass

    def get_upcoming_birthdays(self, days=7):
        """
        Возвращает список контактов, у которых день рождения в ближайшие дни.

        Args:
            days (int, optional): Количество дней для проверки. По умолчанию 7.

        Returns:
            list: Список словарей с информацией о предстоящих днях рождения
                 Каждый словарь содержит:
                 - name: имя контакта
                 - congratulation_date: дата поздравления
        """
        pass
```

## Record (record.py)

```python
class Record:
    """
    Класс для хранения информации о контакте.

    Attributes:
        name (Name): Имя контакта
        phones (list): Список телефонных номеров
        birthday (Birthday or None): Дата рождения контакта
        email (Email or None): Email контакта
    """

    def add_phone(self, phone_number):
        """
        Добавляет номер телефона к контакту.

        Args:
            phone_number (str): Номер телефона для добавления

        Returns:
            str: Сообщение об успешном добавлении или ошибке

        Raises:
            ValueError: Если формат номера неверный
        """
        pass

    def edit_phone(self, old_phone, new_phone):
        """
        Изменяет существующий номер телефона.

        Args:
            old_phone (str): Старый номер телефона
            new_phone (str): Новый номер телефона

        Returns:
            str: Сообщение об успешном изменении или ошибке

        Raises:
            ValueError: Если старый номер не найден или новый имеет неверный формат
        """
        pass
```

## NotesManager (note_manager.py)

```python
class NotesManager:
    """
    Класс для управления заметками.

    Attributes:
        notes (list): Список объектов Note
    """

    def add_note(self, author, title, text, tags=None):
        """
        Создает и добавляет новую заметку.

        Args:
            author (str): Автор заметки
            title (str): Заголовок заметки
            text (str): Текст заметки
            tags (str, optional): Теги, разделенные запятыми

        Returns:
            str: Сообщение об успешном создании заметки

        Raises:
            ValueError: Если обязательные поля пустые
        """
        pass

    def search_notes(self, search_term):
        """
        Поиск заметок по ключевому слову.

        Поиск выполняется по всем полям заметки: автор, заголовок, текст и теги.

        Args:
            search_term (str): Поисковый запрос

        Returns:
            str: Отформатированный список найденных заметок

        Raises:
            ValueError: Если поисковый запрос пустой
            KeyError: Если заметки не найдены
        """
        pass
```

## Декораторы (functionality.py)

```python
def input_error(func):
    """
    Декоратор для обработки ошибок в функциях работы с контактами.

    Обрабатывает следующие исключения:
    - KeyError: Когда ключ не найден
    - ValueError: При неверном формате данных
    - IndexError: При неверном индексе
    - Exception: Для всех остальных исключений

    Args:
        func (callable): Декорируемая функция

    Returns:
        callable: Обернутая функция с обработкой ошибок

    Example:
        @input_error
        def add_contact(args, book):
            name, phone = args
            # Добавление контакта
    """
    pass
```

## Функции работы с данными (functionality.py)

```python
def save_data(book, filename="addressbook.pkl"):
    """
    Сохраняет адресную книгу в файл.

    Args:
        book (AddressBook): Объект адресной книги для сохранения
        filename (str, optional): Имя файла. По умолчанию "addressbook.pkl"

    Raises:
        ValueError: При ошибке сохранения
    """
    pass

def load_data(filename="addressbook.pkl"):
    """
    Загружает адресную книгу из файла.

    Args:
        filename (str, optional): Имя файла. По умолчанию "addressbook.pkl"

    Returns:
        AddressBook: Загруженная адресная книга или новая, если файл не найден

    Raises:
        ValueError: При ошибке загрузки
    """
    pass
```

## Валидация полей (check_classes)

### Email (email.py)

```python
class Email(Field):
    """
    Класс для валидации email адреса.

    Проверяет соответствие email формату username@domain.tld

    Example:
        >>> email = Email("user@example.com")
        >>> email.check_email()
        True
    """

    def check_email(self):
        """
        Проверяет корректность формата email.

        Returns:
            bool: True если email корректный, False в противном случае
        """
        pass
```

### Birthday (birthday.py)

```python
class Birthday(Field):
    """
    Класс для валидации и хранения даты рождения.

    Принимает дату в формате DD.MM.YYYY

    Example:
        >>> birthday = Birthday("25.12.1990")
        >>> birthday.check_birthday()
        datetime.date(1990, 12, 25)
    """

    def check_birthday(self):
        """
        Проверяет и преобразует строку даты в объект datetime.date.

        Returns:
            datetime.date: Объект даты

        Raises:
            ValueError: Если формат даты неверный
        """
        pass
```
