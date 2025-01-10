from colorama import Fore, Style, init
from datetime import datetime
from collections import UserDict
from .address_book import AddressBook
from .record import Record
from .command import Command
from .completer import Prompt
from .fields import *
from .notes_book import NotesBook
from src.utils import input_error

init(autoreset=True)

class Bot:
    def __init__(self):
        self.address_book = AddressBook.load()
        self.notes_book = NotesBook.load()
        self.prompt = Prompt()

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

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
            del self.address_book[old_name]
            result = record.edit_name(old_name, new_name)
            self.address_book[new_name] = record
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
    def find_contact(self, args):
        name = args[0].lower()
        results = [record for key, record in self.address_book.items() if name in key.lower()]

        if not results:
            return Fore.YELLOW + f"No contacts found with name containing '{name}'."

        found_contacts = "\n".join(str(record) for record in results)
        return Fore.GREEN + f"Contacts matching '{name}':\n{found_contacts}"
    
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
            print(self.add_contact([name, phone]))
        else:
            print(Fore.YELLOW + "Phone not set. Skipping phone.")


        # Step 2: Add Email
        email = input(Fore.YELLOW + "Enter email (leave empty to skip): ").strip()
        if email:
            print(self.add_email([name, email]))
        else:
            print(Fore.YELLOW + "Email not set. Skipping email.")

        # Step 3: Add Address
        address = input(Fore.YELLOW + "Enter address (leave empty to skip): ").strip()
        if address:
            print(self.add_address([name, address]))
        else:
            print(Fore.YELLOW + "Address not set. Skipping address.")

        # Step 4: Add Birthday
        birthday = input(Fore.YELLOW + "Enter birthday (YYYY-MM-DD, leave empty to skip): ").strip()
        if birthday:
            print(self.add_birthday([name, birthday]))
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
            result = self.change_name([old_name, new_name])
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
                print(self.change_phone([old_name, old_phone, new_phone]))
            elif new_phone:
                print(self.add_contact([old_name, new_phone]))
            else:
                print(Fore.YELLOW + "Phone not changed. Skipping.")
        else:
            print(Fore.YELLOW + "Phone change skipped.")

        # Step 4: Change Email
        email = input(Fore.YELLOW + "Enter new email (leave empty to skip): ").strip()
        if email:
            print(self.add_email([old_name, email]))
        else:
            print(Fore.YELLOW + "Email not changed. Skipping.")

        # Step 5: Change Address
        address = input(Fore.YELLOW + "Enter new address (leave empty to skip): ").strip()
        if address:
            print(self.add_address([old_name, address]))
        else:
            print(Fore.YELLOW + "Address not changed. Skipping.")

        # Step 6: Change Birthday
        birthday = input(Fore.YELLOW + "Enter new birthday (YYYY-MM-DD, leave empty to skip): ").strip()
        if birthday:
            print(self.add_birthday([old_name, birthday]))
        else:
            print(Fore.YELLOW + "Birthday not changed. Skipping.")

        print(Fore.GREEN + f"Contact '{old_name}' has been updated successfully.")

    @input_error
    def add_note(self, args):
        title, content = args[0], " ".join(args[1:])
        return self.notes_book.add_note(title, content)

    @input_error
    def find_note(self, args):
        title = args[0]
        return self.notes_book.find_note(title)
    
    @input_error
    def sort_notes(self, by="title"):
        if by == "title":
            self.notes = sorted(self.notes, key=lambda note: note['title'].lower())
        elif by == "date":
            self.notes = sorted(self.notes, key=lambda note: note['date'])

    @input_error
    def edit_note(self, args):
        title, new_content = args[0], " ".join(args[1:])
        return self.notes_book.edit_note(title, new_content)

    @input_error
    def delete_note(self, args):
        title = args[0]
        return self.notes_book.delete_note(title)

    @input_error
    def show_all_notes(self, args=None):
        return self.notes_book.show_all_notes()

    
    def format_command(self, command, description):
        command_colored = Fore.GREEN + Style.BRIGHT + command
        description_colored = Fore.WHITE + description
        return f"  {command_colored}: {description_colored}\n"
    
    def show_help(self):
        help_text = Fore.CYAN + Style.BRIGHT + "Available commands:\n"
        
        help_text += Fore.YELLOW + Style.BRIGHT + "\nGeneral Commands:\n"
        help_text += self.format_command("hello", "Greet the bot.")
        help_text += self.format_command("exit, close", "Exit the bot.")
        help_text += self.format_command("help", "Show this help text.")
        
        help_text += Fore.YELLOW + Style.BRIGHT + "\nContact Management:\n"
        help_text += self.format_command("add-contact", "Add a new contact with all fields interactively.")
        help_text += self.format_command("change-contact", "Update all fields of an existing contact interactively.")
        help_text += self.format_command("find-contact <name>", "Find contacts by name.")
        help_text += self.format_command("remove-contact <name>", "Remove a contact from the address book.")
        help_text += self.format_command("all-contacts", "Show all contacts in the address book.")
        help_text += self.format_command("add-phone <name> <phone>", "Add a new phone number to a contact.")
        help_text += self.format_command("change-phone <name> <old_phone> <new_phone>", "Change a contact's phone number.")
        help_text += self.format_command("show-phone <name>", "Show phone numbers of a contact.")
        help_text += self.format_command("remove-phone <name> <phone>", "Remove a specific phone number from a contact.")
        help_text += self.format_command("change-name <old_name> <new_name>", "Change a contact's name.")
        help_text += self.format_command("add-birthday <name> <birthday>", "Add a birthday to a contact (format: YYYY-MM-DD).")
        help_text += self.format_command("show-birthday <name>", "Show a contact's birthday.")
        help_text += self.format_command("birthdays [days]", "Show contacts with upcoming birthdays in the next [days] days (default: 7).")

        help_text += Fore.YELLOW + Style.BRIGHT + "\nAdditional Info:\n"
        help_text += self.format_command("add-email <name> <email>", "Add an email to a contact.")
        help_text += self.format_command("show-email <name>", "Show the email of a contact.")
        help_text += self.format_command("add-address <name> <address>", "Add an address to a contact.")
        help_text += self.format_command("show-address <name>", "Show the address of a contact.")
        
        help_text += Fore.YELLOW + Style.BRIGHT + "\nNotes Management:\n"
        help_text += self.format_command("add-note <title> <content>", "Add a new note.")
        help_text += self.format_command("find-note <title>", "Find a note by title.")
        help_text += self.format_command("edit-note <title> <new_content>", "Edit an existing note.")
        help_text += self.format_command("delete-note <title>", "Delete a note by title.")
        help_text += self.format_command("all-notes", "Show all notes.")

        return help_text

    def run(self):
        print(Fore.GREEN + "Welcome to the assistant bot!")
        
        while True:
            message_text = "Enter a command: "
            styled_message = {message_text: "#0000FF"}
            user_input = self.prompt.styled_prompt(styled_message, Command.command_list()).strip()

            user_input_parts = user_input.split()
            command = user_input_parts[0]
            args = user_input_parts[1:]

            if user_input:
                try:
                    cmd_enum = Command(command)
                except KeyError:
                    print(Fore.RED + "Invalid command.")
                    continue

            if cmd_enum in {Command.EXIT, Command.CLOSE}:
                print(Fore.GREEN + "Good bye!")
                self.address_book.save()
                self.notes_book.save()
                break
            elif cmd_enum == Command.HELLO:
                print(Fore.GREEN + "How can I help you?")
            elif cmd_enum == Command.ADD_CONTACT:
                self.add_full_contact()
            elif cmd_enum == Command.CHANGE_CONTACT:
                self.change_full_contact(args)
            elif cmd_enum == Command.ADD_PHONE:
                if args:
                    print(self.add_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and phone number after 'add-phone'.")
            elif cmd_enum == Command.CHANGE_PHONE:
                if len(args) == 3:
                    print(self.change_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name, old phone number and new phone number after 'change-phone'.")
            elif cmd_enum == Command.CHANGE_NAME:
                if len(args) == 2:
                    print(self.change_name(args))
                else:
                    print(Fore.YELLOW + "Please provide the old contact name and new contact name after 'change-name'.")
            elif cmd_enum == Command.SHOW_PHONE:
                if args:
                    print(self.show_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-phone'.")
            elif cmd_enum == Command.REMOVE_PHONE:
                if len(args) == 2:
                    print(self.remove_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and phone number after 'remove-phone'.")
            elif cmd_enum == Command.REMOVE_CONTACT:
                if args:
                    print(self.remove_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-contact'.")
            elif cmd_enum == Command.ALL_CONTACTS:
                print(self.show_all())
            elif cmd_enum == Command.ADD_BIRTHDAY:
                if len(args) == 2:
                    print(self.add_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and birthday (DD.MM.YYYY) after 'add-birthday'.")
            elif cmd_enum == Command.SHOW_BIRTHDAY:
                if args:
                    print(self.show_contact_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-birthday'.")
            elif cmd_enum == Command.BIRTHDAYS:
                print(self.show_birthdays(args))
            elif cmd_enum == Command.HELP:
                print(self.show_help())
            elif cmd_enum == Command.ADD_EMAIL:
                if len(args) == 2:
                    print(self.add_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and email after 'add-email'.")
            elif cmd_enum == Command.SHOW_EMAIL:
                if args:
                    print(self.show_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-email'.")
            elif cmd_enum == Command.ADD_ADDRESS:
                if len(args) > 1:
                    print(self.add_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and address after 'add-address'.")
            elif cmd_enum == Command.SHOW_ADDRESS:
                if args:
                    print(self.show_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-address'.")
            elif cmd_enum == Command.FIND_CONTACT:
                if args:
                    print(self.find_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'find-contact'.")
            elif cmd_enum == Command.ADD_NOTE:
                if len(args) > 1:
                    print(self.add_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title and content after 'add-note'.")
            elif cmd_enum == Command.FIND_NOTE:
                if args:
                    print(self.find_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title after 'find-note'.")
            elif cmd_enum == Command.EDIT_NOTE:
                if len(args) > 1:
                    print(self.edit_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title and new content after 'edit-note'.")
            elif cmd_enum == Command.DELETE_NOTE:
                if args:
                    print(self.delete_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title after 'delete-note'.")
            elif cmd_enum == Command.ALL_NOTES:
                print(self.show_all_notes()) 
            
            else:
                print(Fore.RED + "Unknown command.")