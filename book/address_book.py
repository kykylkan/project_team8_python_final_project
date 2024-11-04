from datetime import datetime, date, timedelta
from collections import UserDict



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        print(f'Contact {record.name} added' )


    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f'Contact with name "{name}" not found')
            return None


    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
        else:
            print(f'Contact with name "{name}" not found')


    def get_upcoming_birthdays(self):
        """
        Returns a list of contacts with birthdays in the next 7 days.
        Returns:
            list of dict:
        """
        today = datetime.today().date()
        reminder = []

        for contact in self.data.values():
            birthday = contact.birthday
            if birthday != None:
                birthday_this_year = date(today.year, birthday.value.month, birthday.value.day)
                if birthday_this_year < today:
                    birthday_this_year = date(today.year + 1, birthday.value.month, birthday.value.day)
                days_until_birthday = (birthday_this_year - today).days

                if days_until_birthday <= 7:
                    if(birthday_this_year.weekday() == 5):
                        congratulation_date = birthday_this_year + timedelta(days=2)
                    elif(birthday_this_year.weekday() == 6):
                        congratulation_date = birthday_this_year + timedelta(days=1)
                    else:
                        congratulation_date = birthday_this_year

                    congratulation_date_str = datetime.strftime(congratulation_date, '%d.%m.%Y')
                    reminder.append({'name': contact.name.value, 'congratulation_date': congratulation_date_str}) 

        return reminder