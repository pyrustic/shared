## Shared

`Shared` is a Python library to store, expose, read, and edit collections of data.

Expose your data:

```python
from shared import Shared

shared = Shared("my-store")
shared.dict = {"author": "alexrustic", "year": 2020}
shared.save()

```

Read data:

```python
from shared import Shared

shared = Shared("my-store", readonly=True)
print(shared.dict)  # {"author": "alexrustic", "year": 2020}

```

Edit data:

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

`Dict` is just one of the available collections of data:

```python
from shared import Shared

shared = Shared("my-store")
# list
shared.list.append("hello")
shared.list.append("friend")
# set
shared.set = {"red", "blue"}

shared.save()
```

And yes, you can read the content from the command line interface:

```bash
$ shared "my-store" list
["hello", "friend"]

$ shared "my-store" set
{"red", "blue"}
```

But wait... can you store binary data with `Shared` ?

Yes, you can:

```python
from shared import Shared

shared = Shared("my-store")
with open("/home/alex/selfie.png", "rb") as file:
    data = file.read()
    shared.add_bin("selfie", data)
    
# binary data are available in the 'bin' collection
for name, path in shared.bin.items():
    print(name, path)
```

From the command line, you can copy this binary data into an arbitrary file:

```bash
$ shared "my-store" bin "selfie" > "/home/alex/new.png"

```

Or you can do the same thing but in the opposite way: store the binary data from the command line

```bash
$ shared "my-store" bin "selfie" "/home/alex/selfie.png"

```

Then programmatically copy this binary data into an arbitrary file:

```python
from shared import Shared
from shutil import copyfile

shared = Shared("my-store")
src = shared.bin["selfie"]
dst = "/home/alex/new.png"
# copy the content from src to dst
copyfile(src, dst)

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

You can decide to be a badass and delete the whole store:

```python
from shared import Shared

shared = Shared("my-store")
shared.del_store()
```

Do you like this library ? Guess what, it's available on PyPI:

```bash
pip install shared
```

No dependency... No voodoo magic... Be curious, explore the source code to discover the rest ;)
