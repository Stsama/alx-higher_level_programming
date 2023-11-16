#!/usr/bin/python3
# 2-append_write.py
# Albert Ezoula
"""Define a text file-appending funtion"""


def append_write(filename="", text=""):
    """append a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        characters = 0
        for char in text:
            characters += 1
        return (characters)
