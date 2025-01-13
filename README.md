# Contacts & Notes Assistant

This project provides a command-line interface (CLI) bot for managing a **Contacts Book** and **Notes Book**. Users can save, edit, and manage their contacts and notes efficiently. The bot offers a user-friendly interface to interact with data, making everyday tasks simpler and more organized.

## How to Run the Project

### 1. Activate Virtual Environment
To set up the environment:
```bash
source .venv/bin/activate
```

### 2. Install Dependencies
Install all required packages using:
```bash
pip install -r requirements.txt
```

### 3. Run the Bot
Start the bot by running the main script:
```bash
python main.py
```

### 4. Deactivate Virtual Environment
Once you're done, deactivate the virtual environment:
```bash
deactivate
```

---

## Using the Contacts & Notes Assistant
The bot is designed to work in the console. Users interact with it by typing commands, and the bot responds with helpful outputs to guide the user. Simply type a command and follow the instructions to perform various actions on contacts or notes.

### Example Usage
1. **Add a Contact**: Type `add-contact` and follow the prompts to add a new contact.
2. **Find a Note**: Use `find-note <title>` to search for a specific note.
3. **Show All Contacts**: Type `all-contacts` to display all saved contacts.

---

## Commands Reference
Below is a comprehensive list of commands categorized by functionality.

### General Commands
| Command         | Description                    |
|-----------------|--------------------------------|
| `hello`         | Greet the bot.                |
| `exit, close`   | Exit the bot.                 |
| `help`          | Show help text with commands. |

### Contact Management
| Command                                   | Description                                           |
|------------------------------------------|-------------------------------------------------------|
| `add-contact`                            | Add a new contact with all fields interactively.      |
| `change-contact`                         | Update all fields of an existing contact interactively.|
| `all-contacts`                           | Show all contacts in the address book.               |
| `find-contact <name>`                    | Find contacts by name.                                |
| `remove-contact <name>`                  | Remove a contact from the address book.              |
| `add-phone <name> <phone>`               | Add a new phone number to a contact.                 |
| `change-phone <name> <old_phone> <new_phone>` | Change a contact's phone number.                     |
| `show-phone <name>`                      | Show phone numbers of a contact.                     |
| `remove-phone <name> <phone>`            | Remove a specific phone number from a contact.       |
| `change-name <old_name> <new_name>`      | Change a contact's name.                             |
| `add-birthday <name> <birthday>`         | Add a birthday to a contact (format: YYYY-MM-DD).    |
| `show-birthday <name>`                   | Show a contact's birthday.                           |
| `remove-birthday <name>`                 | Remove a contact's birthday.                         |
| `birthdays [days]`                       | Show contacts with upcoming birthdays in the next [days] days (default: 7). |
| `add-email <name> <email>`               | Add an email to a contact.                           |
| `show-email <name>`                      | Show the email of a contact.                         |
| `remove-email <name>`                    | Remove the email of a contact.                       |
| `add-address <name> <address>`           | Add an address to a contact.                         |
| `show-address <name>`                    | Show the address of a contact.                       |
| `remove-address <name>`                  | Remove the address of a contact.                     |

### Notes Management
| Command                                   | Description                                           |
|------------------------------------------|-------------------------------------------------------|
| `add-full-note`                          | Add a new note with all fields interactively.         |
| `change-full-note`                       | Update all fields of an existing note interactively.  |
| `all-notes`                              | Show all notes.                                       |
| `add-note <title> <content>`             | Add a new note.                                       |
| `find-note <title>`                      | Find a note by title.                                 |
| `edit-note <title> <new_content>`        | Edit an existing note.                                |
| `remove-note <title>`                    | Delete a note by title.                               |
| `add-tag <title> <tags>`                 | Add tags to a note.                                   |
| `find-by-tag <tag>`                      | Find notes by tag.                                    |
| `remove-tag <title>`                     | Remove tags from a note.                             |

---

## Technologies and Libraries Used

This project uses the following libraries and tools:

- **[colorama](https://pypi.org/project/colorama/)**: For colored terminal text.
- **[prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/)**: For interactive command-line input.

Additionally, the project leverages Python’s built-in libraries:

- **[datetime](https://docs.python.org/3/library/datetime.html)**: For managing dates and times.
- **[enum](https://docs.python.org/3/library/enum.html)**: For enumerations.
- **[pickle](https://docs.python.org/3/library/pickle.html)**: For object serialization.
- **[functools](https://docs.python.org/3/library/functools.html)**: For higher-order functions.
- **[collections](https://docs.python.org/3/library/collections.html)**: For specialized container datatypes.

---

## Developer
This project is developed and maintained by:

- **Kashnykov Anton** [GitHub Repository](https://github.com/KashnykovAnton)
- **Bazhinova Irina** [GitHub Repository](https://github.com/Iris2030)
- **Ostafiichuk Oleksii** [GitHub Repository](https://github.com/OstafiichukO)
- **Drynko Oleksii** [GitHub Repository](https://github.com/Aleksey-Dr)
