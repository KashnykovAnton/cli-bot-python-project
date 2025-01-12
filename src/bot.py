from colorama import Fore, init
from src.command import Command
from src.completer import Prompt
from src.address_book import AddressBook
from src.notes_book import NotesBook
from src.utils import input_error
from src.handlers import *

init(autoreset=True)

class Bot:
    def __init__(self):
        self.address_book = AddressBook.load()
        self.notes_book = NotesBook.load()
        self.prompt = Prompt()
        self.help_handler = Help()
        self.contact_handler = ContactHandler(self.address_book)
        self.contact_additional_handler = ContactAdditionalHandler(self.address_book)
        self.contact_full_handler = ContactFullHandler(self.address_book)
        self.note_handler = NoteHandler(self.notes_book)
        self.note_full_handler = NoteFullHandler(self.notes_book)

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args


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
            elif cmd_enum == Command.HELP:
                print(self.help_handler.show_help())
            elif cmd_enum == Command.ADD_CONTACT:
                self.contact_full_handler.add_full_contact()
            elif cmd_enum == Command.CHANGE_CONTACT:
                self.contact_full_handler.change_full_contact(args)
            elif cmd_enum == Command.ADD_PHONE:
                if args:
                    print(self.contact_handler.add_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and phone number after 'add-phone'.")
            elif cmd_enum == Command.CHANGE_PHONE:
                if len(args) == 3:
                    print(self.contact_handler.change_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name, old phone number and new phone number after 'change-phone'.")
            elif cmd_enum == Command.CHANGE_NAME:
                if len(args) == 2:
                    print(self.contact_handler.change_name(args))
                else:
                    print(Fore.YELLOW + "Please provide the old contact name and new contact name after 'change-name'.")
            elif cmd_enum == Command.SHOW_PHONE:
                if args:
                    print(self.contact_handler.show_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-phone'.")
            elif cmd_enum == Command.REMOVE_PHONE:
                if len(args) == 2:
                    print(self.contact_handler.remove_phone(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and phone number after 'remove-phone'.")
            elif cmd_enum == Command.REMOVE_CONTACT:
                if args:
                    print(self.contact_handler.remove_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-contact'.")
            elif cmd_enum == Command.FIND_CONTACT:
                if args:
                    print(self.contact_handler.find_contact(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'find-contact'.")
            elif cmd_enum == Command.ALL_CONTACTS:
                print(self.contact_handler.show_all())
            elif cmd_enum == Command.ADD_BIRTHDAY:
                if len(args) == 2:
                    print(self.contact_handler.add_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and birthday (DD.MM.YYYY) after 'add-birthday'.")
            elif cmd_enum == Command.SHOW_BIRTHDAY:
                if args:
                    print(self.contact_handler.show_contact_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-birthday'.")
            elif cmd_enum == Command.REMOVE_BIRTHDAY:
                if args:
                    print(self.contact_handler.remove_birthday(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-birthday'.")
            elif cmd_enum == Command.BIRTHDAYS:
                print(self.contact_handler.show_birthdays(args))
            elif cmd_enum == Command.ADD_EMAIL:
                if len(args) == 2:
                    print(self.contact_additional_handler.add_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and email after 'add-email'.")
            elif cmd_enum == Command.SHOW_EMAIL:
                if args:
                    print(self.contact_additional_handler.show_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-email'.")
            elif cmd_enum == Command.REMOVE_EMAIL:
                if args:
                    print(self.contact_additional_handler.remove_email(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-email'.")
            elif cmd_enum == Command.ADD_ADDRESS:
                if len(args) > 1:
                    print(self.contact_additional_handler.add_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name and address after 'add-address'.")
            elif cmd_enum == Command.SHOW_ADDRESS:
                if args:
                    print(self.contact_additional_handler.show_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'show-address'.")
            elif cmd_enum == Command.REMOVE_ADDRESS:
                if args:
                    print(self.contact_additional_handler.remove_address(args))
                else:
                    print(Fore.YELLOW + "Please provide the contact name after 'remove-address'.")
            elif cmd_enum == Command.ADD_NOTE:
                if len(args) > 1:
                    print(self.note_handler.add_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title and content after 'add-note'.")
            elif cmd_enum == Command.FIND_NOTE:
                if args:
                    print(self.note_handler.find_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title after 'find-note'.")
            elif cmd_enum == Command.EDIT_NOTE:
                if len(args) > 1:
                    print(self.note_handler.edit_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title and new content after 'edit-note'.")
            elif cmd_enum == Command.REMOVE_NOTE:
                if args:
                    print(self.note_handler.delete_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title after 'delete-note'.")
            elif cmd_enum == Command.ALL_NOTES:
                print(self.note_handler.show_all_notes()) 
            elif cmd_enum == Command.ADD_TAG:
                if len(args) > 1:
                    print(self.note_handler.add_tag_to_note(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title and tags after 'add-tag'.")
            elif cmd_enum == Command.FIND_BY_TAG:
                if args:
                    print(self.note_handler.find_note_by_tag(args))
                else:
                    print(Fore.YELLOW + "Please provide the tag after 'find-by-tag'.")
            elif cmd_enum == Command.REMOVE_TAG:
                if args:
                    print(self.note_handler.remove_tag(args))
                else:
                    print(Fore.YELLOW + "Please provide the note title after 'remove-tag'.")
            elif cmd_enum == Command.ADD_FULL_NOTE:
                self.note_full_handler.add_full_note()
            elif cmd_enum == Command.CHANGE_FULL_NOTE:
                self.note_full_handler.change_full_note()
            
            else:
                print(Fore.RED + "Unknown command.")