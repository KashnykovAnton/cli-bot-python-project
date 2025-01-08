from enum import Enum

class Command(Enum):
    EXIT = "exit"
    CLOSE = "close"
    HELLO = "hello"
    ADD_CONTACT = "add-contact"
    ADD = "add"
    CHANGE = "change"
    CHANGE_NAME = "change-name"
    REMOVE = "remove"
    PHONE = "phone"
    REMOVE_PHONE = "remove-phone"
    ALL = "all"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    BIRTHDAYS = "birthdays"
    HELP = "help"
    ADD_EMAIL = "add-email"
    SHOW_EMAIL = "show-email"
    ADD_ADDRESS = "add-address"
    SHOW_ADDRESS = "show-address"
    FIND = "find"
    ADD_NOTE = 'add-note'
    FIND_NOTE = 'find-note'
    EDIT_NOTE = 'edit-note'
    DELETE_NOTE = 'delete-note'
    ALL_NOTES = 'all-notes'