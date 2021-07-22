import os
import os.path
import json
import time
import shutil
from probed import ProbedDict, ProbedList, ProbedSet


DEFAULT_LOCATION = os.path.join(os.path.expanduser("~"),
                                "PyrusticData", "shared")


class Shared:
    def __init__(self, store, readonly=False,
                 autosave=False, location=DEFAULT_LOCATION):
        """
        - store: the name of the store
        - readonly: boolean, readonly mode
        - autosave: boolean, auto-save mode
        - location: the directory where stores can be created
        """
        self._store = store
        self._readonly = readonly
        self._autosave = autosave
        self._location = location
        self._store_path = None
        self._meta = dict()
        self._meta_filename = None
        self._data_path = None
        self._cache = dict()
        self._deleted = False
        self._setup()

    @property
    def store(self):
        return self._store

    @property
    def readonly(self):
        return self._readonly

    @property
    def autosave(self):
        return self._autosave

    @property
    def location(self):
        return self._location

    @property
    def info(self):
        """
        Returns a dictionary of entries and their container types
        Example: {"entry_1": "dict", "entry_2": "bin", "entry_3": "set"}
        """
        self._load_meta()
        cache = dict()
        for key, value in self._meta.items():
            container, _ = value
            cache[key] = container
        return cache

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
        if self._deleted:
            return
        if self._readonly:
            raise ReadonlyError
        container = self._get_container(data)
        container = "bin" if container is None else container
        return self._save(name, container, data)

    def get(self, name):
        """
        This method returns None if the entry isn't in the store.
        A path is returned if the entry requested exists and is a binary data.
        SharedDict, SharedList, SharedSet are returned respectively if the entry
        requested is a dict, a list or a set
        """
        if self._deleted:
            return
        self._load_meta()
        cache = self._meta.get(name)
        if cache is None:
            return None
        container, filename = cache
        if container == "bin":
            return filename
        data = json_load(filename)
        collection = self._convert_collection(container, data)
        self._bind_save_method(name, container, collection)
        return collection

    def delete(self, *names):
        """
        This method delete the store if there isn't any argument.
        Else, the arguments are the entries to delete.
        Returns a boolean or raise ReadonlyError
        """
        if self._deleted:
            return
        if self._readonly:
            raise ReadonlyError
        if not legal_store(self._store_path):
            return False
        if not names:  # delete store
            shutil.rmtree(self._store_path)
            self._deleted = True
        else:
            self._load_meta()
            for name in names:
                cache = self._meta.get(name)
                if not cache:
                    continue
                del self._meta[name]
                _, filename = cache
                if os.path.isfile(filename):
                    os.remove(filename)
            json_dump(self._meta_filename, self._meta)
        return True

    def _setup(self):
        self._store_path = os.path.join(self._location, self._store)
        self._meta_filename = os.path.join(self._store_path, "meta")
        self._data_path = os.path.join(self._store_path, "data")
        self._create_store()
        self._load_meta()

    def _create_store(self):
        if self._readonly or legal_store(self._store_path):
            return
        # create store
        os.makedirs(self._store_path)
        # create data folder
        os.mkdir(os.path.join(self._store_path, "data"))
        # create meta file
        json_dump(self._meta_filename, dict())
        # add 'pyrustic' empty file (signature)
        cache = os.path.join(self._store_path, "pyrustic")
        with open(cache, "w") as file:
            pass
        # add 'shared' empty file (signature)
        cache = os.path.join(self._store_path, "shared")
        with open(cache, "w") as file:
            pass

    def _load_meta(self):
        if not os.path.exists(self._store_path):
            return
        self._meta = json_load(self._meta_filename)

    def _gen_filename(self, container):
        while True:
            timestamp = int(time.time())
            cache = "{}-{}".format(container, str(timestamp))
            filename = os.path.join(self._data_path, cache)
            if not os.path.exists(filename):
                return filename

    def _save(self, name, container, data):
        cache = self._meta.get(name)
        if cache is None:
            filename = self._gen_filename(container)
        else:
            _, filename = cache
        # save metadata
        self._meta[name] = (container, filename)
        self._save_meta()
        if container == "set":
            data = self._set_to_dict(data)
        if container in ("dict", "list", "set"):
            json_dump(filename, data)
            if (isinstance(data, SharedDict)
                    or isinstance(data, SharedList)
                    or isinstance(data, SharedSet)):
                return data
            cache = self._convert_collection(container, data)
            self._bind_save_method(name, container, cache)
            return cache
        elif container == "bin":
            with open(filename, "wb") as file:
                file.write(data)
            return filename
        else:
            raise Error("Unknown container '{}'.".format(container))

    def _save_meta(self):
        json_dump(self._meta_filename, self._meta)

    def _get_container(self, data):
        result = None
        if isinstance(data, dict):
            result = "dict"
        elif isinstance(data, list):
            result = "list"
        elif isinstance(data, set):
            result = "set"
        return result

    def _convert_collection(self, container, data):
        if container == "dict":
            cache = SharedDict(items=data)
        elif container == "list":
            cache = SharedList(items=data)
        elif container == "set":
            cache = SharedSet(items=data)
        else:
            raise Error("Unknown container '{}'.".format(container))
        return cache

    def _bind_save_method(self, name, container, collection):
        if self._readonly:
            return
        collection.save = (lambda self=self, name=name,
                                  container=container,
                                  collection=collection:
                           self._save(name, container, collection))
        if self._autosave:
            collection.on_change = (lambda info: info.collection.save())

    def _set_to_dict(self, data):
        return {item: None for item in data}


class SharedDict(ProbedDict):
    def save(self):
        raise ReadonlyError


class SharedList(ProbedList):
    def save(self):
        raise ReadonlyError


class SharedSet(ProbedSet):
    def save(self):
        raise ReadonlyError


def json_dump(json_filename, data):
    with open(json_filename, "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)


def json_load(json_filename):
    with open(json_filename, "r") as file:
        data = json.load(file)
    return data


def legal_store(path):
    pyrustic_file = os.path.join(path, "pyrustic")
    shared_file = os.path.join(path, "shared")
    meta_file = os.path.join(path, "meta")
    data_folder = os.path.join(path, "data")
    for item in (pyrustic_file, shared_file, meta_file):
        if not os.path.isfile(item):
            return False
    if not os.path.isdir(data_folder):
        return False
    return True


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ReadonlyError(Error):
    pass
