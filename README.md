## Shared

`Shared` is the Python library to store, expose, read, and edit collections of data.
 It's part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).

## Overview

Use `Shared` to easily store your data:

```python
from shared import Shared

# data
people = {"Jack": "male", "Jane": "female"}  # dict
planets = ["Mars", "Venus", "Jupiter"]  # list
colors = {"red", "green", "blue"}  # set

# let's persist the data in the store 'my-store'
shared = Shared("my-store")
shared.set("people", people)  # set the entry 'people'
shared.set("planets", planets)  # set the entry 'planets'
shared.set("colors", colors)  # set the entry 'colors'

# Done !
```

Read the data from another script:

```python
from shared import Shared

# let's open the shared store in readonly mode
shared = Shared("my-store", readonly=True)

# get data from the shared store 'my-store'
people = shared.get("people") # get the entry 'people'
planets = shared.get("planets") # get the entry 'planets'
colors = shared.get("colors") # get the entry 'colors'

print(people)
# output: {'Jack': 'male', 'Jane': 'female'}

print(planets)
# output: ['Mars', 'Venus', 'Jupiter']

print(colors)
# output: {'red', 'green', 'blue'}

```

Since we're all consenting adults here, you can edit the data from another script:

```python
from shared import Shared

shared = Shared("my-store")
planets = shared.get("planets")

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
from shared import Shared

# the 'autosave' feature will save your collections
# whenever their content change
shared = Shared("my-store", autosave=True)
planets = shared.get("planets")

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
from shared import Shared

PRIVATE_DATA_DIRECTORY = "/home/alex/private"
shared = Shared("secret-store-42",
                location=PRIVATE_DATA_DIRECTORY)

# the store 'secret-store-42' will be created inside
# the directory '/home/alex/private'

```

Private stores are still accessible through the command line interface. You will just need to change the current working directory:

```bash
$ cd "/home/alex/private"

$ shared store "secret-store-42"
- Empty store -
```

As you can see, `Shared` is great for sharing collections with other software, or just used as a private database. The command line interface makes things more wonderful.

Wait... can you store binary data with `Shared` ?

Yes, you can:

```python
from shared import Shared

shared = Shared("my-store")

with open("/home/alex/selfie.png", "rb") as file:
    data = file.read()
    shared.set("selfie", data)  # set the entry 'selfie'

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
from shared import Shared
from shutil import copyfile

shared = Shared("my-store")
source_path = shared.get("selfie")  # get the bin entry 'selfie'
destination_path = "/home/alex/new.png"

# copy the content from source to destination
copyfile(source_path, destination_path)

```

Do you care about the space available on your hard drive ?

Well you can easily delete any entry. Programmatically:

```python
from shared import Shared

shared = Shared("my-store")
# delete the entry 'selfie'
shared.delete("selfie")

```

or from the command line interface:

```bash
$ shared del "my-store" "selfie"
Successfully deleted !
```

You can decide to be a badass and delete the store. Programmatically:

```python
from shared import Shared

shared = Shared("my-store")
shared.delete()  # data collections, binary data, and meta data are gone
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
    if not legal_store(self._store_path):
        return False
    if not names:  # delete store
        shutil.rmtree(self._store_path)
    
    ...

```

Are you wondering how the `autosave` feature works ? Under the hood, `Shared` uses the awesome library `probed`.

`Probed` collections let you know when their content change (with 1 more twist !).

Discover [Probed](https://github.com/pyrustic/probed) !


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