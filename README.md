## Shared

`Shared` is a Python library to store, expose, read, and edit collections of data.

Store your data:

```python
from shared import Shared

shared = Shared("my-store")
shared.dict = {"author": "alexrustic", "year": 2020}
shared.save()

```

Read the data from another script:

```python
from shared import Shared

shared = Shared("my-store", readonly=True)
print(shared.dict)  # {"author": "alexrustic", "year": 2020}

```

Since we're all consenting adults here, you can edit the data from another script:

```python
from shared import Shared

shared = Shared("my-store")
shared.dict["year"] = 2021
shared.save()
```

Access data from the command line:

```bash
$ shared "my-store" dict
{"author": "alexrustic", "year": 2021}
```

So far we've only played with the `dict` container. There is more to play with:

```python
from shared import Shared

shared = Shared("my-store")
# list container
shared.list.append("hello")
shared.list.append("friend")  
# set container
shared.set = {"red", "blue"}
# save
shared.save()
```

Yes, you can view previous collections from the command line interface:

```bash
$ shared "my-store" list
["hello", "friend"]

$ shared "my-store" set
{"red", "blue"}
```

Wait... can you store binary data with `Shared` ?

Yes, you can:

```python
from shared import Shared

shared = Shared("my-store")

with open("/home/alex/selfie.png", "rb") as file:
    data = file.read()
    shared.add_bin("selfie", data)  # the name of this entry is "selfie"
    
# binary data are available in the 'bin' collection
for name, path in shared.bin.items():
    print(name, path)
```

From the command line, you can copy this binary data into an arbitrary file:

```bash
$ shared "my-store" bin "selfie" > "/home/alex/new.png"

```

Or you can do the same but backwards, i.e. store the binary data from the command line:

```bash
$ shared "my-store" bin "selfie" "/home/alex/selfie.png"

```

Then programmatically copy this binary data to an arbitrary file:

```python
from shared import Shared
from shutil import copyfile

shared = Shared("my-store")
source = shared.bin["selfie"]  # the source path
destination = "/home/alex/new.png"

# copy the content from src to dst
copyfile(source, destination)

```

Do you care about the space available on your hard drive ?
Well you can easily delete the binary data:

```python
from shared import Shared

shared = Shared("my-store")
# delete only the 'selfie' binary data
shared.del_bin("selfie")
# or just clear binary data
shared.del_bin()
```

You can decide to be a badass and delete the store:

```python
from shared import Shared

shared = Shared("my-store")
shared.del_store()  # data collections, binary data, and meta data are gone

```

When you call the `save` method, only data collections that have been modified are saved. To do this, `Shared` uses [Probed](https://github.com/pyrustic/probed) data collections. `Probed` is the library that will change the way you interact with Python collections.


Discover [Probed](https://github.com/pyrustic/probed) !


Do you like `Shared` ? Guess what, it's available on PyPI:

```bash
$ pip install shared
```

Join the [Discord](https://discord.gg/fSZ6nxzVd6) !
