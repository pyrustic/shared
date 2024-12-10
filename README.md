[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI package version](https://img.shields.io/pypi/v/shared)](https://pypi.org/project/shared)


⚠️⚠️   

**Shared** is an experimental data exchange and persistence solution based on human-readable files. It serves as a playground to test new ideas and then create stable derivative projects. I recently built a **multi-model embedded database for persisting arbitrary-sized data.** The project is called **[Jinbase](https://github.com/pyrustic/jinbase/)** and I strongly encourage you to give it a **[try](https://github.com/pyrustic/jinbase/)**.

⚠️⚠️   


<!-- Cover -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/shared/cover.png" alt="Cover" width="630">
    <p align="center">
    <i> </i>
    </p>
</div>



# Pyrustic Shared
**Data exchange and persistence based on human-readable files**

## Table of contents
- [Overview](#overview) 
- [Example](#example) 
- [Related projects](#related-projects)
- [Testing and contributing](#testing-and-contributing)
- [Installation](#installation) 

# Overview
**Shared** is a Python package created to be the programmer's companion when it comes to storing unstructured application data, managing configuration files, caching data, and exchanging data with other programs.

Under the hood, Shared uses [Paradict](https://github.com/pyrustic/paradict) to encode a dictionary populated with **strings**, **scalars** (integer, float, decimal float, complex, booleans), **date** and **time**, **null** value, **binary** data and nested **collections** (list, set, and dictionary).

> **Note:** This library does not implement any synchronization mechanisms to prevent simultaneous access to a file, which could lead to data corruption. **For a safe, more robust and rich persistence solution, please consider [Jinbase](https://github.com/pyrustic/jinbase).**

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
assert profile == profile_bis  # True ;)
```


# Related projects
- [Jinbase](https://github.com/pyrustic/jinbase): Multi-model transactional embedded database
- [LiteDBC](https://github.com/pyrustic/litedbc): Lite database connector
- [KvF](https://github.com/pyrustic/kvf): The key-value file format with sections 
- [Paradict](https://github.com/pyrustic/paradict): Streamable multi-format serialization with schema 
- [Asyncpal](https://github.com/pyrustic/asyncpal): Preemptive concurrency and parallelism for sporadic workloads

# Testing and contributing
Feel free to **open an issue** to report a bug, suggest some changes, show some useful code snippets, or discuss anything related to this project. You can also directly email [me](https://pyrustic.github.io/#contact).

## Setup your development environment
Following are instructions to setup your development environment

```bash
# create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# clone the project then change into its directory
git clone https://github.com/pyrustic/shared.git
cd shared

# install the package locally (editable mode)
pip install -e .

# run tests
python -m tests

# deactivate the virtual environment
deactivate
```

<p align="right"><a href="#readme">Back to top</a></p>

# Installation
**Shared** is **cross-platform**. It is built on [Ubuntu](https://ubuntu.com/download/desktop) and should work on **Python 3.5** or **newer**.

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

<p align="right"><a href="#readme">Back to top</a></p>

# About the author
Hello world, I'm Alex (😎️), a tech enthusiast and the architect of [Pyrustic](https://pyrustic.github.io) ! Feel free to get in touch with [me](https://pyrustic.github.io/#contact) !

<br>
<br>
<br>

[Back to top](#readme)