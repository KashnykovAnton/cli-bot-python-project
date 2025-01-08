from enum import Enum

class Command(Enum):
    EXIT = "exit"
    CLOSE = "close"
    HELLO = "hello"
    HELP = "help"
    ADD_CONTACT = "add-contact"
    FIND_CONTACT = "find-contact"
    REMOVE_CONTACT = "remove-contact"
    ALL_CONTACTS = "all-contacts"
    ADD_PHONE = "add-phone"
    CHANGE_PHONE = "change-phone"
    SHOW_PHONE = "show_phone"
    REMOVE_PHONE = "remove-phone"
    CHANGE_NAME = "change-name"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    BIRTHDAYS = "birthdays"
    ADD_EMAIL = "add-email"
    SHOW_EMAIL = "show-email"
    ADD_ADDRESS = "add-address"
    SHOW_ADDRESS = "show-address"
    ADD_NOTE = 'add-note'
    FIND_NOTE = 'find-note'
    EDIT_NOTE = 'edit-note'
    DELETE_NOTE = 'delete-note'
    ALL_NOTES = 'all-notes'