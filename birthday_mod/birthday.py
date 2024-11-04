from field_saves.field import Field
from datetime import datetime
import re


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        pattern = r'\d{2}.\d{2}.\d{4}'
        try:
            if re.search(pattern, value):
                datetime_object = datetime.strptime(value, '%d.%m.%Y').date()
                self.value = datetime_object
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")