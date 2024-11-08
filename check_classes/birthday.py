from field_saves.field import Field
from datetime import datetime
import re
from colorama import Fore, Style


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    def check_birthday(self):
        pattern = r"\d{2}\.\d{2}\.\d{4}"
        if re.match(pattern, str(self.value)):
            datetime_object = datetime.strptime(self.value, "%d.%m.%Y").date()
            return datetime_object
        else:
            raise ValueError(
                f"⛔️   {Fore.RED}Invalid date format. Use DD.MM.YYYY {Style.RESET_ALL}"
            )
