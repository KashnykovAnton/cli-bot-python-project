from datetime import datetime
from colorama import Fore
from .field import Field

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(Fore.CYAN + "Invalid date format. Use DD.MM.YYYY")
