Back to [Modules overview](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md)
  
# Module documentation
>## shared.\_\_main\_\_
No description
<br>
[constants (4)](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared.__main__/constants.md) &nbsp;.&nbsp; [functions (10)](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared.__main__/functions.md)


## Constants
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

