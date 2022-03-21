import os
import os.path
import pathlib
import hackernote
from tempfile import TemporaryDirectory
from probed import ProbedDict, ProbedList
from shared import error
from shared import util
from shared import constant
from shared.constant import DEFAULT_DIRECTORY


class Document:
    """
    Definition of the Document class
    """
    def __init__(self, name, *, readonly=False,
                 autosave=False, default=None, file_format="auto",
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
        - file_format: "auto" or "json" or "hackernote". If the value is "auto",
         the document will be considered as a JSON file if its extension is ".json",
         otherwise it will be considered as a hackernote.
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
        self._file_format = file_format
        self._caching = caching
        self._pretty_json = pretty_json
        self._directory = directory
        self._tempdir = None
        self._new = False
        self._deleted = False
        self._filename = None
        self._temporary = False
        self._cache = None
        self._setup()

    @property
    def cache(self):
        """
        Returns the cached contents of the document.
        Returns None if caching is set to False.
        """
        return self._cache

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
    def file_format(self):
        """Returns the file format (either 'hackernote' or 'json')"""
        return self._file_format

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

    def set(self, data):
        """
        Set the contents of the JSON file or hackernote file.
        Return the same data or the probed version of the data if autosave is True.
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        data = self._ensure_autosave(data)
        if self._caching:
            self._cache = data
        self._dump(data)
        return data

    def get(self):
        """
        Load data from the document
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        data = self._load()
        data = self._ensure_autosave(data)
        if self._caching:
            self._cache = data
        return data

    def delete(self):
        """
        This method delete the document.
        Returns a boolean or raise ReadonlyError
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        if not os.path.isfile(self._filename):
            return False
        os.remove(self._filename)
        if self._tempdir:
            self._tempdir.cleanup()
        self._deleted = True
        self._cache = None
        return True

    def _setup(self):
        self._ensure_name_and_directory()
        self._filename = os.path.join(self._directory,
                                      self._name)
        self._check_format()
        if not os.path.isfile(self._filename):
            data = self._default
            if data is not None:
                self._dump(data)
            self._new = True
            if self._caching:
                self._cache = self._ensure_autosave(data)

    def _ensure_autosave(self, data):
        if not self._autosave or data is None:
            return data
        if isinstance(data, dict):
            data = ProbedDict(items=data)
        elif isinstance(data, list):
            data = ProbedList(items=data)
        else:
            raise error.Error("Unknown data type")
        data.on_change = (lambda context, self=self, data=data: self.set(data))
        return data

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

    def _check_format(self):
        if self._file_format not in constant.VALID_DOCUMENT_FILE_FORMATS:
            msg = "Unknown '{}' file format.".format(self._file_format)
            raise error.Error(msg)
        if self._file_format == "auto":
            _, ext = os.path.splitext(self._filename)
            self._file_format = "json" if ext.lower() == ".json" else "hackernote"

    def _load(self):
        # load json
        if self._file_format == "json":
            return util.json_load(self._filename)
        # load hackernote
        path = pathlib.Path(self._filename)
        return hackernote.parse(path)

    def _dump(self, data):
        # dump json
        if self._file_format == "json":
            return util.json_dump(self._filename, data, pretty=self._pretty_json)
        # dump hackernote
        hackernote.render(data, destination=self._filename)
