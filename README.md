[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI package version](https://img.shields.io/pypi/v/shared)](https://pypi.org/project/shared)
[![Downloads](https://pepy.tech/badge/shared)](https://pepy.tech/project/shared)

<!-- Cover -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/shared/cover.png" alt="Demo" width="541">
    <p align="center">
    <i> </i>
    </p>
</div>



# Rustic Data Sharing
**Data exchange and persistence**

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/shared/tags) . [Modules Documentation](https://github.com/pyrustic/shared/tree/master/docs/modules#readme)

## Table of contents
- [Overview](#overview) 
- [Document](#document) 
- [Dossier](#dossier)
- [Database](#database)
- [Command line interface](#command-line-interface)
- [Installation](#installation) 

# Overview
**Shared** is a Python package created to be the [hacker](https://en.wikipedia.org/wiki/Hacker_culture)'s companion when it comes to storing application data, managing configuration files, caching data, and exchanging data with other programs. This library is the reference implementation of the [Rustic Data Sharing Interface](https://github.com/pyrustic/shared/blob/master/rustic.md).

Although a lightweight package, **Shared** smoothly handles collections (**dict**, **list**, **set**), **binary** data, and **SQL** queries.

**Shared**'s application programming interface is designed for intuitive use. Thus, three classes with similar interfaces are created to cover the needs of data exchange and persistence: `Document`, `Dossier`, and `Database`.

|Class|Relevance|
|---|---|
|`Document`|For individual access to [Jesth](https://github.com/pyrustic/jesth#readme) and [JSON](https://en.wikipedia.org/wiki/JSON) files that are likely to be **manually edited by a human**.|
|`Dossier`|To store collections and binary data in a dossier **without worrying about how they are actually saved**.|
|`Database`|For an intuitive interaction with [SQLite](https://www.sqlite.org) **databases**.|


All three classes emphasize **initialization**:
- `Document` and `Dossier` give the possibility to define **default data**.
- `Database` allows the definition of an **initialization SQL script** which is only executed to create a new database.

Among the three classes, `Dossier` is the class of which a single instance can handle multiple underlying files. The `Dossier` class has its own protocol for organizing data. For this reason, `Dossier` offers a simple yet powerful **command-line interface** that allows other programs or a human to read and write the contents of a dossier.

`Document` and `Dossier` provide **Autosave** functionality, while `Database` automatically closes the underlying database connection when the user closes the application.

All three classes provide **read-only** access to data and also allow the creation of **temporary data** which is automatically deleted when the user closes the application.

Let's explore the [Document](#document), [Dossier](#dossier), and [Database](#database) classes in the next sections !

# Document

The `Document` class represents an interface for reading and writing an underlying file whose format is either [Jesth](https://github.com/pyrustic/jesth#readme) or [JSON](https://en.wikipedia.org/wiki/JSON). Accessing a document or creating a new one is as simple as this:

```python
from shared import Document


# Create a new document instance which will be linked to the 'my-data.json' file.
# If this file doesn't exist yet, it will be automatically created
document = Document("my-data.json")

# From now, we can use 'document' to read and write the contents of 'my-data.json' !
# ...
```

The string `my-data.json` is the base name of a file that will be created if it does not yet exist. This string is called **Target** and can be an absolute path or an instance of [pathlib.Path](https://docs.python.org/3/library/pathlib.html). The `Document` class exposes the `read` and `write` methods, respectively, to read and write the underlying document.

By default, the underlying document will be considered as a JSON file if its extension is `.json`, otherwise it will be considered as a [Jesth](https://github.com/pyrustic/jesth#readme) file. The default behaviour can be changed by setting the `file_format` parameter which accepts the strings `json` or `jesth`.

## Initialization
A `document` can be initialized with a conditional statement or by defining default data. By default, the `Document` class will assign a `dict` to the null parameter `default_data`.

### Use a conditional statement
It's as simple as testing a boolean to check if the underlying document file is newly created or not:

```python
from shared import Document


# access 'my-data.json'
document = Document("my-data.json")

# let's initialize the content of 'my-data.json'
if document.new:
    data = {"name": "alex", "job": "evangelist"}
    document.write(data)  # persisted !
```

### Set default data
The most elegant, least detailed and recommended way to initialize a document is to set some default data:

```python
from shared import Document

# default data to init the file 'my-data.json'
DEFAULT_DATA = {"name": "alex", "job": "evangelist"}

# access 'my-data.json'
document = Document("my-data.json", default=DEFAULT_DATA)

# From now, thanks to the initialization functionality, the underlying
# document contains the default data, assuming that 'my-data.json'
# did not exist before the `Document` class was instantiated
```

## Data location
The only mandatory argument to be supplied to the `Document` class constructor is the `target`. For convenience, the `target` is either the absolute path or the base name of a file. Its data type is either a string or an instance of [pathlib.Path](https://docs.python.org/3/library/pathlib.html).

The optional `directory` parameter exists to supplement the `target` value, assuming that value is not an absolute path.

### Default directory
By default, document files are saved in `$HOME/PyrusticHome/shared`. You can change the location according to your needs:

```python
from shared import Document

DIRECTORY = "/home/alex/private"

# access 'my-data.json'
document = Document("my-data.json", directory=DIRECTORY)

# From now, you can access these properties:
#   document.name == "my-data.json"
#   document.directory == "/home/alex/private"
#   document.target == "my-data.json"

```

### Absolute pathname
You can set an absolute path as the target. In this case, the `Document` class ignores the `directory` parameter.

```python
from shared import Document

pathname = "/home/alex/private/my-data.json"

# access 'my-data.json'
document = Document(pathname)

# From now, you can access these properties:
#   document.name == "my-data.json"
#   document.directory == "/home/alex/private"
#   document.target == "/home/alex/private/my-data.json"
```

### Temporary data
Setting a boolean can enable temporary mode, so a document can only be created and used while the application is running, and then safely deleted when the application closes:

```python
from shared import Document


# access 'my-data.json'
document = Document("my-data.json", temporary=True)

# This document will be created in a temporary directory
# then it will be safely deleted when the application closes
# or when the developer explicitly calls the 'close' or 'delete' method
```

The `Document` class uses [tempfile.TemporaryDirectory](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory) to implement this functionality.


## Autosave
Thanks to [atexit](https://docs.python.org/3/library/atexit.html) module, `Document` can autosave content when the application is closed:

```python
import sys
from shared import Document


# access 'my-config.json' with `autosave` mode enabled
document = Document("my-config.json", autosave=True, default=[])
# load the data
data = document.read()

# few lines of code later...

data.append("batman")  # data modified

sys.exit()  # data automatically saved !
```
Along with `atexit` module, the `Document` class also uses a caching mechanism to implement the `autosave` functionality.

## Caching
By default, `caching` mode is enabled, so the user can access cached data through the `cache` property of an instance of the `Document` class:

```python
from shared import Document

DEFAULT_DATA = {"name": "alex", "job": "evangelist"}

# access 'my-config.json'
document = Document("my-config.json", caching=True, default=DEFAULT_DATA)

data = document.read()

if data is document.cache:
    print("Same same !")
```

## Readonly
Setting the `readonly` parameter to `True` prevents the current application from accidentally modifying the content of a document:

```python
from shared import Document


# access 'my-data.json'
document = Document("my-data.json", readonly=True)

# when you set readonly to True, you can no longer edit the content !
# shared.ReadonlyError will be raised if you try to mess with a readonly document

```

## Clear data
You can delete the underlying file of a document (assuming the file isn't in readonly mode):

```python
from shared import Document


# access 'my-data.json'
document = Document("my-data.json")

# delete 'my-data.json'
document.delete()

if document.deleted:
    print("Successfully deleted !")
```

## Convenience functions
Four convenience functions are available for the `Document` class:

```python
from shared import create, readonly, write, autosave

# quickly create a document
create("my-data.json")

# quickly open a document in readonly mode
data = readonly("my-data.json", )

# quicky change the content of a document
data = ["moon", "sun"]
write("my-data.json", data)

# quickly read the content of a document in autosave mode
default = ["red", "green"]
data = autosave("my-data.json", default=default)
data.append("blue")  # data will be automatically saved on exit
```

## Conclusion
For individual access to [Jesth](https://github.com/pyrustic/jesth#readme) and [JSON](https://en.wikipedia.org/wiki/JSON) files that are likely to be **manually edited by a human**, the `Document` class is the recommended interface.

For more technical details about this class, read its [reference documentation](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document).

# Dossier
The `Dossier` class stores collections (`list`, `dict`, `set`) and `binary data` with a unified interface inside a [dossier](https://dictionary.cambridge.org/dictionary/english/dossier). The `Shared` library allows to read and write a dossier not only programmatically but also from the [command line](#command-line-interface).

This class shares a similar interface with the `Document` class. Thus, the `Dossier` class constructor has `target`, `directory`, `autosave`, `readonly` and `temporary` as parameters. These elements are already covered in the [Document](#document) class section.

Under the hood, `Dossier` uses [files](https://en.wikipedia.org/wiki/Computer_file) and [JSON](https://en.wikipedia.org/wiki/JSON) to store data.

## Example
Let's create data in **script_1.py**:

```python
# script_1.py
from shared import Dossier

# data
people = {"Jack": "male", "Jane": "female"}  # dict
planets = ["Mars", "Venus", "Jupiter"]  # list
colors = {"red", "green", "blue"}  # set

# let's persist the data in 'my-dossier'
dossier = Dossier("my-dossier")
dossier.set("people", people)  # set the 'people' entry
dossier.set("planets", planets)  # set the 'planets' entry
dossier.set("colors", colors)  # set the 'colors' entry

# Done ! The data is persisted !
```

From **script_2.py**, let's access the data created by **script_1.py**:
```python
# script_2.py
from shared import Dossier

# let's access the shared dossier
dossier = Dossier("my-dossier")

# get data from the shared dossier
people = dossier.get("people") # get the 'people' entry
planets = dossier.get("planets") # get the 'planets' entry'
colors = dossier.get("colors") # get the 'colors' entry

print(people)
# output: {'Jack': 'male', 'Jane': 'female'}

print(planets)
# output: ['Mars', 'Venus', 'Jupiter']

print(set(colors)) # there is nothing called 'set' in JSON [1]
# output: {'red', 'green', 'blue'}


# [1] the value of 'colors' is this dictionary:
# {'red': None, 'green': None, 'blue': None}
```

## Binary data
You can store binary data with the same unified interface:

```python
# script_1.py
from shared import Dossier

dossier = Dossier("my-dossier")

with open("/home/alex/selfie.png", "rb") as file:
    data = file.read()
    dossier.set("selfie", data)  # set the 'selfie' entry

# the 'set' method returns the path to the binary file that stores the binary entry
```

The above code can also be expressed like this:

```python
# script_1.py
import pathlib
from shared import Dossier

dossier = Dossier("my-dossier")

path = pathlib.Path("/home/alex/selfie.png")
dossier.set("selfie", path)  # set the 'selfie' entry

# the 'set' method returns the path to the binary file that stores the binary entry
```

You can retrieve your binary data from another script:
```python
# script_2.py
from shared import Dossier
from shutil import copyfile

dossier = Dossier("my-dossier")
source_path = dossier.get("selfie")  # get the filename of the 'selfie' bin entry
destination_path = "/home/alex/new.png"

# copy the content from source to destination
copyfile(source_path, destination_path)

```

## Check
Use the `check` method to check the contents of a dossier or a specific entry:

```python
from shared import Dossier

dossier = Dossier("my-dossier")

# check a specific entry
info = dossier.check("entry")
if info:
    # info is a 2-tuple (container, filename)
    # the container is a string that represents the type of the entry
    # containers: "dict", "list", "set", and "bin"
    # The filename is either the path to a JSON file or a binary file
    container, filename = info

# check the contents of the dossier
dossier_info = dossier.check()  # returns a dict, keys are entries and values are 2-tuples

for entry, info in dossier_info.items():
    print("Entry:", info.name) # the entry name
    print("Container:", info.container)  # 'dict', 'set', 'list', or 'bin'
    print("Filename:", info.filename) # the underlying file in which the data is stored
    print()
```


## Clear data
You can decide to delete a specific entry, a group of entries, or the dossier:

```python
from shared import Dossier

dossier = Dossier("my-dossier")

# delete a specific entry
dossier.delete("entry_1")

# delete a group of entries
dossier.delete("entry_2", "entry_3")

# delete the dossier
dossier.delete()  # collections, binary data, and meta data are gone
```

## Conclusion
To store collections and binary data in a dossier **without worrying about how they are actually saved**, the `Document` class is the interface to use.

For more technical details about this class, read its [documentation](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier).

# Database
Intuitive interaction with **SQLite** databases.

## Example
The following example shows how nice it is to work with the `Database` class:

```python
from shared import Database

# Initialization script
# This SQL script will create two tables: friends and projects
INIT_SCRIPT = """\
CREATE TABLE friends (name TEXT PRIMARY KEY,
                      age INTEGER NOT NULL);

CREATE TABLE projects (name TEXT PRIMARY KEY,
                       language TEXT NOT NULL);
"""

# If this database doesn't exist yet,
# it will be created with the initialization script
database = Database("my-database", init_script=INIT_SCRIPT)

# This will only be executed once !
# So you can safely restart this script again and again...
if database.new:
    # Write data to this database
    sql = """INSERT INTO friends VALUES ("Jack", 20)"""
    database.edit(sql)

    # few lines of code later...

    # Write data to this database
    sql = """INSERT INTO friends VALUES (?, ?)"""
    database.edit(sql, param=("Jane", 21))

# Read data
sql = "SELECT * FROM friends"
columns, data = database.query(sql)

print(columns)
# output: ['name', 'age']

print(data)
# output: [('Jack', 20), ('Jane', 21)]

```

For more technical details about this class, read its [documentation](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database).


# Command line interface
**Shared** comes with an intuitive command line interface for **Dossier** class. Type `help` in the command line interface to display a short manual.

For the next subsections, suppose we have a non-empty dossier named `my-dossier` located in `/home/alex/dossiers`. 

## Check the content
Check the contents of `my-dossier` or a specific entry:
```bash
$ cd /home/alex/dossiers/my-dossier

$ shared check
- 'colors' set 56B
- 'people' dict 44B
- 'planets' list 42B

$ shared check people
'people' dict 44B

$ shared check colors
'colors' set 56B
```

## Read the content of a specific entry

```bash
$ cd /home/alex/dossiers/my-dossier

$ shared get people
{
    "Jack": "male",
    "Jane": "female"
}

$ shared get planets
[
    "Mars",
    "Venus",
    "Jupiter"
]

shared get colors
{
    "red": null,
    "blue": null,
    "green": null
}

```
The output text is the exact JSON representation as stored in a file. So the **output can be consumed as is** by another program and deserialized with a JSON library. Note that the `colors` entry is a `set` but represented as a `dict` in JSON.

## Store binary data
```bash
$ shared set selfie bin: "/home/alex/selfie.png"
Entry successfully updated !
```

You can copy a binary entry into an arbitrary file from the command line:

```bash
$ shared get selfie > "/home/alex/selfie-copy.png"
```

## Store a collection
```bash
$ shared set countries list: "/home/alex/countries.json"
Entry successfully updated !

$ shared set my_config dict: "/home/alex/app_config.json"
Entry successfully updated !
```

## Delete an entry

```bash
$ shared del "selfie"
Entry successfully deleted !

$ shared check selfie
This entry doesn't exist.
```

## Delete a dossier
Right-click on the folder with your mouse, then send it safely to the trash ;)


# Installation
**Shared** is **cross platform** and versions under **1.0.0** will be considered **Beta** at best. It is built on [Ubuntu](https://ubuntu.com/download/desktop) with [Python 3.8](https://www.python.org/downloads/) and should work on **Python 3.5** or **newer**.

## For the first time

```bash
$ pip install shared
```

## Upgrade
```bash
$ pip install shared --upgrade --upgrade-strategy eager

```


<br>
<br>
<br>

[Back to top](#readme)
