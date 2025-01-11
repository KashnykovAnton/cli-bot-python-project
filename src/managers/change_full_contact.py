from colorama import Fore
from .additional_info_manager import AdditionalInfoManager
from .contacts_manager import ContactsManager
from src.utils.decorators import input_error

class ChangeFullContact:
    def __init__(self, address_book):
        self.address_book = address_book
        self.contacts_manager = ContactsManager(self.address_book)
        self.additional_info_manager = AdditionalInfoManager(self.address_book)

    @input_error
    def change_full_contact(self):
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
            result = self.contacts_manager.change_name([old_name, new_name])
            if result is not None and not isinstance(result, str):
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
                print(self.contacts_manager.change_phone([old_name, old_phone, new_phone]))
            elif new_phone:
                print(self.contacts_manager.add_contact([old_name, new_phone]))
            else:
                print(Fore.YELLOW + "Phone not changed. Skipping.")
        else:
            print(Fore.YELLOW + "Phone change skipped.")

        # Step 4: Change Email
        email = input(Fore.YELLOW + "Enter new email (leave empty to skip): ").strip()
        if email:
            print(self.additional_info_manager.add_email([old_name, email]))
        else:
            print(Fore.YELLOW + "Email not changed. Skipping.")

        # Step 5: Change Address
        address = input(Fore.YELLOW + "Enter new address (leave empty to skip): ").strip()
        if address:
            print(self.additional_info_manager.add_address([old_name, address]))
        else:
            print(Fore.YELLOW + "Address not changed. Skipping.")

        # Step 6: Change Birthday
        birthday = input(Fore.YELLOW + "Enter new birthday (YYYY-MM-DD, leave empty to skip): ").strip()
        if birthday:
            print(self.contacts_manager.add_birthday([old_name, birthday]))
        else:
            print(Fore.YELLOW + "Birthday not changed. Skipping.")

        print(Fore.GREEN + f"Contact '{old_name}' has been updated successfully.")
