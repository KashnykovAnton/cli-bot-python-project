from colorama import Fore
from .field import Field

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value or not value.strip():
            raise ValueError(Fore.CYAN + "Name cannot be empty.")