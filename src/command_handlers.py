from colorama import Fore
from src.command import Command

def get_command_handlers(contacts_book, notes_book, contact_full_handler, contact_handler, contact_additional_handler, note_handler, note_full_handler, help_handler):
    def exit_program():
        print(Fore.GREEN + "Good bye!")
        contacts_book.save()
        notes_book.save()
        exit()

    return {
        Command.EXIT: lambda args: exit_program(),
        Command.CLOSE: lambda args: exit_program(),
        Command.HELLO: lambda args: print(Fore.GREEN + "How can I help you?"),
        Command.HELP: lambda args: print(help_handler.show_help()),
        Command.ADD_CONTACT: lambda args: contact_full_handler.add_full_contact(),
        Command.CHANGE_CONTACT: lambda args: contact_full_handler.change_full_contact(args),
        Command.ADD_PHONE: lambda args: print(contact_handler.add_contact(args)) if args else print(Fore.YELLOW + "Please provide the contact name and phone number after 'add-phone'."),
        Command.CHANGE_PHONE: lambda args: print(contact_handler.change_phone(args)) if len(args) == 3 else print(Fore.YELLOW + "Please provide the contact name, old phone number and new phone number after 'change-phone'."),
        Command.CHANGE_NAME: lambda args: print(contact_handler.change_name(args)) if len(args) == 2 else print(Fore.YELLOW + "Please provide the old contact name and new contact name after 'change-name'."),
        Command.SHOW_PHONE: lambda args: print(contact_handler.show_phone(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'show-phone'."),
        Command.REMOVE_PHONE: lambda args: print(contact_handler.remove_phone(args)) if len(args) == 2 else print(Fore.YELLOW + "Please provide the contact name and phone number after 'remove-phone'."),
        Command.REMOVE_CONTACT: lambda args: print(contact_handler.remove_contact(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'remove-contact'."),
        Command.FIND_CONTACT: lambda args: print(contact_handler.find_contact(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'find-contact'."),
        Command.ALL_CONTACTS: lambda args: print(contact_handler.show_all()),
        Command.ADD_BIRTHDAY: lambda args: print(contact_handler.add_birthday(args)) if len(args) == 2 else print(Fore.YELLOW + "Please provide the contact name and birthday (DD.MM.YYYY) after 'add-birthday'."),
        Command.SHOW_BIRTHDAY: lambda args: print(contact_handler.show_contact_birthday(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'show-birthday'."),
        Command.REMOVE_BIRTHDAY: lambda args: print(contact_handler.remove_birthday(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'remove-birthday'."),
        Command.BIRTHDAYS: lambda args: print(contact_handler.show_birthdays(args)),
        Command.ADD_EMAIL: lambda args: print(contact_additional_handler.add_email(args)) if len(args) == 2 else print(Fore.YELLOW + "Please provide the contact name and email after 'add-email'."),
        Command.SHOW_EMAIL: lambda args: print(contact_additional_handler.show_email(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'show-email'."),
        Command.REMOVE_EMAIL: lambda args: print(contact_additional_handler.remove_email(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'remove-email'."),
        Command.ADD_ADDRESS: lambda args: print(contact_additional_handler.add_address(args)) if len(args) > 1 else print(Fore.YELLOW + "Please provide the contact name and address after 'add-address'."),
        Command.SHOW_ADDRESS: lambda args: print(contact_additional_handler.show_address(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'show-address'."),
        Command.REMOVE_ADDRESS: lambda args: print(contact_additional_handler.remove_address(args)) if args else print(Fore.YELLOW + "Please provide the contact name after 'remove-address'."),
        Command.ADD_NOTE: lambda args: print(note_handler.add_note(args)) if len(args) > 1 else print(Fore.YELLOW + "Please provide the note title and content after 'add-note'."),
        Command.FIND_NOTE: lambda args: print(note_handler.find_note(args)) if args else print(Fore.YELLOW + "Please provide the note title after 'find-note'."),
        Command.EDIT_NOTE: lambda args: print(note_handler.edit_note(args)) if len(args) > 1 else print(Fore.YELLOW + "Please provide the note title and new content after 'edit-note'."),
        Command.REMOVE_NOTE: lambda args: print(note_handler.delete_note(args)) if args else print(Fore.YELLOW + "Please provide the note title after 'delete-note'."),
        Command.ALL_NOTES: lambda args: print(note_handler.show_all_notes()),
        Command.ADD_TAG: lambda args: print(note_handler.add_tag_to_note(args)) if len(args) > 1 else print(Fore.YELLOW + "Please provide the note title and tags after 'add-tag'."),
        Command.FIND_BY_TAG: lambda args: print(note_handler.find_note_by_tag(args)) if args else print(Fore.YELLOW + "Please provide the tag after 'find-by-tag'."),
        Command.REMOVE_TAG: lambda args: print(note_handler.remove_tag(args)) if args else print(Fore.YELLOW + "Please provide the note title after 'remove-tag'."),
        Command.ADD_FULL_NOTE: lambda args: note_full_handler.add_full_note(),
        Command.CHANGE_FULL_NOTE: lambda args: note_full_handler.change_full_note(),
    }
