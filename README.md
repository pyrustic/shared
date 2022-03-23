# Pyrustic Shared Data
**Data exchange and persistence**

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/shared/tags) . [Modules Documentation](https://github.com/pyrustic/shared/tree/master/docs/modules#readme)

## Table of contents
- [Overview](#overview) 
- [Document](#document) 
- [Dossier](#dossier)
- [Database](#database)
- [Temporary data](#temporary-data)
- [Autosave feature](#autosave-feature)
- [Command line interface](#command-line-interface)
- [Implementations](#implementations)
- [Installation](#installation) 

# Overview
**Shared** is a Python package created to be a developer's companion when it comes to managing configuration files, storing application data, caching data, and exchanging data with other programs.

Although a lightweight package, **Shared** smoothly handles collections (**dict**, **list**, **set**), **binary** data, and **SQL** queries.

**Shared**'s application programming interface is designed for intuitive use. Thus, the expression of solutions to data exchange and persistence needs manifests in three classes: `Document`, `Dossier`, and `Database`.

- **Document:** for individual access to [hackernotes](https://github.com/pyrustic/hackernote#readme) and [JSON](https://en.wikipedia.org/wiki/JSON) files that are likely to be **manually edited by a human**;
- **Dossier:** to store collections and binary data **without worrying about how they are actually saved**;
- **Database:** for an intuitive interaction with [SQLite](https://www.sqlite.org) **databases**.


[Gaspium](https://github.com/pyrustic/gaspium), the framework for building Python apps with the [GASP](https://github.com/pyrustic/gaspium/blob/master/gasp.md) metaphor, includes the **Shared** package as the default solution for data exchange and persistence.

# Document
With the **Document** class, you can handle data in **Hackernote** or **JSON** format. The following examples will focus on **JSON** since it is well known. For more about hackernotes, visit the [Hackernote](https://github.com/pyrustic/hackernote#readme) project.

> **Read the class [documentation](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document)**

## Example

```python
from shared import Document


# Create a new document instance which will be linked to the 'my-data.json' file.
# If this file doesn't exist yet, it will be automatically created
document = Document("my-data.json")

# From now, we can use 'document' to read and write the contents of 'my-data.json' !
# ...
```
By default, the `file_format` argument of the constructor is set to `auto`, i.e. the document will be considered as a JSON file if its extension is `.json`, otherwise it will be considered as a hackernote. Other values for the `file_format` argument are: `hackernote` and `json`.


## Initialization
It's as simple as testing a boolean to check if the underlying document file is newly created or not:

```python
from shared import Document


# access 'my-data.json'
document = Document("my-data.json")

# let's initialize the content of 'my-data.json'
if document.new:
    data = {"name": "alex", "job": "evangelist"}
    document.set(data)  # persisted !
```

## Default data
You can automatically initialize a document with default data:

```python
from shared import Document

# default data to init the file 'my-data.json'
DEFAULT_DATA = {"name": "alex", "job": "evangelist"}

# access 'my-data.json'
document = Document("my-data.json", default=DEFAULT_DATA)

# Done !
```

## Data location
By default, document files are saved in `$HOME/PyrusticHome/shared`. You can change the location to fit your needs:

```python
from shared import Document

DIRECTORY = "/home/alex/private"

# access 'my-data.json'
document = Document("my-data.json", directory=DIRECTORY)

```

## Autosave
Thanks to [probed](https://github.com/pyrustic/probed) collections, you can tell **Document** to autosave when the contents of a collection change:

```python
from shared import Document


# access 'my-config.json' with `autosave` mode enabled
document = Document("my-config.json", autosave=True, default=[])
# load the data
data = document.get()  # returns a probed list

# few lines of code later...

data.append("batman")  # automatically saved !
```

When the `autosave` mode is enabled, the data is converted into a **probed** collection. In the example above, the `get` method returns a **probed** list.

**Probed** is a Python library that gives full control over collections (`list`, `dict`, `set`), such as being notified when their contents change or filtering what is added to them.

> **Discover [Probed](https://github.com/pyrustic/probed#readme) !**

## Caching
By default, `caching` mode is enabled, i.e. you can access cached data through the `cache` property of a **Document** instance:

```python
from shared import Document

DEFAULT_DATA = {"name": "alex", "job": "evangelist"}

# access 'my-config.json'
document = Document("my-config.json", caching=True, default=DEFAULT_DATA)

data = document.get()  # returns a probed dict

if data is document.cache:
    print("Same same !")
```

## Readonly
Sometimes you need to access a document file with the guarantee that its contents will not be modified by your own code:

```python
from shared import Document


# access 'my-data.json'
document = Document("my-data.json", readonly=True)

# when you set readonly to True, you can no longer edit the content !
# shared.ReadonlyError will be raised if you try to mess with a readonly document

```

## Clear data
You can delete the underlying file of a document (assuming that the file isn't accessed in readonly mode):

```python
from shared import Document


# access 'my-data.json'
document = Document("my-data.json")

# delete 'my-data.json'
document.delete()

if document.deleted:
    print("Successfully deleted !")
```

# Dossier
A [dossier](https://dictionary.cambridge.org/dictionary/english/dossier) stores collections (`list`, `dict`, `set`) and `binary data` with a unified interface. You can read and write a dossier not only programmatically but also from the **command line**.

Under the hood, **Dossier** uses [files](https://en.wikipedia.org/wiki/Computer_file) and [JSON](https://en.wikipedia.org/wiki/JSON).

> **Read the class [documentation](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier)**

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

print(colors)
# output: {'red', 'green', 'blue'}

```

## Data location
By default, the dossier is created in `$HOME/PyrusticHome/shared`. You can change the location to fit your needs:
```python
from shared import Dossier

DIRECTORY = "/home/alex/private/dossiers"

# access 'my-dossier'
dossier = Dossier("my-dossier", directory=DIRECTORY)
```

## Autosave
Thanks to [probed](https://github.com/pyrustic/probed) collections, you can tell **Dossier** to autosave when the contents of a collection change:

```python
from shared import Dossier

# access 'my-dossier' with autosave set to True
# thus, shared collections will be automatically persisted
dossier = Dossier("my-dossier", autosave=True)

# get the 'people' entry previously stored as {'Jack': 'male', 'Jane': 'female'}
people = dossier.get("people")  # returns a probed dict

# update the contents of people
people["Janet"] = "female"  # automatically saved !

# set a new entry
data = ["alpha", 42, True]
new_entry = dossier.set("new_entry", data)  # returns a probed list

# update the contents of new_entry
new_entry.append(3.14)  # persisted !

```

## Readonly
Sometimes you need to access a dossier with the guarantee that its contents will not be modified by your own code:
```python
from shared import Dossier


# access 'my-dossier'
dossier = Dossier("my-dossier", readonly=True)

# when you set readonly to True, you can't anymore edit the contents !
# you can only use the 'get' method of the dossier, not anymore the 'set' method, nor autosave.
# shared.ReadonlyError will be raised if you try to mess with a readonly dossier

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
    container, filename = info
    print("Entry:", entry)
    print("Container:", container)
    print("Filename:", filename)
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

# Database
Intuitive interaction with **SQLite** databases.

> **Read the class [documentation](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database)**

## Example
The following example shows how nice it is to work with the **Database** class:

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

# Temporary data
The constructors of all three classes have a `directory` parameter. For the **Document** and **Dossier** classes, if you set `None` as the `directory` argument, the underlying file will be created in a **temporary directory** which will be automatically deleted at the end of use. The **Database** class will not create a temporary directory but will store the database in [memory](https://www.sqlite.org/inmemorydb.html).


# Autosave feature
When the `autosave` mode is enabled, **Document** and **Dossier** uses **Probed** to create and return `probed collections`.

**Probed** is a Python library that gives full control over collections (`list`, `dict`, `set`), such as being notified when their contents change or filtering what is added to them.

The obvious mapping between Python collections and Probed collections:

| Python collections | Probed collections |
|--------------------|--------------------|
| dict               | probed.ProbedDict  |
| list               | probed.ProbedList  |
| set                | probed.ProbedSet   |


> **Discover [Probed](https://github.com/pyrustic/probed#readme) !**

# Command line interface
**Shared** comes with an intuitive command line interface for **Dossier** class. Type `help` in the command line interface to display a short manual.

For the next subsections, suppose we have a non-empty dossier named `my-dossier` located in `/home/alex/dossiers`. 

## Check the content
Check the contents of `my-dossier` or a specific entry:
```bash
$ cd /home/alex/dossiers/my-dossier

$ shared check
- 'colors' set 42B
- 'people' dict 34B
- 'planets' list 28B

$ shared check people
'people' dict 34B

$ shared check colors
'colors' set 42B
```

## Read the content of a specific entry

```bash
$ cd /home/alex/dossiers/my-dossier

$ shared get people
{'Jack': 'male', 'Jane': 'female'}

$ shared get planets
['Mars', 'Venus', 'Jupiter']

shared get colors
{"red": null, "green": null, "blue": null}
```
The output text is the exact JSON representation as stored in a file. So the **output can be consumed as is** by another program and deserialized with a JSON library. Note that the `colors` entry is a `set` but represented as a `dict` in JSON.

## Store binary data
```bash
$ shared set selfie bin "/home/alex/selfie.png"
Entry successfully updated !
```

You can copy a binary entry into an arbitrary file from the command line:

```bash
$ shared get selfie > "/home/alex/selfie-copy.png"
```

## Store a collection
```bash
$ shared set countries list "/home/alex/countries.json"
Entry successfully updated !

$ shared set my_config dict "/home/alex/app_config.json"
Entry successfully updated !
```

## Delete an entry

```bash
$ shared del "selfie"
Entry successfully deleted !
```

## Delete a dossier
Right-click on the folder with your mouse, then send it safely to the trash ;)

# Implementations
This is the **reference** implementation of the **Pyrustic Shared Data** written in **Python**. 

_Do you want to implement this in another programming language ?_ Let me know ;)

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
