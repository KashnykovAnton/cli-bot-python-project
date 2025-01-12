from colorama import Fore
from .fields import *
from src.utils import input_error

class ContactRecord:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            raise ValueError(Fore.RED + f"An error occurred while adding name: {str(e)}")
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    @input_error
    def add_phone(self, phone):
        existing_phone = list(filter(lambda p: p.value == phone, self.phones))
        if existing_phone:
            return Fore.CYAN + f"Phone number {phone} already exists."
        self.phones.append(phone)
        print(Fore.GREEN + f"Phone number {phone} added successfully.")

    @input_error
    def remove_phone(self, phone):
        original_length = len(self.phones)
        self.phones = list(filter(lambda p: p.value != phone, self.phones))
        if len(self.phones) < original_length:
            return Fore.GREEN + f"Phone number {phone} was successfully removed."
        return Fore.CYAN + f"Phone number {phone} not found."

    @input_error
    def edit_phone(self, old_phone, new_phone):
        if old_phone == new_phone:
            return Fore.YELLOW + "New phone number should be different from the old one."
        
        if new_phone in [p.value for p in self.phones]:
            return Fore.YELLOW + "New phone number is already in the list."
        
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[idx] = Phone(new_phone)
                return Fore.GREEN + f"Phone number {old_phone} successfully changed to {new_phone}."
        
        return Fore.RED + f"Phone number {old_phone} not found."

    @input_error
    def edit_name(self, old_name, new_name):
        self.name = Name(new_name)
        return Fore.GREEN + f"Contact name {old_name} successfully changed to {new_name}."

    @input_error
    def show_phones(self):
        phones = "; ".join(p.value for p in self.phones)
        return Fore.GREEN + f"Contact name: {self.name.value}, phones: {phones}"
    
    @input_error
    def add_birthday(self, birthday):
        if self.birthday is not None:
            self.birthday = birthday
            return Fore.YELLOW + f"Birthday updated to {birthday} successfully."
        else:
            self.birthday = birthday
            return Fore.GREEN + f"Birthday {birthday} added successfully."
    
    @input_error
    def show_birthday(self):
        if self.birthday:
            return Fore.GREEN + f"Contact name: {self.name}, birthday: {self.birthday}"
        return Fore.YELLOW + f"Birthday for {self.name}: not set"
        

    @input_error
    def remove_birthday(self):
        if self.birthday:
            self.birthday = None
            return Fore.GREEN + f"Birthday for {self.name} successfully deleted."
        return Fore.YELLOW + f"Birthday for {self.name}: not set"

    @input_error
    def add_email(self, email):
        if self.email is not None:
            self.email = Email(email)
            return Fore.YELLOW + f"Email for {self.name} updated: {self.email}"
        else:
            self.email = Email(email)
            return Fore.GREEN + f"Email {email} added successfully."

    @input_error
    def show_email(self):
        if self.email:
            return Fore.GREEN + f"Contact name: {self.name.value}, email: {self.email.value}"
        return Fore.YELLOW + f"Email for {self.name}: not set"

    @input_error
    def remove_email(self):
        if self.email:
            self.email = None
            return Fore.GREEN + f"Email for {self.name.value} successfully deleted."
        return Fore.YELLOW + f"Email for {self.name.value}: not set"
    
    @input_error
    def add_address(self, address):
        if self.address is not None:
            self.address = Address(address)
            return Fore.YELLOW + f"Address for {self.name.value} updated: {self.address.value}"
        else:
            self.address = Address(address)
            return Fore.GREEN + f"Address '{address}' added successfully."

    @input_error
    def show_address(self):
        if self.address:
            return Fore.GREEN + f"Contact name: {self.name.value}, address: {self.address.value}"
        return Fore.YELLOW + f"Address for {self.name.value}: not set"
    
    @input_error
    def remove_address(self):
        if self.address:
            self.address = None
            return Fore.GREEN + f"Address for {self.name.value} successfully deleted."
        return Fore.YELLOW + f"Address for {self.name.value}: not set"

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = self.birthday.value if self.birthday else "not set"
        email = self.email.value if self.email else "not set"
        address = self.address.value if self.address else "not set"
        return Fore.RESET + f"Contact name: {self.name.value}, phones: {phones}, email: {email}, address: {address}, birthday: {birthday}"
    