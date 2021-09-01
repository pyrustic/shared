import os
import os.path
import time
import json
import shutil
from probed import ProbedDict, ProbedList, ProbedSet


DEFAULT_LOCATION = os.path.join(os.path.expanduser("~"),
                                "PyrusticData", "shared")


class Jason:
    def __init__(self, name, *, readonly=False,
                 autosave=False, default=None,
                 location=DEFAULT_LOCATION):
        self._name = name
        self._readonly = readonly
        self._autosave = autosave
        self._default = default
        self._location = location
        self._new = False
        self._deleted = False
        self._filename = None
        self._data = None
        self._setup()

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        if self._deleted:
            raise JasonDeletedError
        if self._readonly:
            raise ReadonlyError
        self._data = self._convert_collection(val)
        self._bind_save_method()

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
    def new(self):
        """ Returns True if this json file is newly created, else return False """
        return self._new

    @property
    def deleted(self):
        return self._deleted

    def _setup(self):
        try:
            os.makedirs(self._location)
        except FileExistsError:
            pass
        self._filename = os.path.join(self._location,
                                      "{}.json".format(self._name))
        if os.path.isfile(self._filename):
            data = json_load(self._filename)
        else:
            data = self._default
            if data is not None:
                json_dump(self._filename, data, pretty=True)
            self._new = True
        self._data = self._convert_collection(data)
        self._bind_save_method()

    def _convert_collection(self, data):
        if isinstance(data, dict):
            data = SharedDict(items=data)
        elif isinstance(data, list):
            data = SharedList(items=data)
        return data

    def _bind_save_method(self):
        if self._data is None:
            return
        self._data.save = lambda self=self: self.save()
        if self._autosave:
            self._data.on_change = (lambda info: info.collection.save())

    def save(self):
        if self._deleted:
            raise JasonDeletedError
        if self._readonly:
            raise ReadonlyError
        json_dump(self._filename, self._data, pretty=True)

    def delete(self):
        """
        This method delete the Jason file.
        Returns a boolean or raise ReadonlyError
        """
        if self._deleted:
            raise JasonDeletedError
        if self._readonly:
            raise ReadonlyError
        if not valid_jason(self._filename):
            return False
        os.remove(self._filename)
        self._deleted = True
        return True


class Store:
    def __init__(self, name, *, readonly=False,
                 autosave=False, location=DEFAULT_LOCATION):
        """
        - name: str, the name of the store
        - readonly: bool, readonly mode
        - autosave: bool, auto-save mode
        - location: str, the directory where stores will be created
        """
        self._name = name
        self._readonly = readonly
        self._autosave = autosave
        self._location = location
        self._store_path = None
        self._meta_filename = None
        self._meta = dict()
        self._cache = dict()
        self._deleted = False
        self._new = False
        self._setup()

    @property
    def name(self):
        return self._name

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
        for name, info in self._meta.items():
            container, _ = info
            cache[name] = container
        return cache

    @property
    def new(self):
        """ Returns True if this store is newly created, else return False """
        return self._new

    @property
    def deleted(self):
        """ Returns True if this store has been deleted through this object """
        return self._deleted

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
            raise StoreDeletedError
        if self._readonly:
            raise ReadonlyError
        container = self._get_container(data)
        return self._save(name, container, data)

    def get(self, name, default=None):
        """
        This method returns None if the entry isn't in the store.
        A path is returned if the entry requested exists and is a binary data.
        SharedDict, SharedList, SharedSet are returned respectively if the entry
        requested is a dict, a list or a set
        """
        if self._deleted:
            raise StoreDeletedError
        self._load_meta()
        info = self._meta.get(name)
        if info is None:
            if default is None:
                return None
            return self.set(name, default)
        container, file_id = info
        filename = self._get_filename(file_id)
        if container == "bin":
            return filename
        data = json_load(filename)
        collection = self._convert_collection(container, data)
        self._bind_save_method(name, collection)
        return collection

    def delete(self, *names):
        """
        This method delete the store if there isn't any argument.
        Else, the arguments are the entries to delete.
        Returns a boolean or raise ReadonlyError
        """
        if self._deleted:
            raise StoreDeletedError
        if self._readonly:
            raise ReadonlyError
        if not valid_store(self._store_path):
            return False
        if not names:  # delete store
            shutil.rmtree(self._store_path)
            self._deleted = True
        else:
            self._load_meta()
            for name in names:
                info = self._meta.get(name)
                if not info:
                    continue
                del self._meta[name]
                container, file_id = info
                filename = self._get_filename(file_id)
                if os.path.isfile(filename):
                    os.remove(filename)
            self._save_meta()
        return True

    def _setup(self):
        self._store_path = os.path.join(self._location, self._name)
        self._meta_filename = os.path.join(self._store_path, "STORE")
        self._create_store()
        self._load_meta()

    def _create_store(self):
        if valid_store(self._store_path):
            return
        # create store
        try:
            os.makedirs(self._store_path)
        except FileExistsError:
            pass
        # create data dir
        try:
            os.mkdir(os.path.join(self._store_path, "data"))
        except FileExistsError:
            pass
        # create meta file
        json_dump(self._meta_filename, dict(), pretty=False)
        # is new store
        self._new = True

    def _load_meta(self):
        self._meta = json_load(self._meta_filename)

    def _save(self, name, container, data):
        info = self._meta.get(name)
        if info is None:
            file_id = self._gen_file_id()
        else:
            _, file_id = info
        filename = self._get_filename(file_id)
        # save metadata
        self._meta[name] = (container, file_id)
        self._save_meta()
        if container == "set":
            data = self._set_to_dict(data)
        if container in ("dict", "list", "set"):
            json_dump(filename, data, pretty=False)
            if (isinstance(data, SharedDict)
                    or isinstance(data, SharedList)
                    or isinstance(data, SharedSet)):
                return data
            cache = self._convert_collection(container, data)
            self._bind_save_method(name, cache)
            return cache
        else:  # "bin"
            with open(filename, "wb") as file:
                file.write(data)
            return filename

    def _save_meta(self):
        json_dump(self._meta_filename, self._meta,
                  pretty=False)

    def _get_container(self, data):
        if isinstance(data, dict):
            container = "dict"
        elif isinstance(data, list):
            container = "list"
        elif isinstance(data, set):
            container = "set"
        else:
            container = "bin"
        return container

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

    def _bind_save_method(self, name, collection):
        collection.save = (lambda self=self:
                           self.set(name, collection))
        if self._autosave:
            collection.on_change = (lambda info: info.collection.save())

    def _set_to_dict(self, data):
        return {item: None for item in data}

    def _get_filename(self, file_id):
        return os.path.join(self._store_path, "data", file_id)

    def _gen_file_id(self):
        while True:
            timestamp = int(time.time())
            file_id = str(timestamp)
            filename = self._get_filename(file_id)
            if not os.path.exists(filename):
                return file_id


class Config(ProbedDict):
    def __init__(self, name, *, readonly=False,
                 autosave=False, default=None,
                 location=DEFAULT_LOCATION):
        self.__name = name
        self.__readonly = readonly
        self.__autosave = autosave
        self.__location = location
        self.__new = False
        self.__deleted = False
        self.__filename = os.path.join(location,
                                       "{}.json".format(name))
        if os.path.isfile(self.__filename):
            data = json_load(self.__filename)
        else:
            data = default if default else dict()
            json_dump(self.__filename, data, pretty=True)
            self.__new = True
        super().__init__(items=data)
        if not self.__readonly and self.__autosave:
            self.on_change = lambda info: info.collection.save()

    @property
    def name(self):
        return self.__name

    @property
    def readonly(self):
        return self.__readonly

    @property
    def autosave(self):
        return self.__autosave

    @property
    def location(self):
        return self.__location

    @property
    def new(self):
        """ Returns True if this store is newly created, else return False """
        return self.__new

    @property
    def deleted(self):
        return self.__deleted

    def save(self):
        """ Save the config """
        if self.__deleted:
            raise JasonDeletedError
        if self.__readonly:
            raise ReadonlyError
        json_dump(self.__filename, self, pretty=True)

    def delete(self):
        """ """
        if self.__deleted:
            raise JasonDeletedError
        if self.__readonly:
            raise ReadonlyError
        if not valid_jason(self.__filename):
            return False
        os.remove(self.__filename)
        self.__deleted = True
        return True


class SharedDict(ProbedDict):
    def save(self):
        raise ReadonlyError


class SharedList(ProbedList):
    def save(self):
        raise ReadonlyError


class SharedSet(ProbedSet):
    def save(self):
        raise ReadonlyError


def json_dump(json_filename, data, pretty=True):
    with open(json_filename, "w") as file:
        if pretty:
            indent, sort_keys = 4, True
        else:
            indent, sort_keys = None, False
        json.dump(data, file, indent=indent, sort_keys=sort_keys)


def json_load(json_filename):
    with open(json_filename, "r") as file:
        data = json.load(file)
    return data


def valid_store(path):
    store_file = os.path.join(path, "STORE")
    data_dir = os.path.join(path, "data")
    if not os.path.isfile(store_file):
        return False
    if not os.path.isdir(data_dir):
        return False
    return True


def valid_jason(path):
    if not os.path.isfile(path):
        return False
    _, ext = os.path.splitext(path)
    if ext != ".json":
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


class StoreDeletedError(Error):
    pass


class JasonDeletedError(Error):
    pass
