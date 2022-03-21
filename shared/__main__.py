"""Command line interface"""
import sys
import os
import os.path
from shared import Dossier
from shared.util import valid_dossier, json_load, convert_size


__all__ = []


HELP = """\

Welcome to Shared !
https://github.com/pyrustic/shared

Shared is part of the Pyrustic Open Ecosystem
https://pyrustic.github.io


Description
===========
Shared is a Python library for data exchange and persistence.
Use this CLI tool to create, read, and edit dossiers.


Commands
========
There are six commands available:

    init check get set del help


Initialize a new dossier
========================
The 'init' command turns the empty current working directory
into a valid dossier.

    Create the dossier
    ==================
    init


Read and write
==============
The 'check' command allows you to get basic information about
the contents of a dossier.
Use 'get', 'set', and 'del' commands to retrieve, update,
and delete dossier data respectively.
The current working directory is considered the dossier.

    Check the dossier
    =================
    check
    
    Check an entry
    ==============
    check <entry-name>
    
    Content of an entry
    ===================
    get <entry-name>
    
    Copy the content of an entry
    ============================
    get <entry-name> > <destination-filename>
    
    Update the content of an entry
    ==============================
    set <entry-name> <type>
    set <entry-name> <type> <new-content-filename>
    Valid types: dict list set bin
    
    Delete a specific entry
    =======================
    del <entry-name>
    
    Delete multiple entries
    =======================
    del <entry-name> <entry-name> ...
"""

DIRECTORY_MUST_BE_EMPTY_NOTE = "Directory must be empty before initialization."
EMPTY_DOSSIER_NOTE = "This dossier is empty."
SUCCESSFULLY_INIT_DOSSIER = "Successfully initialized this dossier !"
ENTRY_DOESNT_EXIST_NOTE = "This entry doesn't exist."
NOT_VALID_DOSSIER_NOTE = "This is not a valid dossier."
DOSSIER_ALREADY_EXISTS_NOTE = "This dossier already exists."
INCORRECT_USAGE_ERROR = "Incorrect usage of the command."


def help_handler(*args):
    print(HELP)


def init_handler(*args):
    if len(args):
        print(INCORRECT_USAGE_ERROR)
        return
    cache = get_dossier()
    if cache:
        print(DOSSIER_ALREADY_EXISTS_NOTE)
        return
    cwd = os.getcwd()
    dossier_parent, dossier_name = os.path.split(cwd)
    if os.listdir(cwd):
        print(DIRECTORY_MUST_BE_EMPTY_NOTE)
        return
    Dossier(dossier_name, directory=dossier_parent)
    print(SUCCESSFULLY_INIT_DOSSIER)


def check_handler(*args):
    if len(args) > 1:
        print(INCORRECT_USAGE_ERROR)
        return
    cache = get_dossier()
    if not cache:
        print(NOT_VALID_DOSSIER_NOTE)
        return
    dossier_name, dossier_parent = cache
    dossier = Dossier(dossier_name, directory=dossier_parent)
    if len(args) == 1:
        entry = args[0]
        info = dossier.check(entry)
        if not info:
            print(ENTRY_DOESNT_EXIST_NOTE)
            return
        container, filename = info
        size = get_file_size(filename)
        print("'{}' {} {}".format(entry, container, size))
    else:
        info = dossier.check()
        if not info:
            print(EMPTY_DOSSIER_NOTE)
            return
        for entry in sorted(info):
            container, filename = info[entry]
            size = get_file_size(filename)
            print("- '{}' {} {}".format(entry, container, size))


def get_handler(*args):
    if len(args) != 1:
        print(INCORRECT_USAGE_ERROR)
        return
    cache = get_dossier()
    if not cache:
        print(NOT_VALID_DOSSIER_NOTE)
        return
    dossier_name, dossier_parent = cache
    entry_name = args[0]
    dossier = Dossier(dossier_name, directory=dossier_parent)
    #data = dossier.get(entry_name)
    #if data is None:
    #    print(ENTRY_DOESNT_EXIST_NOTE)
    #    return
    info = dossier.check(entry_name)
    if not info:
        print(ENTRY_DOESNT_EXIST_NOTE)
        return
    container, filename = info
    if container == "bin":
        if not os.path.exists(filename):
            print("Missing binary file '{}'".format(filename))
            return
        with open(filename, "rb") as file:
            data = file.read()
            sys.stdout.buffer.write(data)
    else:
        with open(filename, "r") as file:
            data = file.read()
            print(data)


def set_handler(*args):
    if len(args) not in (2, 3):
        print(INCORRECT_USAGE_ERROR)
        return
    cache = get_dossier()
    if not cache:
        print(NOT_VALID_DOSSIER_NOTE)
        return
    dossier_name, dossier_parent = cache
    dossier = Dossier(dossier_name, directory=dossier_parent)
    # update entry with default value accordingly to its container type
    if len(args) == 2:
        entry, container = args
        update_entry_with_default_data(dossier, entry, container)
    else:
        entry, container, source_filename = args
        update_entry_content(dossier, entry, container, source_filename)


def del_handler(*args):
    if len(args) == 0:
        print(INCORRECT_USAGE_ERROR)
        return
    cache = get_dossier()
    if not cache:
        print(NOT_VALID_DOSSIER_NOTE)
        return
    dossier_name, dossier_parent = cache
    dossier = Dossier(dossier_name, directory=dossier_parent)
    dossier.delete(*args)
    cache = "Entry"
    if len(args) > 1:
        cache = "Entries"
    print("{} successfully deleted !".format(cache))


def update_entry_content(dossier, entry, container,
                         source_filename):
    if not os.path.exists(source_filename):
        print("Non existent filename '{}'.".format(source_filename))
        return
    if container not in ("bin", "dict", "list", "set"):
        print("Unknown container type '{}'.".format(container))
        return
    if container in ("dict", "list", "set"):
        try:
            data = json_load(source_filename)
        except Exception as e:
            print("Failed to load the JSON file '{}'.".format(source_filename))
            return
        if container == "set":
            data = set(data)
        dossier.set(entry, data)
    elif container == "bin":
        with open(source_filename, "rb") as file:
            data = file.read()
            dossier.set(entry, data)
    print("Entry successfully updated !")


def update_entry_with_default_data(dossier, entry, container):
    if container not in ("bin", "list", "dict", "set"):
        print("Unknown container type '{}'.".format(container))
        return
    data = None
    if container == "bin":
        data = b""
    elif container == "list":
        data = list()
    elif container == "dict":
        data = dict()
    elif container == "set":
        data = set()
    dossier.set(entry, data)
    print("Entry successfully updated !")


def get_dossier():
    dossier_parent, dossier_name = os.path.split(os.getcwd())
    if valid_dossier(dossier_name, dossier_parent):
        return dossier_name, dossier_parent
    return None


def get_file_size(filename):
    size = os.stat(filename).st_size
    size, unit = convert_size(size)
    return "{}{}".format(int(size), unit)


def main():
    cache = sys.argv[1:]
    if not cache:
        help_handler()
        return
    command = cache[0].lower()
    args = cache[1:]
    handlers = {"init": init_handler,
                "check": check_handler,
                "get": get_handler,
                "set": set_handler,
                "del": del_handler,
                "help": help_handler}
    try:
        handlers[command](*args)
    except KeyError:
        print("Unknown command.")


if __name__ == "__main__":
    main()
