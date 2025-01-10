import pickle
from colorama import Fore
from .note import Note

class NotesBook:
    def __init__(self):
        self.notes = {}

    @staticmethod
    def load(filename="notesbook.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(Fore.YELLOW + "No saved notes found. Starting with a new one.")
            return NotesBook()

    def save(self, filename="notesbook.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        print(Fore.GREEN + "Notes saved successfully.")

    def add_note(self, title, content):
        if title in self.notes:
            return Fore.RED + f"Note with title '{title}' already exists."
        note = Note(title, content)
        self.notes[title] = note
        return Fore.GREEN + f"Note '{title}' added successfully."

    def find_note(self, title):
        return self.notes.get(title, "Note not found.")

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            return Fore.GREEN + f"Note '{title}' deleted successfully."
        return Fore.RED + "Note not found."

    def edit_note(self, title, new_content):
        note = self.notes.get(title)
        if note:
            note.edit(new_content)
            return Fore.GREEN + f"Note '{title}' updated successfully."
        return Fore.RED + "Note not found."

    def show_all_notes(self):
        if not self.notes:
            return Fore.RED + "No notes found."
        return "\n".join([str(note) for note in self.notes.values()])