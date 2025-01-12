from colorama import Fore
from src.note import Note

class NoteFullHandler:
    def __init__(self, notes_book):
        self.notes_book = notes_book

    def add_full_note(self):
        print(Fore.CYAN + "Adding a new note. Follow the steps below:")
        
        # Step 1: Add Title (required)
        title = input(Fore.YELLOW + "Enter note title: ").strip()
        if not title:
            print(Fore.RED + "Title is required. Cancelling operation.")
            return
        if title in self.notes_book.notes:
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
        self.notes_book.notes[title] = note
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
        note = self.notes_book.notes.get(title)
        if note is None:
            print(Fore.RED + f"Note with title '{title}' not found. Cancelling operation.")
            return

        print(Fore.GREEN + f"Found note with title '{title}'. Proceeding with changes.")

        # Step 2: Change the title (optional)
        new_title = input(Fore.YELLOW + f"Enter new title for note '{title}' (leave empty to skip): ").strip()
        if new_title:
            if new_title in self.notes_book.notes:
                print(Fore.RED + f"Note with title '{new_title}' already exists. Skipping title change.")
            else:
                note_to_update = self.notes_book.notes.pop(title)
                note = Note(title=new_title, content=note_to_update.content)
                note.add_tags(note_to_update.tags)
                self.notes_book.notes[new_title] = note
                print(Fore.GREEN + f"Title updated to '{new_title}'.")
        else:
            print(Fore.YELLOW + "No title change. Skipping title update.")

        # Step 3: Change the content (required)
        new_content = input(Fore.YELLOW + f"Enter new content for note '{new_title}': ").strip()
        if not new_content:
            print(Fore.RED + "Content is required. Cancelling operation.")
            return
        note.edit(new_content)
        print(Fore.GREEN + f"Content for note '{new_title}' updated successfully.")

        # Step 4: Change Tags (optional)
        tags_input = input(Fore.YELLOW + "Enter new tags (leave empty to skip): ").strip()
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(' ')]
            note.add_tags(tags)
            print(Fore.GREEN + f"Tags updated: {', '.join(tags)}.")
        else:
            print(Fore.YELLOW + "No tags provided. Skipping tag update.")

        print(Fore.GREEN + f"Note '{title}' has been successfully updated.")
