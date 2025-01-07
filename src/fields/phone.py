from colorama import Fore
from .field import Field

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value.isdigit() or len(value) != 10:
            raise ValueError(Fore.CYAN + "Phone number must be exactly 10 digits.")