#!/usr/bin/python3
# 1-write_file.py
# Albert Ezoula
"""Define a text file-writing funtion"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        characters = 0
        text_array = text.split()
        for word in text_array:
            for char in word:
                characters += 1
        return (characters)
