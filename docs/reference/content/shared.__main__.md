
Back to [Reference Overview](https://github.com/pyrustic/shared/blob/master/docs/reference/README.md)

# shared.\_\_main\_\_



<br>


```python
HELP = "
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

"

INCORRECT_USAGE = "Incorrect usage of the command."

```

<br>

```python

def bin_handler(store, *args):
    """
    
    """

```

<br>

```python

def dict_handler(store, *args):
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

def list_handler(store, *args):
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

def set_handler(store, *args):
    """
    
    """

```

