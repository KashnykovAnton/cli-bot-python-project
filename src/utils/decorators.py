from functools import wraps
from colorama import Fore

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return Fore.RED + f"Error: {str(e)}"
    return inner