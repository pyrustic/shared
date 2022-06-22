Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier)
>
> **Functions:** &nbsp; [autosave](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#autosave) &nbsp;&nbsp; [create](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#create) &nbsp;&nbsp; [get\_key\_value](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#get_key_value) &nbsp;&nbsp; [readonly](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#readonly) &nbsp;&nbsp; [write](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#write)
>
> **Constants:** &nbsp; DEFAULT_DIRECTORY

# Class Database
Definition of the Database class

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|closed|getter|Boolean to tell if whether this database is closed or not||
|connection|getter|Connection object||
|deleted|getter|Boolean to tell if whether this database is deleted or not||
|directory|getter|Returns the directory||
|init_script|getter|Returns the initialization script||
|name|getter|Returns the name of this database||
|new|getter|Returns True if the database has just been created, otherwise returns False||
|readonly|getter|Returns the readonly boolean||
|temporary|getter|Returns True if the database is created in memory. The database is created in memory if you assign None to the constructor's "directory" parameter||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [check](#check) &nbsp;&nbsp; [close](#close) &nbsp;&nbsp; [delete](#delete) &nbsp;&nbsp; [edit](#edit) &nbsp;&nbsp; [export](#export) &nbsp;&nbsp; [get\_columns](#get_columns) &nbsp;&nbsp; [get\_tables](#get_tables) &nbsp;&nbsp; [query](#query) &nbsp;&nbsp; [script](#script) &nbsp;&nbsp; [\_create\_connection](#_create_connection) &nbsp;&nbsp; [\_ensure\_filename\_and\_directory](#_ensure_filename_and_directory) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_stringify\_script](#_stringify_script)

## \_\_init\_\_
Init




**Signature:** (self, name, \*, readonly=False, init\_script=None, directory='/home/alex/PyrusticHome/shared', raise\_exception=True, raise\_warning=True, connection\_kwargs=None)

|Parameter|Description|
|---|---|
|name|the name of the database |
|readonly|boolean to set the database in the read-only state |
|init\_script|a path to a file (an instance of pathlib.Path), a file-like object or a string of sql code Example_a: "CREATE TABLE my_table(id INTEGER NOT NULL PRIMARY KEY);". Example_b: pathlib.Path("/path/to/script.sql"). |
|directory|path to directory where the database will be created. Set directory to None if you want the database to be created in memory. |
|raise\_exception|By default, True, so exceptions (sqlite.Error) will be raised |
|raise\_warning|By default, True, so exceptions (sqlite.Warning) will be raised |
|connection\_kwargs|connections arguments used while calling the method "sqlite.connect()"|





**Return Value:** None

[Back to Top](#module-overview)


## check
Test the database




**Signature:** (self)





**Return Value:** Returns True if this is a legal database, otherwise returns False

[Back to Top](#module-overview)


## close
Close the connection




**Signature:** (self)





**Return Value:** Returns a boolean

[Back to Top](#module-overview)


## delete
Delete this database




**Signature:** (self)





**Return Value:** Returns a boolean

[Back to Top](#module-overview)


## edit
Use this method to edit your database.
Formally: Data Definition Language (DDL) and Data Manipulation Language (DML).




**Signature:** (self, sql, param=None)

|Parameter|Description|
|---|---|
|sql|str, the sql code|
|param|a list of parameters to fill the "?" in the sql code |





**Return Value:** It returns True or False or raises sqlite.Error, sqlite.Warning

[Back to Top](#module-overview)


## export
export the database: it returns a string of sql code.
This method can raise sqlite.Error, sqlite.Warning



**Signature:** (self, destination=None)





**Return Value:** None

[Back to Top](#module-overview)


## get\_columns
Returns information about the columns of a given table
A column is a namedtuple:
    namedtuple(index, name, type, not_null, default, primary_key)
Example:
    [namedtuple(0, "id", "INTEGER", 1, None, 1),
    namedtuple(1, "name", "TEXT", 0, None, 0),
    namedtuple(2, "age", "INTEGER", 1, None, 0)]

This method can raise sqlite.Error, sqlite.Warning



**Signature:** (self, table)





**Return Value:** None

[Back to Top](#module-overview)


## get\_tables
Returns the list of tables names.
Example: ["table_1", "table_2"]
This method can raise sqlite.Error, sqlite.Warning



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## query
Use this method to query your database.
Formally: Data Query Language (DQL)
It returns a namedtuple: (columns, data).
Columns is a list of strings, columns names.
Data is a list with data from ur query.
    Example:
        namedtuple(columns=["id", "name", "age"],
                data= ( [1, "Jack", 50], ...) )
This method can raise sqlite.Error, sqlite.Warning



**Signature:** (self, sql, param=None)





**Return Value:** None

[Back to Top](#module-overview)


## script
Executes the script as a sql-script. Meaning: there are multiple lines of sql.
This method returns nothing but could raise sqlite.Error, sqlite.Warning.

script could be a path (pathlib.Path) to a file, a file-like object or just a string.



**Signature:** (self, script)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_connection
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_filename\_and\_directory
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_stringify\_script
This method will:
- try to read the script: if the script is a file-like object,
    the content (string) will be returned
- try to open the script: if the script is a path to a file,
    the content (string) will be returned
- if the script is already a string, it will be returned as it,
- the script will be returned as it if failed to read/open



**Signature:** (self, script)





**Return Value:** None

[Back to Top](#module-overview)



