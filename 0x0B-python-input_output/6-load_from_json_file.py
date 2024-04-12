#!/usr/bin/python3
"""
saroo
"""
import json


def load_from_json_file(filename):
    """
    saroo
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
