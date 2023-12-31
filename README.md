
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI package version](https://img.shields.io/pypi/v/shared)](https://pypi.org/project/shared)

<!-- Cover -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/shared/cover.png" alt="Cover" width="630">
    <p align="center">
    <i> </i>
    </p>
</div>



# Pyrustic Shared
**Data exchange and persistence**

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/shared/tags) . [Modules](https://github.com/pyrustic/shared/tree/master/docs/modules#readme)

## Table of contents
- [Overview](#overview) 
- [Example](#example) 
- [API](#api)
- [Installation](#installation) 

# Overview
**Shared** is a Python package created to be the programmer's companion when it comes to storing unstructured application data, managing configuration files, caching data, and exchanging data with other programs.

Under the hood, Shared uses [Paradict](https://github.com/pyrustic/paradict) to encode a dictionary populated with **strings**, **scalars** (integer, float, decimal float, complex, booleans), **date** and **time**, **null** value, **binary** data and nested **collections** (list, set, and dictionary).

> **Note:** This library isn't intended to replace a proper relational database such as SQLite !

# Example
```python
from shared import Dossier, HOME
from datetime import datetime
from pathlib import Path

# load a picture
with open("/home/alex/image.png", "rb") as file:
    photo = file.read()

# create a user profile dictionary embedding the picture
now = datetime.now()
profile = {"name": "alex", "access_datetime": now, "photo": photo,
           "pi": 3.14, "books": ["Seul sur Mars", "The Fall"],
           "is_author": True, "fingerprint": None}

# create a dossier (or access an existing one)
path = Path(HOME, "my_dossier")
dossier = Dossier(path)

# save profile dictionary in the dossier
dossier.set("my_profile", profile)

# retrieve profile dictionary
profile_bis = dossier.get("my_profile")

# let's compare the two profile objects !
assert profile == profile_bis
```

# API
Explore the source code.


# Installation
**Shared** is **cross platform**. It is built on [Ubuntu](https://ubuntu.com/download/desktop) with [Python 3.8](https://www.python.org/downloads/) and should work on **Python 3.5** or **newer**.


## Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

## Install for the first time

```bash
pip install shared
```

## Upgrade the package
```bash
pip install shared --upgrade --upgrade-strategy eager
```

## Deactivate the virtual environment
```bash
deactivate
```

# About the author
Hi, I'm Alex, a tech enthusiast ! Get in touch with [me](https://pyrustic.github.io/#contact) ! 

<br>
<br>
<br>

[Back to top](#readme)
