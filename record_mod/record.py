
from email_mod.email import Email
from name_mod.name import Name
from check_phone.phone import Phone
from birthday_mod.birthday import Birthday


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
            print(f"Phone {phone_number} added.")
        else:
            print("Failed to add phone due to invalid format.")
            return None        

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                


    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                if Phone(new_phone).check_phone():
                    self.phones[index] = Phone(new_phone)
                    return f"Phone {old_phone} changed to {new_phone}"
            else:
                return f"Phone {old_phone} not found"
    

    def find_phone(self, phone_number):
        try:
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone.value
        except ValueError as e:
            print(e)


    def add_email(self, email):
        emails = Email(email)
        if emails.check_email():
            self.email = emails  # Зберігаємо об'єкт Email у self.email
            print(f"Email {email} added.")
        else:
            print("Invalid email format.")

           
    def add_birthday(self, birthday_value):
        birthday = Birthday(birthday_value)
        if birthday:
            self.birthday = birthday



    def __str__(self):
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        email_str = f", email: {self.email.value}" if self.email else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}{email_str}"
