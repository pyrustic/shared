import sys
import os
import os.path
import pprint
from shared import Shared, DEFAULT_LOCATION, legal_store, json_load


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
    Legal types: dict list set bin
    
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
    store = args[0]
    Shared(store, location=os.getcwd())
    print("Successfully created the store '{}' !".format(store))


def del_handler(*args):
    if not args:
        print(MISSING_STORE_NAME_ERROR)
        return
    store = args[0]
    location = shared_location(store)
    if not location:
        return
    shared = Shared(store, location=location)
    shared.delete(*args[1:])
    print("Successfully deleted !")


def store_handler(*args):
    if not args:
        print(MISSING_STORE_NAME_ERROR)
        return
    store = args[0]
    location = shared_location(store)
    if not location:
        return
    shared = Shared(store, location=location)
    n = len(args[1:])
    if n == 0:  # Show store content
        show_store_content(shared, location)
    elif n == 1:  # Show entry content
        entry = args[1]
        show_entry_content(shared, entry)
    elif n == 3:  # Update the content of an entry
        entry, container, source_filename = args[1:]
        update_entry_content(shared, entry, container,
                             source_filename)
    else:
        print(INCORRECT_USAGE_ERROR)


def show_store_content(shared, location):
    if not shared.info:
        print("- Empty store -")
        return
    print("{}".format(location))
    for name, container in shared.info.items():
        print("- {} ({})".format(name, container))


def show_entry_content(shared, entry):
    data = shared.get(entry)
    if data is None:
        print("- This entry doesn't exist -")
        return
    container = shared.info[entry]
    if container == "bin":
        if not os.path.exists(data):
            print("Error: Missing binary file '{}'".format(data))
            return
        with open(data, "rb") as file:
            data = file.read()
            sys.stdout.buffer.write(data)
    else:
        display(data)


def update_entry_content(shared, entry, container,
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
        shared.set(entry, data)
        print("Successfully updated the entry '{}' !".format(entry))
    elif container == "bin":
        with open(source_filename, "rb") as file:
            data = file.read()
            shared.set(entry, data)
        print("Successfully updated the entry '{}' !".format(entry))
    else:
        print("Error: Unknown container type '{}'.".format(container))


def shared_location(store):
    location = os.getcwd()
    store_path = os.path.join(location, store)
    if not legal_store(store_path):
        location = DEFAULT_LOCATION
        store_path = os.path.join(location, store)
        if not legal_store(store_path):
            print("Error: The store '{}' doesn't exist.".format(store))
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

