#!/usr/bin/python3
# 3-say_my_name.py
# Albert Ezoula
def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

        Args:
            first_name (st): First params
            last_name (str): Second params
        Raises:
            TypeError : if one arg is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
