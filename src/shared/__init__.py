import os
import os.path
import pathlib
from paradict import Datatype
from paradict import TypeRef
import kvf


__all__ = ["Dossier", "HOME"]


HOME = os.path.join(os.path.expanduser("~"), "PyrusticHome", "shared")


class Dossier:
    def __init__(self, path, type_ref=None, obj_builder=None):
        self._path = str(pathlib.Path(path).resolve())
        self._type_ref = type_ref if type_ref else TypeRef()
        self._obj_builder = obj_builder

    @property
    def path(self):
        return self._path

    @property
    def type_ref(self):
        return self._type_ref

    @property
    def obj_builder(self):
        return self._obj_builder

    def exists(self, key=None):
        if key is None:
            return True if os.path.isdir(self._path) else False
        else:
            return False if self.locate(key) is None else True

    def keys(self):
        return self._get_keys()

    def get(self, key, default=None):
        filename = self.locate(key)
        if filename is None:
            return default
        doc = kvf.get_config(filename, type_ref=self._type_ref,
                             obj_builder=self._obj_builder)
        return doc.get("", default)  # get the anonymous top section

    def set(self, key, value):
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
        filename = os.path.join(self._path, key + ".kvf")
        return filename if os.path.isfile(filename) else None

    def delete(self, key):
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
