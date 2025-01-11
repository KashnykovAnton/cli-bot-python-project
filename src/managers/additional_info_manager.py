from colorama import Fore
from src.record import Record
from src.utils.decorators import input_error

class AdditionalInfoManager:
    def __init__(self, address_book):
        self.address_book = address_book

    @input_error
    def add_email(self, args):
        name, email = args
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.add_email(email)
        return Fore.RED + "Contact not found."

    @input_error
    def show_email(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.show_email()
        return Fore.RED + "Contact not found."

    @input_error
    def remove_email(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.remove_email()
        return Fore.RED + "Contact not found."

    @input_error
    def add_address(self, args):
        name = args[0]
        address = " ".join(args[1:])
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.add_address(address)
        return Fore.RED + "Contact not found."

    @input_error
    def show_address(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.show_address()
        return Fore.RED + "Contact not found."

    @input_error
    def remove_address(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.remove_address()
        return Fore.RED + "Contact not found."
