from mybank.logger import myprint 

from typing import Callable

from mybank.logger import myprint

def log_action(func: Callable):
    def wrapper(*args, **kwargs):
        func()
        myprint(f"User {func.__name__} funksiyasini ishlatdi.", "DEBUG")
    
    return wrapper
