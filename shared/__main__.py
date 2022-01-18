"""Command line interface"""
import sys
import os
import os.path
import pprint
from shared import Store, DEFAULT_LOCATION, valid_store, json_load


HELP = """\

Welcome to Shared !
https://github.com/pyrustic/shared

Shared is part of the Pyrustic Open Ecosystem
https://pyrustic.github.io


Description
===========
Shared is a Python library to store, expose,
read, and edit collections of data.

This is the command line interface.


Commands
========
There are 3 commands available:

    new del store


Create a new store
==================
The command 'new' creates a new store in the
current working directory.

    Create the store
    ================
    new <store-name>


Delete a store
==============
The command 'del' deletes the store located in
the current working directory or a specific entry.

    Delete the store
    ================
    del <store-name>
    
    Delete a specific entry
    =======================
    del <store-name> <entry-name>
    
    Delete multiple entries
    =======================
    del <store-name> <entry-name> <entry-name> ...


Read and write
==============
The command 'store' allows you to access the store
located in the current working directory.
If the store isn't in the current working directory,
the program will fall back to the default directory 
'~/PyrusticData/shared'.

    Content of the store
    ====================
    store <store-name>
    
    Content of an entry
    ===================
    store <store-name> <entry-name>
    
    Update the content of an entry
    ==============================
    store <store-name> <entry-name> <type> <new-content-filename>
    Valid types: dict list set bin
    
    Copy the content of an entry
    ============================
    store <store-name> <entry-name> > <destination-filename>

"""

INCORRECT_USAGE_ERROR = "Error: Incorrect usage of the command."
MISSING_STORE_NAME_ERROR = "Error: Missing store name."


def display(text):
    pp = pprint.PrettyPrinter()
    pp.pprint(text)


def help_handler(*args):
    print(HELP)


def new_handler(*args):
    if not args:
        print(MISSING_STORE_NAME_ERROR)
        return
    if len(args) > 1:
        print(INCORRECT_USAGE_ERROR)
        return
    store_name = args[0]
    Store(store_name, location=os.getcwd())
    print("Successfully created the store '{}' !".format(store_name))


def del_handler(*args):
    if not args:
        print(MISSING_STORE_NAME_ERROR)
        return
    store_name = args[0]
    location = store_location(store_name)
    if not location:
        return
    store = Store(store_name, location=location)
    store.delete(*args[1:])
    print("Successfully deleted !")


def store_handler(*args):
    if not args:
        print(MISSING_STORE_NAME_ERROR)
        return
    store_name = args[0]
    location = store_location(store_name)
    if not location:
        return
    store = Store(store_name, location=location)
    n = len(args[1:])
    if n == 0:  # Show store content
        show_store_content(store, location)
    elif n == 1:  # Show entry content
        entry = args[1]
        show_entry_content(store, entry)
    elif n == 3:  # Update the content of an entry
        entry, container, source_filename = args[1:]
        update_entry_content(store, entry, container,
                             source_filename)
    else:
        print(INCORRECT_USAGE_ERROR)


def show_store_content(store, location):
    if not store.info:
        print("- Empty store -")
        return
    print("{}".format(location))
    for name, container in store.info.items():
        print("- {} ({})".format(name, container))


def show_entry_content(store, entry):
    data = store.get(entry)
    if data is None:
        print("- This entry doesn't exist -")
        return
    container = store.info[entry]
    if container == "bin":
        if not os.path.exists(data):
            print("Error: Missing binary file '{}'".format(data))
            return
        with open(data, "rb") as file:
            data = file.read()
            sys.stdout.buffer.write(data)
    else:
        display(data)


def update_entry_content(store, entry, container,
                         source_filename):
    if not os.path.exists(source_filename):
        print("Error: Non existent filename '{}'.".format(source_filename))
        return
    if container in ("dict", "list", "set"):
        try:
            data = json_load(source_filename)
        except Exception as e:
            print("Failed to load the JSON file '{}'.".format(source_filename))
            return
        if container == "set":
            data = set(data)
        store.set(entry, data)
        print("Successfully updated the entry '{}' !".format(entry))
    elif container == "bin":
        with open(source_filename, "rb") as file:
            data = file.read()
            store.set(entry, data)
        print("Successfully updated the entry '{}' !".format(entry))
    else:
        print("Error: Unknown container type '{}'.".format(container))


def store_location(store_name):
    location = os.getcwd()
    store_path = os.path.join(location, store_name)
    if not valid_store(store_path):
        location = DEFAULT_LOCATION
        store_path = os.path.join(location, store_name)
        if not valid_store(store_path):
            print("Error: The store '{}' doesn't exist.".format(store_name))
            location = None
    return location


def main():
    cache = sys.argv[1:]
    if not cache:
        help_handler()
        return
    command = cache[0].lower()
    args = cache[1:]
    handlers = {"new": new_handler,
                "del": del_handler,
                "store": store_handler,
                "help": help_handler}
    try:
        handlers[command](*args)
    except KeyError:
        print("* Unknown command - Type 'help' *")


if __name__ == "__main__":
    main()
