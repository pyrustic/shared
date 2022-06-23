"""Shared Data Interface"""
import os
import os.path
import atexit
import time
import shutil
import pathlib
from shared import error, util, dto
from shared.constant import DEFAULT_DIRECTORY


class Dossier:
    """
    Definition of the Dossier class
    """
    def __init__(self, target, *, autosave=False, readonly=False, caching=True,
                 directory=DEFAULT_DIRECTORY, temporary=False):
        """
        Init.

        [parameters]
        - target: target is either the absolute pathname or the basename of the dossier.
        Its datatype is either a string or a pathlib.Path instance.
        - autosave: bool, auto-save mode
        - readonly: bool, readonly mode
        - caching: bool, tell if whether caching should be done or not
        - directory: str, the directory where dossiers will be created.
        By default, this directory is '$HOME/PyrusticHome/shared'.
        If you set None to 'directory', the dossier will be created in a temporary directory.
        - temporary: bool, tells if dossier should be temporary or not
        """
        self._target = target
        self._autosave = autosave
        self._readonly = readonly
        self._caching = caching
        self._directory = directory
        self._temporary = temporary
        self._compact = True
        self._name = None
        self._pathname = None
        self._tempdir = None
        self._meta_filename = None
        self._meta = dict()
        self._cache = dict()
        self._closed = False
        self._deleted = False
        self._new = False
        self._exit_handler_registered = False
        self._setup()

    @property
    def new(self):
        """
        Returns True if this dossier is newly created, else return False
        """
        return self._new

    @property
    def cache(self):
        """Returns the cache"""
        return self._cache

    @property
    def name(self):
        """Returns the name"""
        return self._name

    @property
    def pathname(self):
        """Returns the pathname"""
        return self._pathname

    @property
    def closed(self):
        """Returns the Closed boolean"""
        return self._closed

    @property
    def deleted(self):
        """
        Returns True if this dossier has been deleted through this object
        """
        return self._deleted

    @property
    def target(self):
        """
        Return the target
        """
        return self._target

    @property
    def autosave(self):
        """
        Return the state of the autosave boolean
        """
        return self._autosave

    @property
    def readonly(self):
        """
        Return the state of the readonly boolean
        """
        return self._readonly

    @property
    def caching(self):
        """
        Return the state of the caching boolean
        """
        return self._caching

    @property
    def directory(self):
        """
        Return the directory path (the parent directory of the dossier)
        """
        return self._directory

    @property
    def temporary(self):
        """
        Returns True if this Document is created in a temporary directory.
        The database is created in a temporary directory if you
        assign None to the constructor's "directory" parameter
        """
        return self._temporary

    def set(self, name, data):
        """
        Set an entry.

        [parameters]
        - name: str, the name of the entry
        - data: a dict, a list, a set, binary data, or an instance of pathlib.Path

        [return]
        This method will return the same data if it is a dict, a list, or a set.
        A pathname will be returned if the data saved is binary data.
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            raise error.AlreadyClosedError
        if self._readonly:
            raise error.ReadonlyError
        if data is None:
            msg = "You can't store None."
            raise error.Error(msg)
        data = self._ensure_data(data)
        container = self._get_container(data)
        result = self._save(name, container, data)
        if self._caching and container != "bin":
            self._cache[name] = data
        return result

    def get(self, name, default=None):
        """
        Get an entry.

        [parameters]
        - name: the name of the entry.
        - default: a dict, a list, a set or binary data that will replace a non-existent entry

        [return]
        This method returns None if the entry isn't in the dossier, else it returns a dict, a list,
        or a set.
        A path is returned if the entry requested exists and is a binary data.

        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            raise error.AlreadyClosedError
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
        if self._caching:
            self._cache[name] = data
        return data

    def check(self, name=None):
        """Return basic information about the dossier or a specific entry

        [parameters]
        - name: the name of the specific entry to check. If name is set to None,
        basic information about the dossier will be returned

        [return]
        If there is a specific entry name, returns a namedtuple (container, filename).
        Else returns a dictionary of all entries. Each key represents an entry.
        Example: {"entry_1": namedtuple(container="dict", location="/path/to/contents"), ...}.
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            raise error.AlreadyClosedError
        self._load_meta()
        if name:
            info = self._meta.get(name)
            return self._get_entry_info_dto(name, info)
        cache = dict()
        for name, info in self._meta.items():
            cache[name] = self._get_entry_info_dto(name, info)
        return cache

    def close(self):
        """
        This method closes the access to the document.
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            return False
        self._unregister_exit_handler()
        if self._tempdir:
            self._tempdir.cleanup()
        elif self._autosave:
            self._save_cache()
        self._cache = None
        self._closed = True
        return True

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
            return False
        if self._closed:
            raise error.AlreadyClosedError
        if self._readonly:
            raise error.ReadonlyError
        if not util.valid_dossier(self._name, self._directory):
            return False
        if not names:  # delete dossier
            self._delete_dossier()
        else:  # delete specific entries
            self._delete_specific_entries(names)
        return True

    def _setup(self):
        self._update_variables()
        self._make_directory()
        self._meta_filename = os.path.join(self._pathname, "DOSSIER")
        self._create_dossier()
        self._load_meta()
        if self._autosave:
            if not self._caching:
                msg = "Autosave works only with `caching` set to True"
                raise error.Error(msg)
            self._register_exit_handler()

    def _update_variables(self):
        info = util.check_target(self._target, self._directory, self._temporary)
        self._name, self._directory, self._pathname, self._tempdir = info

    def _make_directory(self):
        if self._temporary:
            return
        try:
            os.makedirs(self._directory)
        except FileExistsError:
            pass

    def _create_dossier(self):
        if util.valid_dossier(self._name, self._directory):
            return
        # create dossier folder
        try:
            os.makedirs(self._pathname)
        except FileExistsError:
            pass
        # create data dir inside dossier folder
        try:
            os.mkdir(os.path.join(self._pathname, "data"))
        except FileExistsError:
            pass
        # create meta file
        util.json_dump(self._meta_filename, dict(), pretty=self._compact)
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
            data = self._convert_set_into_dict(data)
        # dict, list, set
        if container in ("dict", "list", "set"):
            self._save_collection(filename, data)
            return data
        # "bin"
        self._save_bin(filename, data)
        return filename

    def _get_file_id(self, name):
        info = self._meta.get(name)
        if info is None:
            file_id = self._gen_file_id()
        else:
            _, file_id = info
        return file_id

    def _save_collection(self, filename, data):
        util.json_dump(filename, data, pretty=self._compact)

    def _save_bin(self, filename, data):
        with open(filename, "wb") as file:
            file.write(data)

    def _save_meta(self):
        util.json_dump(self._meta_filename, self._meta,
                       pretty=self._compact)

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

    def _ensure_data(self, data):
        if isinstance(data, pathlib.Path):
            with open(data.resolve(), "rb") as file:
                return file.read()
        return data

    def _convert_set_into_dict(self, data):
        return {item: None for item in data}

    def _get_filename(self, file_id):
        return os.path.join(self._pathname, "data", file_id)

    def _gen_file_id(self):
        while True:
            timestamp = int(time.time())
            file_id = str(timestamp)
            filename = self._get_filename(file_id)
            if not os.path.exists(filename):
                return file_id

    def _get_entry_info_dto(self, name, info):
        if info is None:
            return None
        container, file_id = info
        filename = self._get_filename(file_id)
        return dto.DossierEntryInfo(name, container, filename)

    def _register_exit_handler(self):
        if self._exit_handler_registered:
            return
        atexit.register(self._exit_handler)
        self._exit_handler_registered = True

    def _unregister_exit_handler(self):
        if not self._exit_handler_registered:
            return
        atexit.unregister(self._exit_handler)
        self._exit_handler_registered = False

    def _save_cache(self):
        if not self._cache:
            return False
        for key, value in self._cache:
            self.set(key, value)
        return True

    def _delete_dossier(self):
        shutil.rmtree(self._pathname)
        if self._tempdir:
            self._tempdir.cleanup()
        self._autosave = False
        self.close()
        self._deleted = True

    def _delete_specific_entries(self, names):
        self._load_meta()
        for name in names:
            info = self._meta.get(name)
            if not info:
                continue
            del self._meta[name]
            if name in self._cache:
                del self._cache[name]
            container, file_id = info
            filename = self._get_filename(file_id)
            if os.path.isfile(filename):
                os.remove(filename)
        self._save_meta()

    def _exit_handler(self):
        self._unregister_exit_handler()
        if not self._closed:
            self._save_cache()
