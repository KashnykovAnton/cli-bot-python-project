from colorama import Fore
from src.record import Record
from src.utils import input_error
from src.handlers.contact_handler import ContactHandler
from src.handlers.contact_additional_handler import ContactAdditionalHandler

class ContactFullHandler:
    def __init__(self, address_book):
        self.address_book = address_book
        self.contact_handler = ContactHandler(address_book)
        self.contact_additional_handler = ContactAdditionalHandler(address_book)

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
            print(self.contact_handler.add_contact([name, phone]))
        else:
            print(Fore.YELLOW + "Phone not set. Skipping phone.")


        # Step 2: Add Email
        email = input(Fore.YELLOW + "Enter email (leave empty to skip): ").strip()
        if email:
            print(self.contact_additional_handler.add_email([name, email]))
        else:
            print(Fore.YELLOW + "Email not set. Skipping email.")

        # Step 3: Add Address
        address = input(Fore.YELLOW + "Enter address (leave empty to skip): ").strip()
        if address:
            print(self.contact_additional_handler.add_address([name, address]))
        else:
            print(Fore.YELLOW + "Address not set. Skipping address.")

        # Step 4: Add Birthday
        birthday = input(Fore.YELLOW + "Enter birthday (YYYY-MM-DD, leave empty to skip): ").strip()
        if birthday:
            print(self.contact_handler.add_birthday([name, birthday]))
        else:
            print(Fore.YELLOW + "Birthday not set. Skipping birthday.")

        print(Fore.GREEN + f"Contact '{name}' has been added/updated successfully.")

    @input_error
    def change_full_contact(self, args):
        print(Fore.CYAN + "Changing an existing contact. Follow the steps below:")
        
        # Step 1: Enter Old Name
        old_name = input(Fore.YELLOW + "Enter the current name of the contact: ").strip()
        record = self.address_book.find(old_name)
        if isinstance(record, str):
            record = None
        if not record:
            print(Fore.RED + f"Contact '{old_name}' not found.")
            return

        # Step 2: Change Name
        new_name = input(Fore.YELLOW + f"Enter new name for '{old_name}' (leave empty to skip): ").strip()
        if new_name:
            result = self.contact_handler.change_name([old_name, new_name])
            if result is not None:
                old_name = new_name
            print(result)
        else:
            print(Fore.YELLOW + "Name not changed. Skipping.")

        # Step 3: Change Phone
        phone_action = input(Fore.YELLOW + "Do you want to update phone numbers? (yes/no): ").strip().lower()
        if phone_action == "yes":
            old_phone = input(Fore.YELLOW + "Enter the phone number to replace (leave empty to skip): ").strip()
            new_phone = input(Fore.YELLOW + "Enter the new phone number (leave empty to skip): ").strip()
            if old_phone and new_phone:
                print(self.contact_handler.change_phone([old_name, old_phone, new_phone]))
            elif new_phone:
                print(self.contact_handler.add_contact([old_name, new_phone]))
            else:
                print(Fore.YELLOW + "Phone not changed. Skipping.")
        else:
            print(Fore.YELLOW + "Phone change skipped.")

        # Step 4: Change Email
        email = input(Fore.YELLOW + "Enter new email (leave empty to skip): ").strip()
        if email:
            print(self.contact_additional_handler.add_email([old_name, email]))
        else:
            print(Fore.YELLOW + "Email not changed. Skipping.")

        # Step 5: Change Address
        address = input(Fore.YELLOW + "Enter new address (leave empty to skip): ").strip()
        if address:
            print(self.contact_additional_handler.add_address([old_name, address]))
        else:
            print(Fore.YELLOW + "Address not changed. Skipping.")

        # Step 6: Change Birthday
        birthday = input(Fore.YELLOW + "Enter new birthday (YYYY-MM-DD, leave empty to skip): ").strip()
        if birthday:
            print(self.contact_handler.add_birthday([old_name, birthday]))
        else:
            print(Fore.YELLOW + "Birthday not changed. Skipping.")

        print(Fore.GREEN + f"Contact '{old_name}' has been updated successfully.")
