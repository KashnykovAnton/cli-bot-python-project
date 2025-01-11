from colorama import Fore
from .additional_info_manager import AdditionalInfoManager
from .contacts_manager import ContactsManager
from src.utils.decorators import input_error

class AddFullContact:
    def __init__(self, address_book):
        self.address_book = address_book
        self.contacts_manager = ContactsManager(self.address_book)
        self.additional_info_manager = AdditionalInfoManager(self.address_book)

    @input_error
    def add_full_contact(self):
        print(Fore.CYAN + "Adding a new contact. Follow the steps below:")
        
        # Step 1: Add Name and Phone
        name = input(Fore.YELLOW + "Enter contact name: ").strip()
        if not name:
            print(Fore.RED + "Name is required. Cancelling operation.")
            return
        record = self.address_book.find(name)
        if isinstance(record, str):
            record = None
        if record:
            print(Fore.YELLOW + f"Contact '{name}' already exists. Updating contact.")
        phone = input(Fore.YELLOW + "Enter phone number: ").strip()
        if phone:
            print(self.contacts_manager.add_contact([name, phone]))
        else:
            print(Fore.YELLOW + "Phone not set. Skipping phone.")


        # Step 2: Add Email
        email = input(Fore.YELLOW + "Enter email (leave empty to skip): ").strip()
        if email:
            print(self.additional_info_manager.add_email([name, email]))
        else:
            print(Fore.YELLOW + "Email not set. Skipping email.")

        # Step 3: Add Address
        address = input(Fore.YELLOW + "Enter address (leave empty to skip): ").strip()
        if address:
            print(self.additional_info_manager.add_address([name, address]))
        else:
            print(Fore.YELLOW + "Address not set. Skipping address.")

        # Step 4: Add Birthday
        birthday = input(Fore.YELLOW + "Enter birthday (YYYY-MM-DD, leave empty to skip): ").strip()
        if birthday:
            print(self.contacts_manager.add_birthday([name, birthday]))
        else:
            print(Fore.YELLOW + "Birthday not set. Skipping birthday.")

        print(Fore.GREEN + f"Contact '{name}' has been added successfully.")
