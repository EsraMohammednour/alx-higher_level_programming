#!/usr/bin/python3
"""
saroo
"""


def class_to_json(obj):
    """
    saroo
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
