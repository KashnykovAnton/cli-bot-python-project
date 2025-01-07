# cli-bot-python-project

<!-- Run the project -->
Activate virtual environment:
    source .venv/bin/activate

Deactivate virtual environment
    deactivate

Installing packages from requirements.txt
    pip install -r requirements.txt

<!-- Project structure -->
main.py - main file in the priject for run the cli
src/command.py - file with enums of all commands that can be used in the project. The first place where new command should be added.
src/record.py - file with all the logic for contact
src/address_book.py - file with all the logic for addressbook
src/bot.py - class Bot manage the cli work. 
    input_error - manage the errors in all functions
    parse_input - manage the commands from console
    run - work with all commands that user type in console

folder fields - contains all classes with fields for contact. Main parent class - field.py.

