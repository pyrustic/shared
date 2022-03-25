"""Shared Data Interface"""
import os
import os.path
import time
import shutil
import pathlib
from tempfile import TemporaryDirectory
from probed import ProbedDict, ProbedList, ProbedSet
from shared import error
from shared import util
from shared.constant import DEFAULT_DIRECTORY


class Dossier:
    """
    Definition of the Dossier class
    """
    def __init__(self, name, *, readonly=False, autosave=False,
                 pretty_json=False, directory=DEFAULT_DIRECTORY):
        """
        Init.

        [parameters]
        - name: str, the name of the dossier
        - readonly: bool, readonly mode
        - autosave: bool, auto-save mode
        - pretty_json: bool, tell if whether you want JSON files to be indented or not
        - directory: str, the directory where dossiers will be created.
        By default, this directory is '$HOME/PyrusticHome/shared'.
        If you set None to 'directory', the dossier will be created in a temporary directory.
        """
        self._name = name
        self._readonly = readonly
        self._autosave = autosave
        self._pretty_json = pretty_json
        self._directory = directory
        self._dossier_path = None
        self._meta_filename = None
        self._meta = dict()
        self._cache = dict()
        self._deleted = False
        self._new = False
        self._temporary = False
        self._tempdir = None
        self._setup()

    @property
    def new(self):
        """
        Returns True if this dossier is newly created, else return False
        """
        return self._new

    @property
    def temporary(self):
        """
        Returns True if this Document is created in a temporary directory.
        The database is created in a temporary directory if you
        assign None to the constructor's "directory" parameter
        """
        return self._temporary

    @property
    def deleted(self):
        """
        Returns True if this dossier has been deleted through this object
        """
        return self._deleted

    @property
    def name(self):
        """
        Return the name of the dossier
        """
        return self._name

    @property
    def readonly(self):
        """
        Return the state of the readonly boolean
        """
        return self._readonly

    @property
    def autosave(self):
        """
        Return the state of the autosave boolean
        """
        return self._autosave

    @property
    def pretty_json(self):
        """Return the value of pretty_json"""
        return self._pretty_json

    @property
    def directory(self):
        """
        Return the directory path (the parent directory of the dossier)
        """
        return self._directory

    def set(self, name, data):
        """
        Set an entry.

        [parameters]
        - name: str, the name of the entry
        - data: a dict, a list, a set, binary data, or an instance of pathlib.Path

        [return]
        This method will return a path if the entry is a binary data.
        SharedDict, SharedList, SharedSet are returned respectively if the entry
        is a dict, a list or a set, respectively, and if autosave is True.
        You can call the method "save" on the instances of SharedDict, SharedList,
        or SharedSet.
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        if data is None:
            msg = "You can't store None."
            raise error.Error(msg)
        data = self._ensure_data(data)
        container = self._get_container(data)
        return self._save(name, container, data)

    def get(self, name, default=None):
        """
        Get an entry.

        [parameters]
        - name: the name of the entry.
        - default: a dict, a list, a set or binary data to return if the entry doesn't exist.

        [return]
        This method returns None if the entry isn't in the dossier.
        A path is returned if the entry requested exists and is a binary data.
        SharedDict, SharedList, SharedSet are returned respectively if the entry
        requested is a dict, a list or a set, respectively, and if autosave is set to True
        """
        if self._deleted:
            raise error.AlreadyDeletedError
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
        data = util.json_load(filename)
        return self._ensure_autosave(name, container, data)

    def check(self, name=None):
        """Return basic information about the dossier or a specific entry

        [parameters]
        - name: the name of the specific entry to check. If name is set to None,
        basic information about the dossier will be returned

        [return]
        If there is a specific entry name, returns a tuple (container, filename).
        Else returns a dictionary. Each key represents an entry.
        Example: {"entry_1": ("dict", "/path/to/contents"), ...}.

        """
        if self._deleted:
            raise error.AlreadyDeletedError
        self._load_meta()
        if name:
            info = self._meta.get(name)
            return self._check_info(info)
        cache = dict()
        for name, info in self._meta.items():
            cache[name] = self._check_info(info)
        return cache

    def delete(self, *names):
        """
        This method deletes the dossier if there isn't any argument.
        Else, the arguments are the entries to delete.

        [parameters]
        - *names: names of entries to delete.
        If you don't set a name, the dossier will be deleted

        [return]
        Returns a boolean or raise ReadonlyError
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        if not util.valid_dossier(self._name, self._directory):
            return False
        if not names:  # delete dossier
            shutil.rmtree(self._dossier_path)
            if self._tempdir:
                self._tempdir.cleanup()
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
        self._ensure_directory()
        self._dossier_path = os.path.join(self._directory, self._name)
        self._meta_filename = os.path.join(self._dossier_path, "DOSSIER")
        self._create_dossier()
        self._load_meta()

    def _ensure_directory(self):
        if self._directory:
            try:
                os.makedirs(self._directory)
            except FileExistsError:
                pass
        else:
            # Turn on Temporary Mode if self._directory is set to None
            self._tempdir = TemporaryDirectory()
            self._directory = self._tempdir.name
            self._temporary = True

    def _create_dossier(self):
        if util.valid_dossier(self._name, self._directory):
            return
        # create dossier folder
        try:
            os.makedirs(self._dossier_path)
        except FileExistsError:
            pass
        # create data dir inside dossier folder
        try:
            os.mkdir(os.path.join(self._dossier_path, "data"))
        except FileExistsError:
            pass
        # create meta file
        util.json_dump(self._meta_filename, dict(), pretty=self._pretty_json)
        # is new dossier
        self._new = True

    def _load_meta(self):
        self._meta = util.json_load(self._meta_filename)

    def _save(self, name, container, data):
        file_id = self._get_file_id(name)
        filename = self._get_filename(file_id)
        # save metadata
        self._meta[name] = (container, file_id)
        self._save_meta()
        if container == "set":
            data = self._set_to_dict(data)
        if container in ("dict", "list", "set"):
            return self._save_collection(name, container, data, filename)
        else:  # "bin"
            with open(filename, "wb") as file:
                file.write(data)
            return filename

    def _save_collection(self, name, container, data, filename):
        util.json_dump(filename, data, pretty=self._pretty_json)
        if (isinstance(data, ProbedDict)
                or isinstance(data, ProbedList)
                or isinstance(data, ProbedSet)):
            self._update_on_change_callback(name, data)
            return data
        return self._ensure_autosave(name, container, data)

    def _get_file_id(self, name):
        info = self._meta.get(name)
        if info is None:
            file_id = self._gen_file_id()
        else:
            _, file_id = info
        return file_id

    def _save_meta(self):
        util.json_dump(self._meta_filename, self._meta,
                       pretty=self._pretty_json)

    def _get_container(self, data):
        if isinstance(data, dict):
            container = "dict"
        elif isinstance(data, list):
            container = "list"
        elif isinstance(data, set):
            container = "set"
        elif isinstance(data, bytes):
            container = "bin"
        else:
            msg = "Allowed types are: dict, list, set, bytes, and pathlib.Path instance"
            raise error.Error(msg)
        return container

    def _ensure_autosave(self, name, container, data):
        if not self._autosave or data is None:
            return data
        if container == "dict":
            cache = ProbedDict(items=data)
        elif container == "list":
            cache = ProbedList(items=data)
        elif container == "set":
            cache = ProbedSet(items=data)
        else:
            raise error.Error("Unknown container '{}'.".format(container))
        self._update_on_change_callback(name, cache)
        return cache

    def _ensure_data(self, data):
        if isinstance(data, pathlib.Path):
            with open(data.resolve(), "rb") as file:
                return file.read()
        return data

    def _update_on_change_callback(self, name, probed_collection):
        probed_collection.on_change = (lambda context, self=self,
                                              name=name, data=probed_collection:
                                       self.set(name, data))

    def _set_to_dict(self, data):
        return {item: None for item in data}

    def _get_filename(self, file_id):
        return os.path.join(self._dossier_path, "data", file_id)

    def _gen_file_id(self):
        while True:
            timestamp = int(time.time())
            file_id = str(timestamp)
            filename = self._get_filename(file_id)
            if not os.path.exists(filename):
                return file_id

    def _check_info(self, info):
        if info is None:
            return None
        container, file_id = info
        filename = self._get_filename(file_id)
        return container, filename