"""Main module"""
import os
import os.path
import pathlib
from paradict import Datatype
from paradict import TypeRef
import kvf


__all__ = ["Dossier", "HOME"]


HOME = os.path.join(os.path.expanduser("~"), "PyrusticHome", "shared")


class Dossier:
    """The Dossier class implements data persistence based on human-readable files.
    The Paradict text format is used for the serialization."""
    def __init__(self, path, type_ref=None, obj_builder=None):
        """
        Init

        [params]
        - path: The dossier path
        - type_ref: paradict.TypeRef object for Paradict type customization
        - obj_builder: object builder for Paradict extension
        """
        self._path = str(pathlib.Path(path).resolve())
        self._type_ref = type_ref if type_ref else TypeRef()
        self._obj_builder = obj_builder

    @property
    def path(self):
        """The dossier path"""
        return self._path

    @property
    def type_ref(self):
        """The TypeRef object for Paradict type customization"""
        return self._type_ref

    @property
    def obj_builder(self):
        """The object builder for Paradict extension"""
        return self._obj_builder

    def exists(self, key=None):
        """
        Tells whether an entry exists or not.

        [params]
        - key: The name of the entry

        [returns]
        A boolean.
        """
        if key is None:
            return True if os.path.isdir(self._path) else False
        else:
            return False if self.locate(key) is None else True

    def keys(self):
        """Returns a tuple containing existing keys"""
        return self._get_keys()

    def get(self, key, default=None):
        """
        Get the contents of an existing entry

        [params]
        - key: the name of the entry
        - default: the default value to return

        [returns]
        Returns the default value if the entry doesn't exist, else
        returns the contents of the entry that is a dictionary object.
        """
        filename = self.locate(key)
        if filename is None:
            return default
        doc = kvf.get_config(filename, type_ref=self._type_ref,
                             obj_builder=self._obj_builder)
        return doc.get("", default)  # get the anonymous top section

    def set(self, key, value):
        """
        Set an entry

        [params]
        - key: The name of the entry. Keep in mind that an entry will be
            an actual file (with a `.kvf` extension), therefore its name
            should be a valid filename (not a path !)
        - value: A dictionary object.
        """
        if self._type_ref.check(type(value)) != Datatype.DICT:
            msg = "Value isn't a dictionary"
            raise ValueError(msg)
        # ensure_dossier
        self._ensure_dossier()
        # save data
        sections = {"": value}
        filename = os.path.join(self._path, key + ".kvf")
        kvf.put_config(sections, filename,
                       type_ref=self._type_ref)

    def locate(self, key):
        """
        Get the filename of an entry

        [params]
        - key: The name of the entry

        [returns]
        Returns None if the entry doesn't exist, else returns a filename (absolute path).
        """
        filename = os.path.join(self._path, key + ".kvf")
        return filename if os.path.isfile(filename) else None

    def delete(self, key):
        """
        Delete an entry

        [params]
        - key: The name of the entry

        [returns]
        A boolean.
        """
        filename = self.locate(key)
        if filename is None:
            return False
        if os.path.isdir(filename):
            msg = ("The .locate method returned a directory path !"
                   " Please contact the library author")
            raise Exception(msg)
        try:
            pathlib.Path(filename).unlink()
        except Exception:
            return False
        return True

    def _ensure_dossier(self):
        if os.path.isdir(self._path):
            return
        os.makedirs(self._path)

    def _get_keys(self):
        keys = list()
        for item in os.listdir(self._path):
            filename = os.path.join(self._path, item)
            if not os.path.isfile(filename):
                continue
            name, ext = os.path.splitext(item)
            if ext == ".kvf":
                keys.append(name)
        return tuple(keys)
