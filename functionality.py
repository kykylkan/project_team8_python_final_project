from check_classes.email import Email
from record_mod.record import Record
from check_classes.birthday import Birthday
from book_mod.address_book import AddressBook
from colorama import Fore, Back, Style

import pickle

def input_error(func):
    '''
    Decorator for handling errors in command processing functions.
    Parameters:
    func (function): The function to which the decorator is applied.

    Returns:
    function: Internal function that handles errors
    '''


    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"⛔️   {Fore.RED}{e}.{Style.RESET_ALL}"
        except ValueError as e:
            return f"⛔️   {Fore.RED}{e}.{Style.RESET_ALL}"
        except IndexError as e:
            return f"⛔️   {Fore.RED}{e}.{Style.RESET_ALL}"
        except Exception as e:
            return f"⛔️   {Fore.RED}An unexpected error occurred: {e}. Please try again.{Style.RESET_ALL}"
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

 
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = f"✅   {Fore.GREEN}Contact updated.{Style.RESET_ALL}"
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"✅   {Fore.GREEN}Contact added.{Style.RESET_ALL}"
    if phone:
        record.add_phone(phone)
    return message


@input_error
def remove_record(args, book: AddressBook):
    name, *_ = args 
    record = book.find(name)
    if record:
        book.delete(name)
        return f'✅   {Fore.GREEN}Contact with name "{name}" is deleted.{Style.RESET_ALL}'

@input_error
def change_number(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return f"⛔️   {Fore.RED}Contact with name {name}not found.{Style.RESET_ALL}"
    return record.edit_phone(old_phone, new_phone)


@input_error
def show_phones(name, book: AddressBook):
    record = book.find(name)
    if record:
        phones = [phone.value for phone in record.phones]
        return f'✅   {Fore.GREEN}numbers of name {name} is {phones}.{Style.RESET_ALL}'
    
@input_error
def remove_phone(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    print(record)
    if record:
        for el in record.phones:
            if el.value == phone:
                record.remove_phone(phone)
                return f'✅   {Fore.GREEN}phone "{phone}" is delete.{Style.RESET_ALL}'
            else: 
                return f"⛔️   {Fore.RED}phone {phone} is not defined.{Style.RESET_ALL}"


@input_error
def show_all(book: AddressBook):
    result = [f"{record}" for _, record in book.data.items()]

    if result:
        return result
    else:
        return f"⛔️   {Fore.RED}Book is empty.{Style.RESET_ALL}"

@input_error
def add_email(args, book: AddressBook):
    name, email = args
    record = book.find(name)
    if Email(email):
        record.add_email(email)
        return f'✅   {Fore.GREEN}{email} added for name {name}.{Style.RESET_ALL}'


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday_date = args
    record = book.find(name)
    if Birthday(birthday_date):
        record.add_birthday(birthday_date)
        return f'✅   {Fore.GREEN}{birthday_date} added for name {name}.{Style.RESET_ALL}'


@input_error
def show_birthday(name, book: AddressBook):
    record = book.find(name)
    if record:
        birthday = record.birthday.value
        return f'✅   {Fore.GREEN}Birthday of {name} is {birthday}.{Style.RESET_ALL}'
    return f"⛔️   {Fore.RED}Birthday of {name} is not found.{Style.RESET_ALL}"
   

@input_error
def show_reminder(book):
    if book.get_upcoming_birthdays():
        return book.get_upcoming_birthdays()
    return f"⛔️   {Fore.RED}No reminders for this week.{Style.RESET_ALL}"


@input_error
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

@input_error
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  
