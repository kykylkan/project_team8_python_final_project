from tabulate import tabulate
from colorama import Fore, Back, Style
from check_classes.email import Email
from check_classes.name import Name
from check_classes.phone import Phone
from check_classes.birthday import Birthday


class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None


    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        if phone.check_phone():
            self.phones.append(phone)
            return f"✅   {Fore.GREEN}Phone {phone_number} added.{Style.RESET_ALL}"
        else:
            return f"⛔️   {Fore.RED}Failed to add phone due to invalid format.{Style.RESET_ALL}"


    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                


    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                if Phone(new_phone).check_phone():
                    self.phones[index] = Phone(new_phone)
            
                    return f"✅   {Fore.GREEN}Phone {old_phone} changed to {new_phone}{Style.RESET_ALL}"
            else:
                return f"⛔️   {Fore.RED}Phone {old_phone} not found. {new_phone}{Style.RESET_ALL}"
            

    def find_phone(self, phone_number):
        try:
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone.value
        except ValueError as e:
            print( f"⛔️   {Fore.RED}{e}.{Style.RESET_ALL}"
                )


    def add_email(self, email):
        emails = Email(email)
        if emails.check_email():
            self.email = emails  
            return f"✅   {Fore.GREEN}Email {email} added.{Style.RESET_ALL}"
        else:
            return f"⛔️   {Fore.RED}Invalid email format.{Style.RESET_ALL}"


           
    def add_birthday(self, birthday_value):
        birthday = Birthday(birthday_value).check_birthday()
        if birthday:
            self.birthday = birthday
            print(self.birthday)



    def __str__(self):
        phones_str = ", ".join(p.value for p in self.phones) if self.phones else "N/A"
        birthday_str = self.birthday.strftime('%d.%m.%Y') if self.birthday else "N/A"
        email_str = self.email.value if self.email else "N/A"

        return f"{self.name.value:<10} {phones_str:<30} {birthday_str:<15} {email_str:<30}"