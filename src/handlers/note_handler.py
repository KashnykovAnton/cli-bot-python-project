from colorama import Fore
from src.note import Note
from src.utils import input_error

class NoteHandler:
    def __init__(self, notes_book):
        self.notes_book = notes_book

    @input_error
    def add_note(self, args):
        title, content = args[0], " ".join(args[1:])
        return self.notes_book.add_note(title, content)

    @input_error
    def find_note(self, args):
        title = args[0]
        return self.notes_book.find_note(title)
    
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

    @input_error
    def add_tag_to_note(self, args):
        title = args[0]
        tags = args[1:]

        note = self.notes_book.find_note(title)
        if note == "Note not found.":
            return Fore.RED + f"Note with title '{title}' not found."

        note.add_tags(tags)
        return Fore.GREEN + f"Tags added to note '{title}' successfully. Current tags: {', '.join(note.tags)}"
    
    @input_error
    def find_note_by_tag(self, args):
        tag = " ".join(args)
        return self.notes_book.find_note_by_tag(tag)

    @input_error
    def remove_tag(self, args):
        title = args[0]
        return self.notes_book.remove_tag(title)
