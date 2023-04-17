#!/usr/bin/python3
# 4-list_division.py
# Albert Ezoula
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists."""

    new_list = []
    for i in range(0, list_length):
        try:
            rest = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            rest = 0
        except ZeroDivisionError:
            print("division by 0")
            rest = 0
        except IndexError:
            print("out of range")
            rest = 0
        finally:
            new_list.append(rest)
        return (rest)
