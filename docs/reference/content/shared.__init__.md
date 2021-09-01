
Back to [Reference Overview](https://github.com/pyrustic/shared/blob/master/docs/reference/README.md#readme)

# shared.\_\_init\_\_



<br>


```python
DEFAULT_LOCATION = "/home/alex/PyrusticData/shared"

```

<br>

```python

def json_dump(json_filename, data, pretty=True):
    """
    
    """

```

<br>

```python

def json_load(json_filename):
    """
    
    """

```

<br>

```python

def valid_jason(path):
    """
    
    """

```

<br>

```python

def valid_store(path):
    """
    
    """

```

<br>

```python

class Config:
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    """

    def __init__(self, name, *, readonly=False, autosave=False, default=None, location='/home/alex/PyrusticData/shared'):
        """
        - items: default value of the collection
        
        - probe: callback called whenever the content of the collection
        is going to change.
        It should accept as argument an instance of probed.Info.
        It should return the same instance (edited or not) of probed.Info
        it got as argument, or return None to cancel the change operation.
        
        - on_change: callback called whenever the content of the collection changes.
        It should accept as argument an instance of probed.Info.
        """

    @property
    def autosave(self):
        """
        
        """

    @property
    def deleted(self):
        """
        
        """

    @property
    def location(self):
        """
        
        """

    @property
    def name(self):
        """
        
        """

    @property
    def new(self):
        """
        Returns True if this store is newly created, else return False 
        """

    @property
    def readonly(self):
        """
        
        """

    def delete(self):
        """
        
        """

    def save(self):
        """
        Save the config 
        """

```

<br>

```python

class Error:
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

<br>

```python

class Jason:
    """
    
    """

    def __init__(self, name, *, readonly=False, autosave=False, default=None, location='/home/alex/PyrusticData/shared'):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def autosave(self):
        """
        
        """

    @property
    def data(self):
        """
        
        """

    @data.setter
    def data(self, val):
        """
        
        """

    @property
    def deleted(self):
        """
        
        """

    @property
    def location(self):
        """
        
        """

    @property
    def name(self):
        """
        
        """

    @property
    def new(self):
        """
        Returns True if this json file is newly created, else return False 
        """

    @property
    def readonly(self):
        """
        
        """

    def delete(self):
        """
        This method delete the Jason file.
        Returns a boolean or raise ReadonlyError
        """

    def save(self):
        """
        
        """

```

<br>

```python

class JasonDeletedError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class ReadonlyError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class SharedDict:
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    """

    def save(self):
        """
        
        """

```

<br>

```python

class SharedList:
    """
    Built-in mutable sequence.
    
    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    """

    def save(self):
        """
        
        """

```

<br>

```python

class SharedSet:
    """
    set() -> new empty set object
    set(iterable) -> new set object
    
    Build an unordered collection of unique elements.
    """

    def save(self):
        """
        
        """

```

<br>

```python

class Store:
    """
    
    """

    def __init__(self, name, *, readonly=False, autosave=False, location='/home/alex/PyrusticData/shared'):
        """
        - name: str, the name of the store
        - readonly: bool, readonly mode
        - autosave: bool, auto-save mode
        - location: str, the directory where stores will be created
        """

    @property
    def autosave(self):
        """
        
        """

    @property
    def deleted(self):
        """
        Returns True if this store has been deleted through this object 
        """

    @property
    def info(self):
        """
        Returns a dictionary of entries and their container types
        Example: {"entry_1": "dict", "entry_2": "bin", "entry_3": "set"}
        """

    @property
    def location(self):
        """
        
        """

    @property
    def name(self):
        """
        
        """

    @property
    def new(self):
        """
        Returns True if this store is newly created, else return False 
        """

    @property
    def readonly(self):
        """
        
        """

    def delete(self, *names):
        """
        This method delete the store if there isn't any argument.
        Else, the arguments are the entries to delete.
        Returns a boolean or raise ReadonlyError
        """

    def get(self, name, default=None):
        """
        This method returns None if the entry isn't in the store.
        A path is returned if the entry requested exists and is a binary data.
        SharedDict, SharedList, SharedSet are returned respectively if the entry
        requested is a dict, a list or a set
        """

    def set(self, name, data):
        """
        Set an entry.
        Data should be a dict, a list, a set or a binary data.
        This method will return a path if the entry is a binary data.
        SharedDict, SharedList, SharedSet are returned respectively if the entry
        requested is a dict, a list or a set.
        You can call the method "save" on the instances of SharedDict, SharedList,
        or SharedSet.
        """

```

<br>

```python

class StoreDeletedError:
    """
    Common base class for all non-exit exceptions.
    """

```

