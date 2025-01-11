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
        for note_title, note in self.notes.items():
            if note_title.lower() == title.lower():
                return note
        return "Note not found."

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
        return "\n\n".join([f"#{index + 1}: {str(note)}" for index, note in enumerate(self.notes.values())])

    def find_note_by_tag(self, tag):
        if isinstance(tag, str):
            tag = [tag]
        
        matching_notes = []
        for note in self.notes.values():
            if any(t.lower() in [x.lower() for x in note.tags] for t in tag):
                matching_notes.append(note)

        if matching_notes:
            matching_notes.sort(key=lambda note: note.title.lower())
            return "\n\n".join(str(note) for note in matching_notes)
        else:
            return Fore.RED + f"No notes found with tag(s) {', '.join(tag)}."

    def remove_tag(self, title):
        note = None
        for stored_title, stored_note in self.notes.items():
            if stored_title.lower() == title.lower():
                note = stored_note
                break
        if note is None:
            return Fore.RED + "Note not found."
        note.tags = []
        return Fore.GREEN + f"Tags removed from note '{title}'."

    def add_full_note(self):
        print(Fore.CYAN + "Adding a new note. Follow the steps below:")
        
        # Step 1: Add Title (required)
        title = input(Fore.YELLOW + "Enter note title: ").strip()
        if not title:
            print(Fore.RED + "Title is required. Cancelling operation.")
            return
        if title in self.notes:
            print(Fore.YELLOW + f"Note with title '{title}' already exists. Cancelling operation.")
            return
        else:
            print(Fore.GREEN + f"Note '{title}' will be added.")

        # Step 2: Add Content (required)
        content = input(Fore.YELLOW + "Enter note content: ").strip()
        if not content:
            print(Fore.RED + "Content is required. Cancelling operation.")
            return
        note = Note(title, content)
        self.notes[title] = note
        print(Fore.GREEN + f"Note '{title}' added successfully with content.")

        # Step 3: Add Tags (optional)
        tags_input = input(Fore.YELLOW + "Enter tags (leave empty to skip): ").strip()
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(' ')]
            note.add_tags(tags)
            print(Fore.GREEN + f"Tags added: {', '.join(tags)}.")
        else:
            print(Fore.YELLOW + "No tags provided. Skipping tags.")

        print(Fore.GREEN + f"Note '{title}' has been added successfully.")


    def change_full_note(self):
        print(Fore.CYAN + "Changing an existing note. Follow the steps below:")

        # Step 1: Enter the title of the note to be updated (required)
        title = input(Fore.YELLOW + "Enter the title of the note to change: ").strip()
        if not title:
            print(Fore.RED + "Title is required. Cancelling operation.")
            return

        # Check if the note with the given title exists
        note = self.notes.get(title)
        if note is None:
            print(Fore.RED + f"Note with title '{title}' not found. Cancelling operation.")
            return

        print(Fore.GREEN + f"Found note with title '{title}'. Proceeding with changes.")

        # Step 2: Change the title (optional)
        new_title = input(Fore.YELLOW + f"Enter new title for note '{title}' (leave empty to skip): ").strip()
        if new_title:
            if new_title in self.notes:
                print(Fore.RED + f"Note with title '{new_title}' already exists. Skipping title change.")
            else:
                self.notes[new_title] = self.notes.pop(title)
                title = new_title
                print(Fore.GREEN + f"Title updated to '{new_title}'.")
        else:
            print(Fore.YELLOW + "No title change. Skipping title update.")

        # Step 3: Change the content (required)
        new_content = input(Fore.YELLOW + f"Enter new content for note '{title}': ").strip()
        if not new_content:
            print(Fore.RED + "Content is required. Cancelling operation.")
            return
        note.edit(new_content)
        print(Fore.GREEN + f"Content for note '{title}' updated successfully.")

        # Step 4: Change Tags (optional)
        tags_input = input(Fore.YELLOW + "Enter new tags (leave empty to skip): ").strip()
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(' ')]
            note.add_tags(tags)
            print(Fore.GREEN + f"Tags updated: {', '.join(tags)}.")
        else:
            print(Fore.YELLOW + "No tags provided. Skipping tag update.")

        print(Fore.GREEN + f"Note '{title}' has been successfully updated.")
