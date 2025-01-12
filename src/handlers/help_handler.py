from colorama import Fore, Style
from src.command import Command

class Help:
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
        help_text += self.format_command("add-full-note", "Add a new note with all fields interactively.")
        help_text += self.format_command("change-full-note", "Update all fields of an existing note interactively.")
        help_text += self.format_command("add-note <title> <content>", "Add a new note.")
        help_text += self.format_command("find-note <title>", "Find a note by title.")
        help_text += self.format_command("edit-note <title> <new_content>", "Edit an existing note.")
        help_text += self.format_command("remove-note <title>", "Delete a note by title.")
        help_text += self.format_command("all-notes", "Show all notes.")
        help_text += self.format_command("add-tag <title> <tags>", "Add tags to a note.")
        help_text += self.format_command("find-by-tag <tag>", "Find notes by tag.")
        help_text += self.format_command("remove-tag <title>", "Remove tags from a note.")
        
        return help_text