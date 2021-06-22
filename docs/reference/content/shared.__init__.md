
Back to [Reference Overview](https://github.com/pyrustic/shared/blob/master/docs/reference/README.md)

# shared.\_\_init\_\_



<br>


```python
DEFAULT_PATH = "/home/alex/PyrusticData/shared"

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

class ReadonlyError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class Shared:
    """
    
    """

    def __init__(self, store, path='/home/alex/PyrusticData/shared', readonly=False):
        """
        An easy and intuitive way to store your data collections !
        
        Parameters:
            - store: str, the name of the store, just give the app name
            - path: str, the directory where to save data, by default
            it is the path ~/PyrusticData/datastore
            - readonly: bool
        """

    @property
    def bin(self):
        """
        Getter only + Returns a copy 
        """

    @property
    def dict(self):
        """
        
        """

    @dict.setter
    def dict(self, val):
        """
        
        """

    @property
    def exists(self):
        """
        
        """

    @property
    def list(self):
        """
        
        """

    @list.setter
    def list(self, val):
        """
        
        """

    @property
    def path(self):
        """
        
        """

    @property
    def readonly(self):
        """
        
        """

    @property
    def set(self):
        """
        
        """

    @set.setter
    def set(self, val):
        """
        
        """

    @property
    def store(self):
        """
        
        """

    def add_bin(self, name, data):
        """
        
        """

    def del_bin(self, name=None):
        """
        
        """

    def del_store(self):
        """
        
        """

    def reload(self):
        """
        
        """

    def save(self):
        """
        
        """

```

