from field_saves.field import Field
import re


class Email(Field):
    
    def __init__(self, value):
        super().__init__(value)

    def check_email(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        res = re.match(pattern, self.value) 
        if res is None:
            return False        
        else:
            return True