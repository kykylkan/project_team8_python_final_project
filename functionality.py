from email_mod.email import Email
from record_mod.record import Record
from birthday_mod.birthday import Birthday
from book.address_book import AddressBook
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
            return e
        except ValueError as e:
            return e
        except IndexError as e:
            return e
        except Exception as e:
            return f'An unexpected error occurred: {e}. Please try again.'
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def remove_record(args, book: AddressBook):
    name, *_ = args 
    record = book.find(name)
    if record:
        book.delete(name)
        return f'Contact with name "{name}" is deleted'

@input_error
def change_number(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return record.edit_phone(old_phone, new_phone)


@input_error
def show_phones(name, book: AddressBook):
    record = book.find(name)
    if record:
        phones = [phone.value for phone in record.phones]
        return f'numbers of name {name} is {phones}'
    
@input_error
def remove_phone(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    print(record)
    if record:
        for el in record.phones:
            if el.value == phone:
                record.remove_phone(phone)
                return f'phone "{phone}" is delete'
            else: 
                return f'phone "{phone}" is not defined'
        
        


@input_error
def show_all(book: AddressBook):
    result = [f"{record}" for _, record in book.data.items()]

    if result:
        return result
    else:
        return "Book is empty"

@input_error
def add_email(args, book: AddressBook):
    name, email = args
    record = book.find(name)
    if Email(email):
        record.add_email(email)
        return f'{email} added for name {name}'



@input_error
def add_birthday(args, book: AddressBook):
    name, birthday_date = args
    record = book.find(name)
    if Birthday(birthday_date):
        record.add_birthday(birthday_date)
        return f'{birthday_date} added for name {name}'

@input_error
def show_birthday(name, book: AddressBook):
    record = book.find(name)
    if record:
        birthday = record.birthday.value
        return f'Birthday of {name} is {birthday}'
    return f'Birthday of {name} is not found'    

@input_error
def show_reminder(book):
    if book.get_upcoming_birthdays():
        return book.get_upcoming_birthdays()
    return 'No reminders for this week'

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
