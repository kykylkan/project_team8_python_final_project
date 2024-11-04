import re
from field_saves.field import Field


class Email(Field):
    def __init__(self, value):
          super().__init__(value)

    def check_email(self):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            res = re.match(pattern, self.value) is not None
            return res
    



# print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")

