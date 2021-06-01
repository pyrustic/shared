import os
import os.path
import shutil
import json
import time
from probed import ProbedDict, ProbedList, ProbedSet


DEFAULT_PATH = os.path.join(os.path.expanduser("~"),
                            "PyrusticData", "shared")


class Shared:
    def __init__(self, store, path=DEFAULT_PATH,
                 readonly=False):
        """
        An easy and intuitive way to store your data collections !

        Parameters:
            - store: str, the name of the store, just give the app name
            - path: str, the directory where to save data, by default
            it is the path ~/PyrusticData/datastore
            - readonly: bool
        """
        self._store = store
        self._path = path
        self._readonly = readonly
        self._dict = ProbedDict()
        self._list = ProbedList()
        self._set = ProbedSet()
        self._bin = ProbedDict()
        self._store_path = None
        self._dict_json_filename = None
        self._list_json_filename = None
        self._set_json_filename = None
        self._bin_json_filename = None
        self._setup()

    # ======= PROPERTIES =======

    @property
    def store(self):
        return self._store

    @property
    def path(self):
        return self._path

    @property
    def readonly(self):
        return self._readonly

    @property
    def exists(self):
        if os.path.exists(self._store_path):
            return True
        return False

    @property
    def dict(self):
        return self._dict

    @dict.setter
    def dict(self, val):
        if not isinstance(val, ProbedDict):
            val = ProbedDict(items=val)
        self._dict = val
        self._dict.changed = True

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, val):
        if not isinstance(val, ProbedList):
            val = ProbedList(items=val)
        self._list = val
        self._list.changed = True

    @property
    def set(self):
        return self._set

    @set.setter
    def set(self, val):
        if not isinstance(val, ProbedSet):
            val = ProbedSet(items=val)
        self._set = val
        self._set.changed = True

    @property
    def bin(self):
        """ Getter only + Returns a copy """
        return self._bin.copy()

    # ======= PUBLIC METHODS =======

    def reload(self):
        if not os.path.exists(self._store_path):
            return
        # Load data from json then populate variables
        cache = self._json_load(self._dict_json_filename)
        self._dict = ProbedDict(items=cache)
        cache = self._json_load(self._list_json_filename)
        self._list = ProbedList(items=cache)
        cache = set(self._json_load(self._set_json_filename))
        self._set = ProbedSet(items=cache)
        cache = self._json_load(self._bin_json_filename)
        self._bin = ProbedDict(items=cache)

    def save(self):
        if self._readonly:
            raise ReadonlyError
        if self._dict.changed:
            self._save_dict()
            self._dict.changed = False
        if self._list.changed:
            self._save_list()
            self._list.changed = False
        if self._set.changed:
            self._save_set()
            self._set.changed = False

    def add_bin(self, name, data):
        if self._readonly:
            raise ReadonlyError
        bin_dir = os.path.join(self._store_path, "bin")
        if not os.path.exists(bin_dir):
            os.makedirs(bin_dir)
        if name in self._bin:
            filename = self._bin[name]
        else:
            filename = self._new_bin_filename(bin_dir)
        with open(filename, "wb") as file:
            file.write(data)
        self._bin[name] = filename
        self._save_bin()

    def del_bin(self, name=None):
        if self._readonly:
            raise ReadonlyError
        if name is None:
            for name, path in self._bin.items():
                self._del_bin(path)
            self._bin = dict()
        else:
            try:
                self._del_bin(self._bin[name])
                del self._bin[name]
            except KeyError as e:
                pass
        self._json_dump(self._bin_json_filename, self._bin)

    def del_store(self):
        if self._readonly:
            raise ReadonlyError
        if self._deletable_store():
            shutil.rmtree(self._store_path)

    # ======= PRIVATE =======

    def _setup(self):
        """
        Make store directory, init json files,
        set instances json filenames
        """
        self._store_path = os.path.join(self._path, self._store)
        self._create_store()
        self.reload()

    def _create_store(self):
        if not self._readonly and not os.path.exists(self._store_path):
            os.makedirs(self._store_path)
            # create bin folder
            os.mkdir(os.path.join(self._store_path, "bin"))
            # add pyrustic file
            cache = os.path.join(self._store_path, "pyrustic")
            with open(cache, "w") as file:
                pass
            # add shared file
            cache = os.path.join(self._store_path, "shared")
            with open(cache, "w") as file:
                pass
        cache = [("dict", dict()), ("list", list()),
                 ("set", dict()), ("bin", dict())]
        for container, default in cache:
            filename = os.path.join(self._store_path,
                                    "{}.json".format(container))
            if not os.path.exists(filename) and not self._readonly:
                self._json_dump(filename, default)
            if container == "dict":
                self._dict_json_filename = filename
            elif container == "list":
                self._list_json_filename = filename
            elif container == "set":
                self._set_json_filename = filename
            elif container == "bin":
                self._bin_json_filename = filename
            else:
                raise Error("Unknown category {}".format(container))

    def _set_to_dict(self, data):
        return {item: None for item in data}

    def _save_dict(self):
        self._json_dump(self._dict_json_filename, self._dict)

    def _save_list(self):
        self._json_dump(self._list_json_filename, self._list)

    def _save_set(self):
        data = self._set_to_dict(self._set)
        self._json_dump(self._set_json_filename, data)

    def _save_bin(self):
        self._json_dump(self._bin_json_filename, self._bin)

    def _del_bin(self, path):
        if path and os.path.isfile(path):
            # let's be sure before deleting this poor file ;)
            if self._deletable_bin(path):
                os.remove(path)
            else:
                raise Error("Illegal filename {}".format(path))

    def _deletable_bin(self, path):
        basename = os.path.basename(path)
        seq = basename.split("-")
        if len(seq) == 2 and seq[0] == "bin":
            return True
        return False

    def _deletable_store(self):
        store_content = os.listdir(self._store_path)
        important_items = ("pyrustic", "shared", "bin", "bin.json"
                           "dict.json", "list.json", "set.json")
        for item in important_items:
            if item not in store_content:
                return False
        return True

    def _json_load(self, json_filename):
        with open(json_filename, "r") as file:
            data = json.load(file)
        return data

    def _json_dump(self, json_filename, data):
        with open(json_filename, "w") as file:
            json.dump(data, file, indent=4, sort_keys=True)

    def _new_bin_filename(self, bin_dir):
        while True:
            timestamp = int(time.time())
            var = "bin-{}".format(str(timestamp))
            filename = os.path.join(bin_dir, var)
            if not os.path.exists(filename):
                return filename


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ReadonlyError(Error):
    pass
