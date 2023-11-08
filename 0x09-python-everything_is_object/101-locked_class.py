"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass called 'first_name'.
    """

    __slots__ = ["first_name"]
