from datetime import datetime, date, timedelta
from collections import UserDict
from colorama import Fore, Style



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        print(f"✅   {Fore.GREEN}Contact {record.name} added.{Style.RESET_ALL}")


    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f"⛔️   {Fore.RED}Contact with name {name} not found.{Style.RESET_ALL}")
            return None


    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
        else:
            print(f"⛔️   {Fore.RED}Contact with name {name}not found.{Style.RESET_ALL}")




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
                birthday_this_year = date(today.year, birthday.month, birthday.day)
                if birthday_this_year < today:
                    birthday_this_year = date(today.year + 1, birthday.month, birthday.day)
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