import pickle
from datetime import datetime, timedelta
from colorama import Fore
from collections import UserDict
from .record import Record
from .fields import *

class AddressBook(UserDict):
    @staticmethod
    def load(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(Fore.YELLOW + "No saved address book found. Starting with a new one.")
            return AddressBook()

    def save(self, filename="addressbook.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        print(Fore.GREEN + "Address book saved successfully.")

    def add_record(self, record):
        if record.name.value in self.data:
            return Fore.RED + f"Record with name '{record.name.value}' already exists."
        self.data[record.name.value] = record
        return Fore.GREEN + f"Record for '{record.name.value}' has been successfully added."

    def find(self, name):
        record = self.data.get(name)
        if record:
            print(Fore.GREEN + f"Record for '{name}' found.")
            return record
        return Fore.RED + f"No record found for '{name}'."

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return Fore.GREEN + f"Record for '{name}' has been successfully deleted."
        return Fore.RED + f"Cannot delete: No record found for '{name}'."

    def get_upcoming_birthdays(self, days):
        today = datetime.today().date()
        upcoming_birthdays = []

        for name, record in self.data.items():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                difference = (birthday_this_year - today).days
                if difference <= days:
                    weekday = birthday_this_year.weekday()
                    if weekday == 5:  # If Saturday
                        birthday_this_year += timedelta(days=2)
                    elif weekday == 6:  # If Sunday
                        birthday_this_year += timedelta(days=1)

                    upcoming_birthdays.append({
                        "name": name,
                        "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
                    })

        return upcoming_birthdays