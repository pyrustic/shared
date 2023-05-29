"""Shared Data Interface"""
import os
import os.path
import pathlib
import jesth
from jesth import ValueConverter
from shared import misc


class Dossier:
    def __init__(self, path, value_converter=None):
        self._path = str(pathlib.Path(path).resolve())
        self._value_converter = value_converter if value_converter else ValueConverter()
        self._setup()

    @property
    def path(self):
        return self._path

    @property
    def value_converter(self):
        return self._value_converter

    @property
    def exists(self):
        if os.path.isdir(self._path):
            return True
        return False

    @property
    def entries(self):
        return self._get_entries()

    def get(self, entry, fallback=None):
        path = self.locate(entry)
        if not path:
            return fallback
        document = jesth.read(path, value_converter=self._value_converter)
        section = document.get("")  # get anonymous top section
        r = section.to_dict(strict=True)
        if not r:
            return fallback
        return r.get("data", fallback)

    def set(self, entry, data):
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
        body = {"data": data}
        doc = jesth.Document(path, value_converter=self._value_converter)
        doc.set(index=0, header="", body=body)
        doc.save()
