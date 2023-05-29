"""This module is private ! Don't use it !"""
from pathlib import Path


def compute_path(directory, entry):
    path = Path(directory, entry)
    return str(path.resolve())


def validate_entry(entry):
    if not entry or not isinstance(entry, str):
        return False
    if len(entry) == 1 and not entry.isalnum():
        return False
    for char in entry:
        if not char.isalnum() and char not in ("_", "-", "."):
            return False
    return True
