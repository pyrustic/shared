import os
import os.path
import atexit
import threading
import pathlib
import sqlite3 as sqlite
from shared.constant import DEFAULT_DIRECTORY
from shared import error, dto, util


class Database:
    """
    Definition of the Database class
    """
    def __init__(self, target, *, init_script=None, readonly=False,
                 directory=DEFAULT_DIRECTORY, temporary=False,
                 raise_exception=True, raise_warning=True,
                 connection_kwargs=None):
        """
        Init

        [parameters]
        - target: target is either the absolute pathname or the basename of a file.
        Its datatype is either a string or a pathlib.Path instance.

        - init_script: a path to a file (an instance of pathlib.Path),
         a file-like object or a string of sql code.
            Example_a: "CREATE TABLE my_table(id INTEGER NOT NULL PRIMARY KEY);".
            Example_b: pathlib.Path("/path/to/script.sql").

        - readonly: boolean to set the database in the read-only state

        - directory: path to directory where the database will be created.
        Set directory to None if you want the database to be created in memory.

        - raise_exception: By default, True, so exceptions (sqlite.Error) will be raised

        - raise_warning: By default, True, so exceptions (sqlite.Warning) will be raised

        - connection_kwargs: connections arguments used while calling the
         method "sqlite.connect()"
        """
        self._target = target
        self._init_script = init_script
        self._readonly = readonly
        self._directory = directory
        self._temporary = temporary
        self._raise_exception = raise_exception
        self._raise_warning = raise_warning
        self._connection_kwargs = connection_kwargs if connection_kwargs else dict()
        self._name = None
        self._pathname = None
        self._lock = threading.Lock()
        self._connection = None
        self._closed = False
        self._deleted = False
        self._new = False
        self._setup()

    # ====================================
    #              PROPERTIES
    # ====================================

    @property
    def connection(self):
        """
        Connection object
        """
        return self._connection

    @property
    def new(self):
        """
        Returns True if the database has just been created, otherwise returns False
        """
        return self._new

    @property
    def temporary(self):
        """Returns True if the database is created in memory.
        The database is created in memory if you assign None to the
        constructor's "directory" parameter"""
        return self._temporary

    @property
    def closed(self):
        """Boolean to tell if whether this database is closed or not"""
        return self._closed

    @property
    def deleted(self):
        """Boolean to tell if whether this database is deleted or not"""
        return self._deleted

    @property
    def name(self):
        """Returns the name of this database"""
        return self._name

    @property
    def readonly(self):
        """Returns the readonly boolean"""
        return self._readonly

    @property
    def init_script(self):
        """Returns the initialization script"""
        return self._init_script

    @property
    def directory(self):
        """Returns the directory"""
        return self._directory

    # ====================================
    #            PUBLIC METHODS
    # ====================================
    def check(self):
        """
        Test the database

        [return]
        Returns True if this is a legal database, otherwise returns False
        """
        if self._deleted:
            return False
        cache = self._raise_exception
        self._raise_exception = True
        legal = True
        try:
            self.get_tables()
        except sqlite.Error as e:
            legal = False
        except sqlite.Warning as e:
            legal = False
        self._raise_exception = cache
        return legal

    def edit(self, sql, param=None):
        """
        Use this method to edit your database.
        Formally: Data Definition Language (DDL) and Data Manipulation Language (DML).

        [parameters]
        - sql: str, the sql code
        - param: a list of parameters to fill the "?" in the sql code

        [return]
        It returns True or False or raises sqlite.Error, sqlite.Warning
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        with self._lock:
            param = () if param is None else param
            result = True
            cur = None
            try:
                cur = self._connection.cursor()
                cur.execute(sql, param)
                self._connection.commit()
            except sqlite.Error as e:
                result = False
                if self._raise_exception:
                    raise
            except sqlite.Warning as e:
                result = False
                if self._raise_warning:
                    raise
            finally:
                if cur:
                    cur.close()
            return result

    def query(self, sql, param=None):
        """
        Use this method to query your database.
        Formally: Data Query Language (DQL)
        It returns a namedtuple: (columns, data).
        Columns is a list of strings, columns names.
        Data is a list with data from ur query.
            Example:
                namedtuple(columns=["id", "name", "age"],
                        data= ( [1, "Jack", 50], ...) )
        This method can raise sqlite.Error, sqlite.Warning
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        with self._lock:
            param = () if param is None else param
            description = []
            data = []
            cur = None
            try:
                cur = self._connection.cursor()
                cur.execute(sql, param)
                data = cur.fetchall()
                description = cur.description
            except sqlite.Error as e:
                if self._raise_exception:
                    raise
            except sqlite.Warning as e:
                if self._raise_warning:
                    raise
            finally:
                if cur:
                    cur.close()
            columns = [x[0] for x in description]
            return dto.QueryResult(columns, data)

    def script(self, script):
        """
        Executes the script as a sql-script. Meaning: there are multiple lines of sql.
        This method returns nothing but could raise sqlite.Error, sqlite.Warning.

        script could be a path (pathlib.Path) to a file, a file-like object or just a string.
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        with self._lock:
            cur = None
            try:
                script = self._stringify_script(script)
                cur = self._connection.cursor()
                cur.executescript(script)
            except sqlite.Error as e:
                if self._raise_exception:
                    raise
            except sqlite.Warning as e:
                if self._raise_warning:
                    raise
            finally:
                if cur:
                    cur.close()

    def export(self, destination=None):
        """
        export the database: it returns a string of sql code.
        This method can raise sqlite.Error, sqlite.Warning
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        with self._lock:
            result = ""
            try:
                "\n".join(self._connection.iterdump())
            except sqlite.Error as e:
                if self._raise_exception:
                    raise
            except sqlite.Warning as e:
                if self._raise_warning:
                    raise
            if destination:
                with open(destination, "w") as file:
                    file.write(result)
            return result

    def get_tables(self):
        """
        Returns the list of tables names.
        Example: ["table_1", "table_2"]
        This method can raise sqlite.Error, sqlite.Warning
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        with self._lock:
            data = []
            cur = None
            try:
                cur = self._connection.cursor()
                cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
                data = cur.fetchall()
            except sqlite.Error as e:
                if self._raise_exception:
                    raise
            except sqlite.Warning as e:
                if self._raise_warning:
                    raise
            finally:
                if cur:
                    cur.close()
            return [item[0] for item in data]

    def get_columns(self, table):
        """
        Returns information about the columns of a given table
        A column is a namedtuple:
            namedtuple(index, name, type, not_null, default, primary_key)
        Example:
            [namedtuple(0, "id", "INTEGER", 1, None, 1),
            namedtuple(1, "name", "TEXT", 0, None, 0),
            namedtuple(2, "age", "INTEGER", 1, None, 0)]

        This method can raise sqlite.Error, sqlite.Warning
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        with self._lock:
            data = []
            cur = None
            try:
                cur = self._connection.cursor()
                cur.execute("pragma table_info('{}')".format(table))
                cache = cur.fetchall()
            except sqlite.Error as e:
                if self._raise_exception:
                    raise
            except sqlite.Warning as e:
                if self._raise_warning:
                    raise
            finally:
                if cur:
                    cur.close()
            for item in cache:
                info = dto.ColumnInfo(*item)
                data.append(info)
            return data

    def close(self):
        """
        Close the connection

        [return]
        Returns a boolean
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        if self._closed:
            return False
        with self._lock:
            if self._connection:
                try:
                    self._connection.close()
                except Exception:
                    pass
                self._connection = None
                atexit.unregister(self.close)
                self._closed = True
            return True

    def delete(self):
        """
        Delete this database

        [return]
        Returns a boolean
        """
        if self._deleted:
            raise error.AlreadyDeletedError
        if self._readonly:
            raise error.ReadonlyError
        if not self._closed:
            self.close()
        if self._temporary:
            return True
        if not os.path.isfile(self._pathname):
            return False
        os.remove(self._pathname)
        self._deleted = True
        return True

    def _setup(self):
        self._update_variables()
        self._make_directory()
        self._create_connection()
        if self._new and self._init_script:
            self.script(self._init_script)

    def _update_variables(self):
        info = util.check_target(self._target, self._directory, False)
        self._name, self._directory, self._pathname, self._tempdir = info

    def _make_directory(self):
        if self._temporary:
            self._new = True
            return
        try:
            os.makedirs(self._directory)
        except FileExistsError:
            pass
        if not os.path.isfile(self._pathname):
            self._new = True

    def _create_connection(self):
        try:
            if "check_same_thread" in self._connection_kwargs:
                del self._connection_kwargs["check_same_thread"]
            db = ":memory:" if self._temporary else self._pathname
            self._connection = sqlite.connect(db, check_same_thread=False,
                                              **self._connection_kwargs)
        except sqlite.Error as e:
            raise e
        finally:
            atexit.register(self.close)

    def _stringify_script(self, script):
        """ This method will:
        - try to read the script: if the script is a file-like object,
            the content (string) will be returned
        - try to open the script: if the script is a path to a file,
            the content (string) will be returned
        - if the script is already a string, it will be returned as it,
        - the script will be returned as it if failed to read/open
        """
        if isinstance(script, str):
            return script
        if isinstance(script, pathlib.Path):
            pathname = script.resolve()
            with open(pathname, "r") as file:
                return file.read()
        # if script is a file-like object
        return script.read()
