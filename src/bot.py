from colorama import Fore, init
from src.command import Command
from src.completer import Prompt
from src.contacts_book import ContactsBook
from src.notes_book import NotesBook
from src.utils import input_error
from src.handlers import *
from src.command_handlers import get_command_handlers

init(autoreset=True)

class Bot:
    def __init__(self):
        self.prompt = Prompt()
        self.contacts_book = self._load_contacts_book()
        self.notes_book = self._load_notes_book()
        self.command_handlers = self._initialize_handlers()
        self.commands = Command.command_list()

    @staticmethod
    def _load_contacts_book():
        return ContactsBook.load()

    @staticmethod
    def _load_notes_book():
        return NotesBook.load()

    def _initialize_handlers(self):
        help_handler = Help()
        contact_handler = ContactHandler(self.contacts_book)
        contact_additional_handler = ContactAdditionalHandler(self.contacts_book)
        contact_full_handler = ContactFullHandler(self.contacts_book)
        note_handler = NoteHandler(self.notes_book)
        note_full_handler = NoteFullHandler(self.notes_book)

        return get_command_handlers(
            contacts_book=self.contacts_book,
            notes_book=self.notes_book,
            help_handler=help_handler,
            contact_handler=contact_handler,
            contact_additional_handler=contact_additional_handler,
            contact_full_handler=contact_full_handler,
            note_handler=note_handler,
            note_full_handler=note_full_handler,
        )

    def _display_welcome_message(self):
        print(Fore.GREEN + "Welcome to the assistant bot!")

    def _parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    def _execute_command(self, command, args):
        try:
            cmd_enum = Command(command)
        except (KeyError, ValueError):
            print(Fore.RED + "Invalid command.")
            return

        handler = self.command_handlers.get(cmd_enum)
        if handler:
            handler(args)
        else:
            print(Fore.RED + "Unknown command.")

    def run(self):
        self._display_welcome_message()

        while True:
            print()
            user_input = self.prompt.prompt("Enter a command: ", self.commands, style='fg:#0000FF')

            if not user_input:
                continue

            command, args = self._parse_input(user_input)
            self._execute_command(command, args)

# class Bot:
#     def __init__(self):
#         self.contacts_book = ContactsBook.load()
#         self.notes_book = NotesBook.load()
#         self.prompt = Prompt()
#         self.help_handler = Help()
#         self.contact_handler = ContactHandler(self.contacts_book)
#         self.contact_additional_handler = ContactAdditionalHandler(self.contacts_book)
#         self.contact_full_handler = ContactFullHandler(self.contacts_book)
#         self.note_handler = NoteHandler(self.notes_book)
#         self.note_full_handler = NoteFullHandler(self.notes_book)
#         self.command_handlers = get_command_handlers(
#             contacts_book=self.contacts_book,
#             notes_book=self.notes_book,
#             help_handler=self.help_handler,
#             contact_handler=self.contact_handler,
#             contact_additional_handler=self.contact_additional_handler,
#             contact_full_handler=self.contact_full_handler,
#             note_handler=self.note_handler,
#             note_full_handler=self.note_full_handler,
#         )

#     def parse_input(self, user_input):
#         cmd, *args = user_input.split()
#         cmd = cmd.strip().lower()
#         return cmd, args

    
#     def run(self):
#         print(Fore.GREEN + "Welcome to the assistant bot!")

#         commands = Command.command_list()

#         while True:
#             print()
#             user_input = self.prompt.prompt("Enter a command: ", commands, style='fg:#0000FF')

#             if not user_input:
#                 continue

#             command, args = self.parse_input(user_input)

#             if user_input:
#                 try:
#                     cmd_enum = Command(command)
#                 except KeyError:
#                     print(Fore.RED + "Invalid command.")
#                     continue
#                 except ValueError:
#                     print(Fore.RED + "Invalid command.")
#                     continue

#             handler = self.command_handlers.get(cmd_enum)
#             if handler:
#                 handler(args)
#             else:
#                 print(Fore.RED + "Unknown command.")

