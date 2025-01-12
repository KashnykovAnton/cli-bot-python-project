from enum import Enum

class Command(Enum):
    EXIT = "exit"
    CLOSE = "close"
    HELLO = "hello"
    HELP = "help"
    ADD_CONTACT = "add-contact"
    CHANGE_CONTACT = "change-contact"
    FIND_CONTACT = "find-contact"
    REMOVE_CONTACT = "remove-contact"
    ALL_CONTACTS = "all-contacts"
    ADD_PHONE = "add-phone"
    CHANGE_PHONE = "change-phone"
    SHOW_PHONE = "show-phone"
    REMOVE_PHONE = "remove-phone"
    CHANGE_NAME = "change-name"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    REMOVE_BIRTHDAY = "remove-birthday"
    BIRTHDAYS = "birthdays"
    ADD_EMAIL = "add-email"
    SHOW_EMAIL = "show-email"
    REMOVE_EMAIL = "remove-email"
    ADD_ADDRESS = "add-address"
    SHOW_ADDRESS = "show-address"
    REMOVE_ADDRESS = "remove-address"
    ADD_NOTE = 'add-note'
    FIND_NOTE = 'find-note'
    EDIT_NOTE = 'edit-note'
    REMOVE_NOTE = 'remove-note'
    ALL_NOTES = 'all-notes'
    ADD_TAG = 'add-tag'
    FIND_BY_TAG = 'find-by-tag'
    REMOVE_TAG = 'remove-tag'
    ADD_FULL_NOTE = 'add-full-note'
    CHANGE_FULL_NOTE = 'change-full-note'

    @classmethod
    def command_list(cls):
        return [command.value for command in cls]