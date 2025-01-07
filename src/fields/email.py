from colorama import Fore
from .field import Field

class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_email(value)

    def validate_email(self, email):
        if "@" not in email:
            raise ValueError(Fore.CYAN + f"Invalid email address: {email}")
