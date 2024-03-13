"""Shared Data Interface"""
import os
import os.path
import pathlib
import braq
from paradict import TypeRef
from shared import misc


class Dossier:
    def __init__(self, path, type_ref=None):
        self._path = str(pathlib.Path(path).resolve())
        self._type_ref = type_ref if type_ref else TypeRef()
        self._schema = None
        self._setup()

    @property
    def path(self):
        return self._path

    @property
    def type_ref(self):
        return self._type_ref

    @property
    def exists(self):
        if os.path.isdir(self._path):
            return True
        return False

    @property
    def entries(self):
        return self._get_entries()
        
    @property
    def schema(self):
        return self._schema

    def get(self, entry, fallback=None):
        fallback = fallback if fallback else dict()
        path = self.locate(entry)
        if not path:
            return fallback
        document = braq.FileDoc(path, type_ref=self._type_ref)
        r = document.get("")  # get anonymous top section
        if not r:
            return fallback
        return r

    def set(self, entry, data):
        # data is a dictionary
        # ensure_dossier
        self._ensure_dossier()
        path = os.path.join(self._path, entry)
        if isinstance(data, bytes):
            self._save_bin_data(path, data)
            return
        self._save_data(path, data)

    def locate(self, entry):
        path = os.path.join(self._path, entry)
        path = path if os.path.isfile(path) else None
        return path

    def rename(self, old_entry, new_entry):
        if old_entry == new_entry or not self.exists:
            return False
        old_path = self.locate(old_entry)
        new_path = misc.compute_path(self._path, new_entry)
        if not old_path or not new_path:
            return False
        try:
            os.rename(old_path, new_path)
        except Exception as e:
            return False
        return True

    def delete(self, entry):
        if not self.exists:
            return False
        path = self.locate(entry)
        try:
            pathlib.Path(path).unlink()
        except Exception:
            return False
        return True

    def bind_schema(self):
        pass
        
    def unbind_schema(self):
        self._schema = None
    
    def destroy(self):
        if not self.exists:
            return False
        for entry in self.entries:
            self.delete(entry)
        try:
            pathlib.Path(self._path).rmdir()
        except Exception:
            return False
        return True

    def _setup(self):
        pass

    def _ensure_dossier(self):
        if os.path.isdir(self._path):
            return
        os.makedirs(self._path)

    def _get_entries(self):
        entries = list()
        for item in os.listdir(self._path):
            path = os.path.join(self._path, item)
            if os.path.isfile(path):
                entries.append(item)
        return entries

    def _save_bin_data(self, path, data):
        with open(path, "wb") as file:
            file.write(data)

    def _save_data(self, path, data):
        doc = braq.FileDoc(path, type_ref=self._type_ref)
        doc.set("", data)
