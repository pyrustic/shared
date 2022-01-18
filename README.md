# Shared
**Smooth way to store, share, and edit data (collections and binary).**

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/shared/tags) . [Modules Documentation](https://github.com/pyrustic/shared/tree/master/docs/modules#readme)

## Table of contents
- [Overview](#overview) 
- [Jason](#jason) 
- [Store](#store)
- [Shared collections](shared-collections)
- [Installation](#installation) 

# Overview
**Shared** contains two main classes: `Jason` and `Store`.

| Class  | Description | Relevance |
|--------|-------------|-----------|
| `Jason` | allows individual access to `JSON` files that are likely to be **manually edited by a human** | relevant for managing configuration files |
| `Store` | allows you to store collections of data **without worrying about how they are actually saved** | relevant for application data storage and persistent data caching |

**Shared** is included in [Gaspium](https://github.com/pyrustic/gaspium), the high-productivity framework to build Python apps.

# Jason
Under the hood, **Jason** uses the [JSON](https://en.wikipedia.org/wiki/JSON) format to store data.

```python
from shared import Jason


# Create a new jason instance that will be tied to the file 'my-data.json'.
# If this file doesn't exist yet, it will be automatically created
jason = Jason("my-data.json")

# From now, we can use jason to read and write the contents of 'my-data.json' !
# ...
```

## Initialization
It's as easy as testing a boolean to see if your JSON file is newly created or not:

```python
from shared import Jason


# access 'my-data.json'
jason = Jason("my-data.json")

# let's initialize the content of 'my-data.json'
if jason.new:
    jason.data = {"name": "alex", "job": "angelist"}
    # oops I have been distracted by the woman in red !
    jason.data["job"] = "evangelist"
    # now let's save the contents of jason.data to the underlying JSON file
    jason.save()  # persisted !
```


## Default data
**Jason** comes with a feature to automatically initialize a file with default data:

```python
from shared import Jason

# default data to init the file 'my-data.json'
DEFAULT_DATA = {"name": "alex", "job": "evangelist"}

# access 'my-data.json'
jason = Jason("my-data.json", default=DEFAULT_DATA)

# Done !

```

## Data location
By default, the `JSON` files are saved in `$HOME/PyrusticData/shared`. You can change the location to fit your needs:

```python
from shared import Jason

LOCATION = "/home/alex/private"

# access 'my-data.json'
jason = Jason("my-data.json", location=LOCATION)

```

## Autosave
Thanks to [probed](https://github.com/pyrustic/probed) collections, you can tell **Jason** to autosave when the contents of a collection change:

```python
from shared import Jason


# access 'my-config.json'
jason = Jason("my-config.json", autosave=True, default=[])

# when you set autosave to True, you don't anymore need
# to call the method .save() !

jason.data.append("batman")  # persisted ! yeah yeah !
```

`shared.SharedList`, `shared.SharedDict`, and `shared.SharedSet` are based on `probed.ProbedList`, `probed.ProbedDict`, and `probed.ProbedSet` respectively. If you want to have full control over your collections in your projects, such as being notified when their contents change or filtering what is added to them, check [probed](https://github.com/pyrustic/probed) !

## Readonly
Sometimes you need to access a JSON file with the guarantee that its contents will not be modified by your own code:

```python
from shared import Jason


# access 'my-data.json'
jason = Jason("my-data.json", readonly=True)

# when you set readonly to True, you can't anymore edit the content !
# shared.ReadonlyError will be raised if you try to mess with a readonly jason

```

## Clear data
You can delete a JSON file (assuming that the file isn't accessed in readonly mode):
```python
from shared import Jason


# access 'my-data.json'
jason = Jason("my-data.json")

# delete "my-data.json"
jason.delete()

print(jason.deleted)  # output: True

```

# Store
Under the hood, **Store** uses the [JSON](https://en.wikipedia.org/wiki/JSON) and binary files.

Let's create data in **script_1.py**:

```python
# script_1.py
from shared import Store

# data
people = {"Jack": "male", "Jane": "female"}  # dict
planets = ["Mars", "Venus", "Jupiter"]  # list
colors = {"red", "green", "blue"}  # set

# let's persist the data in the store 'my-store'
store = Store("my-store")
store.set("people", people)  # set the entry 'people'
store.set("planets", planets)  # set the entry 'planets'
store.set("colors", colors)  # set the entry 'colors'

# Done ! The data is persisted !
```

From **script_2.py** let's access the data created by **script_1.py**:
```python
# script_2.py
from shared import Store

# let's open the shared store in readonly mode
store = Store("my-store")

# get data from the shared store 'my-store'
people = store.get("people") # get the entry 'people'
planets = store.get("planets") # get the entry 'planets'
colors = store.get("colors") # get the entry 'colors'

print(people)
# output: {'Jack': 'male', 'Jane': 'female'}

print(planets)
# output: ['Mars', 'Venus', 'Jupiter']

print(colors)
# output: {'red', 'green', 'blue'}

```

## Data location
By default, the data is saved in `$HOME/PyrusticData/shared`. You can change the location to fit your needs:
```python
from shared import Store

LOCATION = "/home/alex/private/stores"

# access 'my-store'
store = Store("my-store", location=LOCATION)
```

## Autosave
Thanks to [probed](https://github.com/pyrustic/probed) collections, you can tell **Store** to autosave when the contents of a collection change:

```python
from shared import Store

# access 'my-store' with autosave set to True
# so shared collections will be automatically persisted
store = Store("my-store", autosave=True)

# get the entry 'people' previously stored as {'Jack': 'male', 'Jane': 'female'}
people = store.get("people")  # the value returned is a 'shared.SharedDict'

# update the contents of people
people["Janet"] = "female"  # persisted !

# set a new entry
new_entry = store.set("new_entry", ["alpha", 42, True])  # the value returned is a 'shared.SharedList

# update the contents of new_entry
new_entry.append(3.14)  # persisted !

```

## Readonly
Sometimes you need to access a store with the guarantee that its contents will not be modified by your own code:
```python
from shared import Store


# access 'my-store'
store = Store("my-store", readonly=True)

# when you set readonly to True, you can't anymore edit the contents !
# you can only use the 'get' method of the store, not anymore the 'set' method, nor autosave.
# shared.ReadonlyError will be raised if you try to mess with a readonly jason

```

## Binary data
You can store binary data with in your store :

```python
# script_1.py
from shared import Store

store = Store("my-store")

with open("/home/alex/selfie.png", "rb") as file:
    data = file.read()
    store.set("selfie", data)  # set the entry 'selfie'

# the method 'set' returns the path to the binary file that stores the binary entry
```

You can retrieve your binary data from another script:
```python
# script_2.py
from shared import Store
from shutil import copyfile

store = Store("my-store")
source_path = store.get("selfie")  # get the bin entry 'selfie'
destination_path = "/home/alex/new.png"

# copy the content from source to destination
copyfile(source_path, destination_path)

```

## Clear data
You can decide to delete a store:

```python
from shared import Store

store = Store("my-store")
store.delete()  # data collections, binary data, and meta data are gone
```


## Command line interface
**Shared** comes with an easy-to-use command line interface for the class **Store**. Type `help` in the command line interface to display a short manual.

Let assume that we got a store named `my-store` which contains data:

```bash
$ shared store "my-store" "planets"
['Mars', 'Venus', 'Jupiter', 'Earth', 'Saturn']

$ shared store "my-store" "colors"
{'red', 'green', 'blue'}

$ shared store "my-store" "people"
{'Jack': 'male', 'Jane': 'female'}
```

You can check the contents of a store:
```bash
$ shared store "my-store"
/home/alex/PyrusticData/shared
- colors (set)
- people (dict)
- planets (list)
```

By default, the command line interface looks for the requested store in the default location `$HOME/PyrusticData/shared`. Private stores are still accessible through the command line interface. You will just need to change the current working directory:

```bash
$ cd "/home/alex/private"

$ shared store "secret-store-42"
- Empty store -
```

You can store binary data as an entry from the command line:

```bash
$ shared store "my-store" "selfie" bin "/home/alex/selfie.png"
Successfully updated the entry 'selfie' !
```

You can copy a binary entry into an arbitrary file from the command line:

```bash
$ shared store "my-store" "selfie" > "/home/alex/new.png"

```

You can delete an entry from the command line:

```bash
$ shared del "my-store" "selfie"
Successfully deleted !
```

You can delete a store from the command line:

```bash
$ shared del "my-store"
Successfully deleted !
```


# Shared collections
**Jason** and **Store** works with shared collections that are based on [probed](https://github.com/pyrustic/probed) collections. If the boolean `readonly` isn't set to True, you can use the method `save` of the shared collections returned by **Jason** and **Store**.

There is an intuitive mapping between Python collections, Shared collections, and Probed collections:

| Python collections | Shared collections | Probed collections |
|--------------------|--------------------|--------------------|
| dict               | shared.SharedDict  | probed.ProbedDict  |
| list               | shared.SharedList  | probed.ProbedList  |
| set                | shared.SharedSet   | probed.ProbedSet   |



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

## Make your project packageable
**Backstage** is an extensible command line tool for managing software projects. By default, it supports Python, so you can run the `init` command to make your Python project [packageable](https://packaging.python.org/en/latest/tutorials/packaging-projects/):

```bash
$ cd /path/to/project
$ backstage init
Project successfully initialized !
```

You can also create a distribution package of your project with the `build` command, then publish it to [PyPI](https://pypi.org/) with the `release` command, et cetera.

**Discover [Backstage](https://github.com/pyrustic/backstage) !**


<br>
<br>
<br>

[Back to top](#readme)