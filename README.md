
## Shared

`Shared` is the Python library to store, expose, read, and edit collections of data.
 It's part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).

[Installation](#installation) | [Reference](https://github.com/pyrustic/shared/tree/master/docs/reference#readme)


## Overview
Shared contains two main classes: `Jason` and `Store`.

`Jason` allows individual access to `json` files that are likely to be manually edited by a human user. `Jason` is relevant for managing configuration files.

`Store` allows you to store collections of data without worrying about how they are actually saved. `Store` is relevant for application data storage and persistent data caching.

### Jason

Let's play with `Jason`:
```python
from shared import Jason


# access 'my-data.json'
jason = Jason("my-data")
# let's initialize the content of 'my-data'
if jason.new:
    jason.data = {"name": "alex", "job": "angelist"}

jason.data["job"] = "evangelist"

jason.save()  # persisted !
```

The same stuff with two twists:
```python
from shared import Jason

# default data to init my 'my-data.json'
DEFAULT_DATA = {"name": "alex", "job": "angelist"}

# access 'my-data.json'
jason = Jason("my-data", default=DEFAULT_DATA)

# jason.data is either an instance of
# shared.SharedDict or shared.SharedList
data = jason.data

data["job"] = "evangelist"

# yes, you can call the .save method directly
# from the data returned by the jason.data property
data.save()  # persisted !

```
By default, the `json` files are saved in the in `$HOME/PyrusticData/shared`. You can change the location to fit your needs:

```python
from shared import Jason

LOCATION = "/home/alex/app-data"

# access 'my-data.json'
jason = Jason("my-data", location=LOCATION, readonly=True)

# when you set readonly to True, you can't anymore edit the content !

```
Two more tips:
```python
from shared import Jason


# access 'my-config.json'
jason = Jason("my-config", autosave=True, default=[])

# when you set autosave to True, you don't anymore need
# to call the method .save() !

jason.data.append("batman")  # persisted ! yeah yeah !

# you can delete the jason file (assuming that readonly is False)
jason.delete()

print(jason.deleted)  # output: True
```

Now let's discover the class `shared.Store` !


### Store
Store data:

```python
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

# Done !
```

Read data from another script:

```python
from shared import Store

# let's open the shared store in readonly mode
store = Store("my-store", readonly=True)

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

Since we're all consenting adults here, you can edit the data from another script:

```python
from shared import Store

store = Store("my-store")
planets = store.get("planets")

# the object 'planets' is a SharedList
print(type(planets))
# output: <class 'shared.SharedList'>

# you can update its content like a standard list
planets.append("Earth")

# then you can save the updated collection
planets.save()

```

Maybe you need your collection to be automatically saved when its content changes:

```python
from shared import Store

# the 'autosave' feature will save your collections
# whenever their content change
store = Store("my-store", autosave=True)
planets = store.get("planets")

planets.append("Saturn")  # done ! collection updated and saved !

```

`Shared` comes with an easy-to-use command line interface:

```bash
$ shared store "my-store" "planets"
['Mars', 'Venus', 'Jupiter', 'Earth', 'Saturn']

$ shared store "my-store" "colors"
{'red', 'green', 'blue'}

$ shared store "my-store" "people"
{'Jack': 'male', 'Jane': 'female'}
```

Type `help` in the command line interface to display a short manual.

Now you are wondering where `Shared` stores collections and in what file format.

Well, the file format is [JSON](https://en.wikipedia.org/wiki/JSON), and the default location is in the [home directory](https://en.wikipedia.org/wiki/Home_directory). More precisely, the default directory to keep stores is: `$HOME/PyrusticData/shared`.

```bash
$ shared store "my-store"
/home/alex/PyrusticData/shared
- colors (set)
- people (dict)
- planets (list)
```

You can change the default location:

```python
from shared import Store

PRIVATE_DATA_DIRECTORY = "/home/alex/private"
store = Store("secret-store-42", location=PRIVATE_DATA_DIRECTORY)

# the store 'secret-store-42' will be created inside
# the directory '/home/alex/private'

```

Private stores are still accessible through the command line interface. You will just need to change the current working directory:

```bash
$ cd "/home/alex/private"

$ shared store "secret-store-42"
- Empty store -
```

As you can see, `Shared` is great for sharing collections with other software, or just used as private data storage. The command line interface makes things more wonderful.

Wait... can you store binary data with `Shared` ?

Yes, you can:

```python
from shared import Store

store = Store("my-store")

with open("/home/alex/selfie.png", "rb") as file:
    data = file.read()
    store.set("selfie", data)  # set the entry 'selfie'

```

From the command line, you can copy this binary data into an arbitrary file:

```bash
$ shared store "my-store" "selfie" > "/home/alex/new.png"

```

Or you can do the same thing but in reverse, i.e. store the binary data from the command line:

```bash
$ shared store "my-store" "selfie" bin "/home/alex/selfie.png"
Successfully updated the entry 'selfie' !
```

Then programmatically copy this binary data to an arbitrary file:

```python
from shared import Store
from shutil import copyfile

store = Store("my-store")
source_path = store.get("selfie")  # get the bin entry 'selfie'
destination_path = "/home/alex/new.png"

# copy the content from source to destination
copyfile(source_path, destination_path)

```

Do you care about the space available on your hard drive ?

Well you can easily delete any entry. Programmatically:

```python
from shared import Store

store = Store("my-store")
# delete the entry 'selfie'
store.delete("selfie")

```

or from the command line interface:

```bash
$ shared del "my-store" "selfie"
Successfully deleted !
```

You can decide to be a badass and delete the store. Programmatically:

```python
from shared import Store

store = Store("my-store")
store.delete()  # data collections, binary data, and meta data are gone
```

or from the command line interface:

```bash
$ shared del "my-store"
Successfully deleted !

```

Between us, do you trust the `delete` feature ? Here is a snippet of the code which shows that the directory to be deleted must have a particular signature, otherwise it will not be deleted:

```python

def delete(self, *names):
    
    ...
    
    if self._readonly:
        raise ReadonlyError
    # the directory to delete is checked
    # to be sure that it has the store signature
    if not valid_store(self._store_path):
        return False
    if not names:  # delete store
        shutil.rmtree(self._store_path)
    
    ...

```

Are you wondering how the `autosave` feature works ? Under the hood, `Shared` uses the awesome library `probed`.

`Probed` collections let you know when their content change (with 1 more twist !).

Discover [Probed](https://github.com/pyrustic/probed) !


## Installation
Do you like `Shared` ? Guess what, it's available on [PyPI](https://pypi.org):

```bash
$ pip install shared
```

## Related projects
Both `Shared` and `Probed` are part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).

Looking for an awesome theme for your desktop application ? Check [Cyberpunk Theme](https://github.com/pyrustic/cyberpunk-theme) !

Do you want to create a popular theme for Python desktop apps ? Check [TkStyle](https://github.com/pyrustic/tkstyle) !

Do you dream to add the autocomplete feature to your desktop app ? Check [Suggestion](https://github.com/pyrustic/suggestion) !

Struggling with GUI+multithreading ? Check [Threadom](https://github.com/pyrustic/threadom) !

Do you like the project(s) and want to help ? Tell your friends about the project(s) !