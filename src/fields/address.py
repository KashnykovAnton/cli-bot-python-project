from colorama import Fore
from .field import Field

class Address(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Address cannot be empty.")
        super().__init__(value)
