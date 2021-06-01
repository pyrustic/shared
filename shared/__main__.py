import sys
import os
import os.path
import pprint
from shared import Shared


HELP = """\

Welcome to Shared !

https://github.com/pyrustic/shared


Description
===========

Shared is a Python library to store, expose,
read, and edit collections of data.

This is the command line interface.


Commands
========

Available commands are:
    dict list set bin

    
<store> dict
============

This command prints the content of the dict collection in this store.
You can't edit the content via the command line interface.


<store> list
============

This command prints the content of the list collection in this store.
You can't edit the content via the command line interface.


<store> set
===========

This command prints the content of the set collection in this store.
You can't edit the content via the command line interface.


<store> bin
===========

This command prints information about the collection of binary data in this store.


<store> bin <name> <filename>
=============================

Store the content of filename under a name in this store.

Example:

    "store" bin "icon" "/home/alex/python-icon.png"


<store> bin <name>
==================

Outputs the binary data stored under this name from this store.

Example:

    "store" bin "icon" > "/home/alex/new-icon.png"

"""


INCORRECT_USAGE = "Incorrect usage of the command."


def display(text):
    pp = pprint.PrettyPrinter()
    pp.pprint(text)


def help_handler(*args):
    print(HELP)


def dict_handler(store, *args):
    if args:
        print(INCORRECT_USAGE)
        return
    shared = Shared(store, readonly=True)
    data = shared.dict
    if data:
        display(shared.dict)
    else:
        print("- Empty collection -")


def list_handler(store, *args):
    if args:
        print(INCORRECT_USAGE)
        return
    shared = Shared(store, readonly=True)
    if not shared.exists:
        print("This store doesn't exist !")
        return
    data = shared.list
    if data:
        display(shared.list)
    else:
        print("- Empty collection -")


def set_handler(store, *args):
    if args:
        print(INCORRECT_USAGE)
        return
    shared = Shared(store, readonly=True)
    if not shared.exists:
        print("This store doesn't exist !")
        return
    data = shared.set
    if data:
        display(shared.set)
    else:
        print("- Empty collection -")


def bin_handler(store, *args):
    shared = Shared(store, readonly=True)
    if not args:
        if not shared.exists:
            print("This store doesn't exist !")
            return
        data = shared.bin
        if data:
            display(shared.bin)
        else:
            print("- Empty collection -")
        return
    elif len(args) == 1:  # output binary data stored under a name
        if not shared.exists:
            print("This store doesn't exist !")
            return
        name = args[0]
        path = shared.bin.get(name, None)
        if not path:
            print("This name doesn't exist in the bin collection !")
        elif os.path.exists(path):
            with open(path, "rb") as file:
                data = file.read()
                sys.stdout.buffer.write(data)
        else:
            print("Missing file: {}".format(path))
    elif len(args) == 2:
        shared = Shared(store)
        name = args[0]
        filename = args[1]
        with open(filename, "rb") as file:
            data = file.read()
            shared.add_bin(name, data)
        print("Binary data successfully stored !")
    else:
        print(INCORRECT_USAGE)


def main():
    args = sys.argv[1:]
    if not args or len(args) == 1:
        if not args or (args and args[0] == "help"):
            help_handler()
        else:
            print("* Unknown command - Please type 'help' *")
        return
    store = args[0]
    command = args[1]
    handlers = {"dict": dict_handler,
                "list": list_handler,
                "set": set_handler,
                "bin": bin_handler}
    try:
        handlers[command](store, *args[2:])
    except KeyError:
        print("* Unknown command - Please type 'help' *")


if __name__ == "__main__":
    main()
