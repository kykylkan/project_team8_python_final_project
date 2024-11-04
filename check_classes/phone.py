from field_saves.field import Field

class Phone(Field):
    def check_phone(self):
        if len(self.value) == 10 and self.value.isdigit():
            return True 
        else:
            return False
             