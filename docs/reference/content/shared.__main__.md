
Back to [Reference Overview](https://github.com/pyrustic/shared/blob/master/docs/reference/README.md#readme)

# shared.\_\_main\_\_



<br>


```python
DEFAULT_LOCATION = "/home/alex/PyrusticData/shared"

HELP = "
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

"

INCORRECT_USAGE_ERROR = "Error: Incorrect usage of the command."

MISSING_STORE_NAME_ERROR = "Error: Missing store name."

```

<br>

```python

def del_handler(*args):
    """
    
    """

```

<br>

```python

def display(text):
    """
    
    """

```

<br>

```python

def help_handler(*args):
    """
    
    """

```

<br>

```python

def main():
    """
    
    """

```

<br>

```python

def new_handler(*args):
    """
    
    """

```

<br>

```python

def show_entry_content(store, entry):
    """
    
    """

```

<br>

```python

def show_store_content(store, location):
    """
    
    """

```

<br>

```python

def store_handler(*args):
    """
    
    """

```

<br>

```python

def store_location(store_name):
    """
    
    """

```

<br>

```python

def update_entry_content(store, entry, container, source_filename):
    """
    
    """

```

