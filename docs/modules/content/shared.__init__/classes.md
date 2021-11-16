Back to [Modules overview](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md)
  
# Module documentation
>## shared.\_\_init\_\_
No description
<br>
[constants (1)](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared.__init__/constants.md) &nbsp;.&nbsp; [functions (4)](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared.__init__/functions.md) &nbsp;.&nbsp; [classes (9)](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared.__init__/classes.md)


## Classes
```python
class Error(Exception):
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

```python
class Jason(object):
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

    def _bind_save_method(self):
        """
        
        """

    def _convert_collection(self, data):
        """
        
        """

    def _setup(self):
        """
        
        """

```

```python
class JasonDeletedError(shared.__init__.Error):
    """
    Common base class for all non-exit exceptions.
    """

    # inherited from shared.__init__.Error
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

```python
class ReadonlyError(shared.__init__.Error):
    """
    Common base class for all non-exit exceptions.
    """

    # inherited from shared.__init__.Error
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

```python
class SharedDict(probed.ProbedDict):
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

    # inherited from probed.ProbedDict
    def __init__(self, items=None, probe=None, on_change=None):
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

    # inherited from probed.ProbedDict
    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """

    # inherited from probed.ProbedDict
    @changed.setter
    def changed(self, val):
        """
        
        """

    # inherited from probed.ProbedDict
    @property
    def on_change(self):
        """
        
        """

    # inherited from probed.ProbedDict
    @on_change.setter
    def on_change(self, val):
        """
        
        """

    # inherited from probed.ProbedDict
    @property
    def probe(self):
        """
        
        """

    # inherited from probed.ProbedDict
    @probe.setter
    def probe(self, val):
        """
        
        """

    # inherited from probed.ProbedDict
    def clear(self):
        """
        D.clear() -> None.  Remove all items from D.
        """

    # inherited from dict
    def fromkeys(type, iterable, value=None, /):
        """
        Create a new dictionary with keys from iterable and values set to value.
        """

    # inherited from dict
    def get(self, key, default=None, /):
        """
        Return the value for key if key is in the dictionary, else default.
        """

    # inherited from probed.ProbedDict
    def pop(self, key, default=None):
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """

    # inherited from probed.ProbedDict
    def popitem(self):
        """
        Remove and return a (key, value) pair as a 2-tuple.
        
        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """

    def save(self):
        """
        
        """

    # inherited from probed.ProbedDict
    def setdefault(self, key, default=None):
        """
        Insert key with a value of default if key is not in the dictionary.
        
        Return the value for key if key is in the dictionary, else default.
        """

    # inherited from probed.ProbedDict
    def update(self, other=None, **kwargs):
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """

```

```python
class SharedList(probed.ProbedList):
    """
    Built-in mutable sequence.
    
    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    """

    # inherited from probed.ProbedList
    def __init__(self, items=None, probe=None, on_change=None):
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

    # inherited from probed.ProbedList
    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """

    # inherited from probed.ProbedList
    @changed.setter
    def changed(self, val):
        """
        
        """

    # inherited from probed.ProbedList
    @property
    def on_change(self):
        """
        
        """

    # inherited from probed.ProbedList
    @on_change.setter
    def on_change(self, val):
        """
        
        """

    # inherited from probed.ProbedList
    @property
    def probe(self):
        """
        
        """

    # inherited from probed.ProbedList
    @probe.setter
    def probe(self, val):
        """
        
        """

    # inherited from probed.ProbedList
    def append(self, value):
        """
        Append object to the end of the list.
        """

    # inherited from probed.ProbedList
    def clear(self):
        """
        Remove all items from list.
        """

    # inherited from list
    def copy(self, /):
        """
        Return a shallow copy of the list.
        """

    # inherited from list
    def count(self, value, /):
        """
        Return number of occurrences of value.
        """

    # inherited from probed.ProbedList
    def extend(self, value):
        """
        Extend list by appending elements from the iterable.
        """

    # inherited from list
    def index(self, value, start=0, stop=9223372036854775807, /):
        """
        Return first index of value.
        
        Raises ValueError if the value is not present.
        """

    # inherited from probed.ProbedList
    def insert(self, index, value):
        """
        Insert object before index.
        """

    # inherited from probed.ProbedList
    def pop(self, index=-1):
        """
        Remove and return item at index (default last).
        
        Raises IndexError if list is empty or index is out of range.
        """

    # inherited from probed.ProbedList
    def remove(self, value):
        """
        Remove first occurrence of value.
        
        Raises ValueError if the value is not present.
        """

    # inherited from probed.ProbedList
    def reverse(self):
        """
        Reverse *IN PLACE*.
        """

    def save(self):
        """
        
        """

    # inherited from probed.ProbedList
    def sort(self, *, key=None, reverse=False):
        """
        Sort the list in ascending order and return None.
        
        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).
        
        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.
        
        The reverse flag can be set to sort in descending order.
        """

```

```python
class SharedSet(probed.ProbedSet):
    """
    set() -> new empty set object
    set(iterable) -> new set object
    
    Build an unordered collection of unique elements.
    """

    # inherited from probed.ProbedSet
    def __init__(self, items=None, probe=None, on_change=None):
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

    # inherited from probed.ProbedSet
    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """

    # inherited from probed.ProbedSet
    @changed.setter
    def changed(self, val):
        """
        
        """

    # inherited from probed.ProbedSet
    @property
    def on_change(self):
        """
        
        """

    # inherited from probed.ProbedSet
    @on_change.setter
    def on_change(self, val):
        """
        
        """

    # inherited from probed.ProbedSet
    @property
    def probe(self):
        """
        
        """

    # inherited from probed.ProbedSet
    @probe.setter
    def probe(self, val):
        """
        
        """

    # inherited from probed.ProbedSet
    def add(self, item):
        """
        Add an element to a set.
        
        This has no effect if the element is already present.
        """

    # inherited from probed.ProbedSet
    def clear(self):
        """
        Remove all elements from this set.
        """

    # inherited from probed.ProbedSet
    def difference_update(self, *others):
        """
        Remove all elements of another set from this set.
        """

    # inherited from probed.ProbedSet
    def discard(self, item):
        """
        Remove an element from a set if it is a member.
        
        If the element is not a member, do nothing.
        """

    # inherited from probed.ProbedSet
    def intersection_update(self, *others):
        """
        Update a set with the intersection of itself and another.
        """

    # inherited from probed.ProbedSet
    def pop(self):
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """

    # inherited from probed.ProbedSet
    def remove(self, item):
        """
        Remove an element from a set; it must be a member.
        
        If the element is not a member, raise a KeyError.
        """

    def save(self):
        """
        
        """

    # inherited from probed.ProbedSet
    def symmetric_difference_update(self, other):
        """
        Update a set with the symmetric difference of itself and another.
        """

    # inherited from probed.ProbedSet
    def update(self, *others):
        """
        Update a set with the union of itself and others.
        """

```

```python
class Store(object):
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

    def _bind_save_method(self, name, collection):
        """
        
        """

    def _convert_collection(self, container, data):
        """
        
        """

    def _create_store(self):
        """
        
        """

    def _gen_file_id(self):
        """
        
        """

    def _get_container(self, data):
        """
        
        """

    def _get_filename(self, file_id):
        """
        
        """

    def _load_meta(self):
        """
        
        """

    def _save(self, name, container, data):
        """
        
        """

    def _save_meta(self):
        """
        
        """

    def _set_to_dict(self, data):
        """
        
        """

    def _setup(self):
        """
        
        """

```

```python
class StoreDeletedError(shared.__init__.Error):
    """
    Common base class for all non-exit exceptions.
    """

    # inherited from shared.__init__.Error
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

