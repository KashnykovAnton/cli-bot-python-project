from colorama import Fore
from src.fields import *
from src.record import Record
from src.utils.decorators import input_error

class ContactsManager:
    def __init__(self, address_book):
        self.address_book = address_book

    @input_error
    def add_contact(self, args):
        name, phone = args
        contact_phone = Phone(phone)
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        message = "updated"
        if record is None:
            record = Record(name)
            self.address_book.add_record(record)
            message = "added"
        if contact_phone:
            record.add_phone(contact_phone)    
        return Fore.GREEN + f"Contact {name} {message} successfully."

    @input_error
    def change_phone(self, args):
        name, old_phone, new_phone = args
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.edit_phone(old_phone, new_phone)
        return Fore.RED + "Contact not found."

    @input_error
    def change_name(self, args):
        old_name, new_name = args
        if old_name == new_name:
            return Fore.YELLOW + "New name should be different from the old one."
        if new_name in self.address_book:
            return Fore.RED + f"A contact with the name '{new_name}' already exists."
        
        record = self.address_book.find(old_name)
        if isinstance(record, str):
            record = None
        if record:
            # del self.address_book[old_name]
            result = record.edit_name(old_name, new_name)
            self.address_book[new_name] = self.address_book.pop(old_name)
            # self.address_book[new_name] = record
            return result
        return Fore.RED + "Contact not found."
        

    @input_error
    def show_phone(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.show_phones()
        return Fore.RED + "Contact not found."

    def show_all(self, args=None):
        if self.address_book:
            result = Fore.CYAN + "All contacts:\n"
            for record in self.address_book.values():
                result += Fore.YELLOW + str(record) + "\n"
            return result.strip()
        return Fore.RED + "No contacts found."

    @input_error
    def add_birthday(self, args):
        name, birthday = args
        contact_birthday = Birthday(birthday)
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.add_birthday(contact_birthday)
        return Fore.RED + "Contact not found."

    @input_error
    def show_contact_birthday(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.show_birthday()
        return Fore.RED + "Contact not found."

    @input_error
    def remove_birthday(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.remove_birthday()
        return Fore.RED + "Contact not found."

    @input_error
    def show_birthdays(self, args):
        days = int(args[0]) if args else 7
        upcoming_birthdays = self.address_book.get_upcoming_birthdays(days)
        if upcoming_birthdays:
            result = Fore.CYAN + f"Upcoming birthdays in {days} days:\n"
            for item in upcoming_birthdays:
                result += Fore.YELLOW + f"{item['name']}: {item['congratulation_date']}\n"
            return result.strip()
        return Fore.RED + "No upcoming birthdays."
    
    @input_error
    def remove_contact(self, args):
        name = args[0]
        return self.address_book.delete(name)
    
    @input_error
    def remove_phone(self, args):
        name, phone = args
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            return record.remove_phone(phone)
        return Fore.RED + "Contact not found."
    

    @input_error
    def find_contact(self, args):
        name = args[0]
        lower_name = name.lower()
        results = [record for key, record in self.address_book.items() if lower_name in key.lower()]

        if not results:
            return Fore.YELLOW + f"No contacts found with name containing '{name}'."

        found_contacts = "\n".join(str(record) for record in results)
        return Fore.GREEN + f"Contacts matching '{name}':\n{found_contacts}"
    