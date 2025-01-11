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
from .managers import *

init(autoreset=True)

class Bot:
    def __init__(self):
        self.address_book = AddressBook.load()
        self.notes_book = NotesBook.load()
        self.prompt = Prompt()
        self.contacts_manager = ContactsManager(self.address_book)
        self.additional_info_manager = AdditionalInfoManager(self.address_book)
        self.add_full_contact = AddFullContact(self.address_book)
        self.change_full_contact = ChangeFullContact(self.address_book)

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

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
        help_text += self.format_command("remove-birthday <name>", "Remove a contact's birthday.")
        help_text += self.format_command("birthdays [days]", "Show contacts with upcoming birthdays in the next [days] days (default: 7).")

        help_text += Fore.YELLOW + Style.BRIGHT + "\nAdditional Info:\n"
        help_text += self.format_command("add-email <name> <email>", "Add an email to a contact.")
        help_text += self.format_command("show-email <name>", "Show the email of a contact.")
        help_text += self.format_command("remove-email <name>", "Remove the email of a contact.")
        help_text += self.format_command("add-address <name> <address>", "Add an address to a contact.")
        help_text += self.format_command("show-address <name>", "Show the address of a contact.")
        help_text += self.format_command("remove-address <name>", "Remove the address of a contact.")
        
        help_text += Fore.YELLOW + Style.BRIGHT + "\nNotes Management:\n"
        help_text += self.format_command("add-note <title> <content>", "Add a new note.")
        help_text += self.format_command("find-note <title>", "Find a note by title.")
        help_text += self.format_command("edit-note <title> <new_content>", "Edit an existing note.")
        help_text += self.format_command("delete-note <title>", "Delete a note by title.")
        help_text += self.format_command("all-notes", "Show all notes.")
        
        return help_text

    def run(self):
        print(Fore.GREEN + "Welcome to the assistant bot!")

        commands = Command.command_list()
        
        while True:
            user_input = self.prompt.prompt("Enter a command: ", commands, style='fg:#0000FF')

            if not user_input:
                continue

            command, args = self.parse_input(user_input)

            if user_input:
                try:
                    cmd_enum = Command(command)
                except KeyError:
                    print(Fore.RED + "Invalid command.")
                    continue
                except ValueError:
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
                self.add_full_contact.add_full_contact()
            elif cmd_enum == Command.CHANGE_CONTACT:
                self.change_full_contact.change_full_contact()
            elif cmd_enum == Command.ADD_PHONE:
                if args:
                    print(self.contacts_manager.add_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and phone number after 'add-phone'.")
            elif cmd_enum == Command.CHANGE_PHONE:
                if len(args) == 3:
                    print(self.contacts_manager.change_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name, old phone number and new phone number after 'change-phone'.")
            elif cmd_enum == Command.CHANGE_NAME:
                if len(args) == 2:
                    print(self.contacts_manager.change_name(args))
                else:
                    print(Fore.YELLOW + "Please provide the old contact name and new contact name after 'change-name'.")
            elif cmd_enum == Command.SHOW_PHONE:
                if args:
                    print(self.contacts_manager.show_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-phone'.")
            elif cmd_enum == Command.REMOVE_PHONE:
                if len(args) == 2:
                    print(self.contacts_manager.remove_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and phone number after 'remove-phone'.")
            elif cmd_enum == Command.REMOVE_CONTACT:
                if args:
                    print(self.contacts_manager.remove_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-contact'.")
            elif cmd_enum == Command.ALL_CONTACTS:
                print(self.contacts_manager.show_all())
            elif cmd_enum == Command.ADD_BIRTHDAY:
                if len(args) == 2:
                    print(self.contacts_manager.add_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and birthday (DD.MM.YYYY) after 'add-birthday'.")
            elif cmd_enum == Command.SHOW_BIRTHDAY:
                if args:
                    print(self.contacts_manager.show_contact_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-birthday'.")
            elif cmd_enum == Command.REMOVE_BIRTHDAY:
                if args:
                    print(self.contacts_manager.remove_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-birthday'.")
            elif cmd_enum == Command.BIRTHDAYS:
                print(self.contacts_manager.show_birthdays(args))
            elif cmd_enum == Command.HELP:
                print(self.show_help())
            elif cmd_enum == Command.ADD_EMAIL:
                if len(args) == 2:
                    print(self.additional_info_manager.add_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and email after 'add-email'.")
            elif cmd_enum == Command.SHOW_EMAIL:
                if args:
                    print(self.additional_info_manager.show_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-email'.")
            elif cmd_enum == Command.REMOVE_EMAIL:
                if args:
                    print(self.additional_info_manager.remove_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-email'.")
            elif cmd_enum == Command.ADD_ADDRESS:
                if len(args) > 1:
                    print(self.additional_info_manager.add_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and address after 'add-address'.")
            elif cmd_enum == Command.SHOW_ADDRESS:
                if args:
                    print(self.additional_info_manager.show_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-address'.")
            elif cmd_enum == Command.REMOVE_ADDRESS:
                if args:
                    print(self.additional_info_manager.remove_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-address'.")
            elif cmd_enum == Command.FIND_CONTACT:
                if args:
                    print(self.contacts_manager.find_contact(args))
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