#!/usr/bin/python3
# 1-write_file.py
# Albert Ezoula
"""Define a text file-writing funtion"""


def write_file(filename="", text=""):
    """
    function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added:
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
