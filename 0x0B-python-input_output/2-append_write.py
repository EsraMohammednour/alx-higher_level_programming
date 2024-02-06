#!/usr/bin/python3
"""
saroo
"""


def append_write(filename="", text=""):
    """
    whew
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
