import os
import os.path
import atexit
import jesth
from tempfile import TemporaryDirectory
from shared import error
from shared import util
from shared.constant import DEFAULT_DIRECTORY


def create(target, *, default=None, file_format=None, directory=DEFAULT_DIRECTORY):
    document = Document(target, default=default, autosave=False,
                        readonly=False, caching=False, file_format=file_format,
                        directory=directory, temporary=False)
    document.close()


def readonly(target, *, default=None, file_format=None, directory=DEFAULT_DIRECTORY):
    document = Document(target, default=default, autosave=False,
                        readonly=False, caching=False, file_format=file_format,
                        directory=directory, temporary=False)
    data = document.read()
    document.close()
    return data


def write(target, data, *, file_format=None, directory=DEFAULT_DIRECTORY):
    document = Document(target, default=None, autosave=False,
                        readonly=False, caching=False, file_format=file_format,
                        directory=directory, temporary=False)
    document.write(data)
    document.close()


def autosave(target, *, default=None, file_format=None, directory=DEFAULT_DIRECTORY):
    document = Document(target, default=default, autosave=True,
                        readonly=False, caching=True, file_format=file_format,
                        directory=directory, temporary=False)
    return document.read()


class Document:
    def __init__(self, target, *, default=None,
                 autosave=False, readonly=False,
                 caching=True, file_format=None,
                 directory=DEFAULT_DIRECTORY,
                 temporary=False):
        """
        Init.

        [parameters]
        - target: target is either the absolute pathname or the basename of a file.
        Its datatype is either a string or a pathlib.Path instance.
        - default: default value for this document file.
        If the document is newly created, the default value will populate it. If you don't set a default value, a dict will be the default value.
        - autosave: boolean to say if you want to activate the autosave feature or not
        - readonly: boolean to say if you want to open this document in readonly mode or not
        - caching: boolean to set if whether data should be cached or not
        - directory: the directory where you want to store the document.
        By default, the directory is "$HOME/PyrusticHome/shared". If you set None to directory,
        the document will be created in a temporary directory
        - temporary: boolean to tell if either you want this document to be temporary or not
        - error_module: module containing these Exceptions classes: AlreadyClosedError, , AlreadyDeletedError, and ReadonlyError
        """
        self._target = target
        self._readonly = readonly
        self._autosave = autosave
        self._default = dict() if default is None else default
        self._caching = caching
        self._file_format = file_format
        self._directory = directory
        self._temporary = temporary
        self._name = None
        self._tempdir = None
        self._new = False
        self._deleted = False
        self._closed = False
        self._pathname = None
        self._temporary = False
        self._cache = None
        self._exit_handler_registered = False
        self._is_json = None
        self._setup()

    @property
    def new(self):
        """
        Returns True if this dossier is newly created, else return False
        """
        return self._new

    @property
    def cache(self):
        """
        Returns the cached contents of the document.
        Returns None if caching is set to False.
        """
        return self._cache

    @property
    def name(self):
        return self._name

    @property
    def pathname(self):
        return self._pathname

    @property
    def closed(self):
        return self._closed

    @property
    def deleted(self):
        """
        Return True if this document file is deleted else return False
        """
        return self._deleted

    @property
    def target(self):
        """
        Return the target
        """
        return self._target

    @property
    def default(self):
        """Returns the default value"""
        return self._default

    @property
    def autosave(self):
        """
        Return the autosave boolean state
        """
        return self._autosave

    @property
    def readonly(self):
        """
        Return the readonly boolean state
        """
        return self._readonly

    @property
    def caching(self):
        """Returns the caching boolean"""
        return self._caching

    @property
    def file_format(self):
        return self._file_format

    @property
    def directory(self):
        """
        Return the value of the location variable
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

    def write(self, data):
        """
        Set the contents of the JSON file. Returns the same data
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            raise error.AlreadyClosedError
        if self._readonly:
            raise error.ReadonlyError
        if self._caching:
            self._cache = data
        self._write(data)
        return data

    def read(self):
        """
        Load data from the document
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            raise error.AlreadyClosedError
        data = self._read()
        if self._caching:
            self._cache = data
        return data

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

    def delete(self):
        """
        This method deletes the document.
        Returns a boolean or raise ReadonlyError
        """
        if self._deleted:
            return False
        if self._closed:
            raise error.AlreadyClosedError
        if self._readonly:
            raise error.ReadonlyError
        self._autosave = False
        self.close()
        if not os.path.isfile(self._pathname):
            return False
        os.remove(self._pathname)
        self._deleted = True
        return True

    def _setup(self):
        self._update_variables()
        self._check_file_format()
        self._make_directory()
        self._init_file()
        if self._autosave:
            self._caching = True
            self._register_exit_handler()

    def _update_variables(self):
        info = util.check_target(self._target, self._directory, self._temporary)
        self._name, self._directory, self._pathname, self._tempdir = info

    def _check_file_format(self):
        self._is_json = False
        if self._file_format is None:
            _, ext = os.path.splitext(self._pathname)
            self._is_json = True if ext.lower() == ".json" else False
        elif self._file_format.lower() == "json":
            self._is_json = True
        elif self._file_format.lower() == "jesth":
            self._is_json = False
        else:
            msg = "Unknown file format {} !".format(self._file_format)
            raise error.Error(msg)

    def _make_directory(self):
        if self._temporary:
            return
        try:
            os.makedirs(self._directory)
        except FileExistsError:
            pass

    def _init_file(self):
        self._pathname = os.path.join(self._directory,
                                      self._name)
        if not os.path.isfile(self._pathname):
            self._write(self._default)
            self._new = True
            if self._caching:
                self._cache = self._default

    def _save_cache(self):
        if self._cache is None:
            return False
        self.write(self._cache)
        return True

    def _register_exit_handler(self):
        if self._exit_handler_registered:
            return False
        atexit.register(self._exit_handler)
        self._exit_handler_registered = True
        return True

    def _unregister_exit_handler(self):
        if not self._exit_handler_registered:
            return False
        atexit.unregister(self._exit_handler)
        self._exit_handler_registered = False
        return True

    def _exit_handler(self):
        self._unregister_exit_handler()
        if not self._closed:
            self._save_cache()

    def _read(self):
        if self._is_json:
            return util.json_load(self._pathname)
        return jesth.read(self._pathname, compact=False,
                          split_body=True)

    def _write(self, data):
        if self._is_json:
            return util.json_dump(self._pathname, data, pretty=True)
        return jesth.write(data, self._pathname)


class OldDocument: # TODO DEPRECATED
    """
    Definition of the Document class
    """
    def __init__(self, name, *, readonly=False,
                 autosave=True, default=None,
                 caching=True, pretty_json=True,
                 directory=DEFAULT_DIRECTORY):
        """
        Init.

        [parameters]
        - name: string, the name of the document file. Example: "data.json"
        - readonly: boolean to say if you want to open this document in readonly mode or not
        - autosave: boolean to say if you want to activate the autosave feature or not
        - default: default value for this document file.
        If the document is newly created, the default value will populate it.
        - caching: boolean to set if whether data should be cached or not
        - pretty_json: boolean to tell if either json should be indented or not
        - directory: the directory where you want to store the document.
        By default, the directory is "$HOME/PyrusticHome/shared". If you set None to directory,
        the document will be created in a temporary directory
        """
        self._name = name
        self._readonly = readonly
        self._autosave = autosave
        self._default = default
        self._caching = caching
        self._pretty_json = pretty_json
        self._directory = directory
        self._tempdir = None
        self._new = False
        self._deleted = False
        self._closed = False
        self._filename = None
        self._temporary = False
        self._cache = None
        self._atexit_callback_registered = False
        self._setup()

    @property
    def cache(self):
        """
        Returns the cached contents of the document.
        Returns None if caching is set to False.
        """
        return self._cache

    @property
    def closed(self):
        return self._closed

    @property
    def deleted(self):
        """
        Return True if this document file is deleted else return False
        """
        return self._deleted

    @property
    def name(self):
        """
        Return the name of the document file
        """
        return self._name

    @property
    def readonly(self):
        """
        Return the readonly boolean state
        """
        return self._readonly

    @property
    def autosave(self):
        """
        Return the autosave boolean state
        """
        return self._autosave

    @property
    def default(self):
        """Returns the default value"""
        return self._default

    @property
    def caching(self):
        """Returns the caching boolean"""
        return self._caching

    @property
    def pretty_json(self):
        """Return the value of pretty_json"""
        return self._pretty_json

    @property
    def directory(self):
        """
        Return the value of the location variable
        """
        return self._directory

    @property
    def new(self):
        """
        Returns True if the underlying document file is newly created, else return False
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

    def write(self, data):
        """
        Set the contents of the JSON file. Returns the same data
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            raise error.AlreadyClosedError
        if self._readonly:
            raise error.ReadonlyError
        if self._caching:
            self._cache = data
        self._dump(data)
        return data

    def read(self):
        """
        Load data from the document
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            raise error.AlreadyClosedError
        data = self._load()
        if self._caching:
            self._cache = data
        return data

    def close(self):
        """
        This method closes the access to the document.
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._closed:
            return False
        self._unregister_atexit_callback()
        if self._tempdir:
            self._tempdir.cleanup()
        elif self._autosave:
            self._save_cache()
        self._cache = None
        self._closed = True
        return True

    def delete(self):
        """
        This method deletes the document.
        Returns a boolean or raise ReadonlyError
        """
        if self._deleted:
            return False
        if self._closed:
            raise error.AlreadyClosedError
        if self._readonly:
            raise error.ReadonlyError
        self._autosave = False
        self.close()
        if not os.path.isfile(self._filename):
            return False
        os.remove(self._filename)
        self._deleted = True
        return True

    def _setup(self):
        self._ensure_name_and_directory()
        self._filename = os.path.join(self._directory,
                                      self._name)
        if not os.path.isfile(self._filename):
            data = self._default
            if data is not None:
                self._dump(data)
            self._new = True
            if self._caching:
                self._cache = data
        if self._autosave:
            if not self._caching:
                msg = "Autosave works only with `caching` set to True"
                raise error.Error(msg)
            self._register_atexit_callback()

    def _ensure_name_and_directory(self):
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

    def _load(self):
        # load json
        return util.json_load(self._filename)

    def _dump(self, data):
        # dump json
        return util.json_dump(self._filename, data, pretty=self._pretty_json)

    def _save_cache(self):
        if self._cache is None:
            return False
        self.write(self._cache)
        return True

    def _register_atexit_callback(self):
        if self._atexit_callback_registered:
            return
        atexit.register(self._on_exit)
        self._atexit_callback_registered = True

    def _unregister_atexit_callback(self):
        if not self._atexit_callback_registered:
            return
        atexit.unregister(self._on_exit)
        self._atexit_callback_registered = False

    def _on_exit(self):
        self._unregister_atexit_callback()
        if not self._closed:
            self._save_cache()
