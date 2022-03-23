Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Dossier
Definition of the Dossier class

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|autosave|getter|Return the state of the autosave boolean||
|deleted|getter|Returns True if this dossier has been deleted through this object||
|directory|getter|Return the directory path (the parent directory of the dossier)||
|name|getter|Return the name of the dossier||
|new|getter|Returns True if this dossier is newly created, else return False||
|pretty_json|getter|Return the value of pretty_json||
|readonly|getter|Return the state of the readonly boolean||
|temporary|getter|Returns True if this Document is created in a temporary directory. The database is created in a temporary directory if you assign None to the constructor's "directory" parameter||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [check](#check) &nbsp;&nbsp; [delete](#delete) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [set](#set) &nbsp;&nbsp; [\_check\_info](#_check_info) &nbsp;&nbsp; [\_create\_dossier](#_create_dossier) &nbsp;&nbsp; [\_ensure\_autosave](#_ensure_autosave) &nbsp;&nbsp; [\_ensure\_data](#_ensure_data) &nbsp;&nbsp; [\_ensure\_directory](#_ensure_directory) &nbsp;&nbsp; [\_gen\_file\_id](#_gen_file_id) &nbsp;&nbsp; [\_get\_container](#_get_container) &nbsp;&nbsp; [\_get\_file\_id](#_get_file_id) &nbsp;&nbsp; [\_get\_filename](#_get_filename) &nbsp;&nbsp; [\_load\_meta](#_load_meta) &nbsp;&nbsp; [\_save](#_save) &nbsp;&nbsp; [\_save\_collection](#_save_collection) &nbsp;&nbsp; [\_save\_meta](#_save_meta) &nbsp;&nbsp; [\_set\_to\_dict](#_set_to_dict) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_update\_on\_change\_callback](#_update_on_change_callback)

## \_\_init\_\_
Init.




**Signature:** (self, name, \*, readonly=False, autosave=False, pretty\_json=False, directory='/home/alex/PyrusticHome/shared')

|Parameter|Description|
|---|---|
|name|str, the name of the dossier|
|readonly|bool, readonly mode|
|autosave|bool, auto-save mode|
|pretty\_json|bool, tell if whether you want JSON files to be indented or not|
|directory|str, the directory where dossiers will be created. By default, this directory is '$HOME/PyrusticHome/shared'. If you set None to 'directory', the dossier will be created in a temporary directory.|





**Return Value:** None

[Back to Top](#module-overview)


## check
Return basic information about the dossier or a specific entry




**Signature:** (self, name=None)

|Parameter|Description|
|---|---|
|name|the name of the specific entry to check. If name is set to None, basic information about the dossier will be returned |





**Return Value:** If there is a specific entry name, returns a tuple (container, filename).
Else returns a dictionary. Each key represents an entry.
Example: {"entry_1": ("dict", "/path/to/contents"), ...}.

[Back to Top](#module-overview)


## delete
This method deletes the dossier if there isn't any argument.
Else, the arguments are the entries to delete.




**Signature:** (self, \*names)

|Parameter|Description|
|---|---|
|\*names|names of entries to delete. If you don't set a name, the dossier will be deleted |





**Return Value:** Returns a boolean or raise ReadonlyError

[Back to Top](#module-overview)


## get
Get an entry.




**Signature:** (self, name, default=None)

|Parameter|Description|
|---|---|
|name|the name of the entry.|
|default|a dict, a list, a set or binary data to return if the entry doesn't exist. |





**Return Value:** This method returns None if the entry isn't in the dossier.
A path is returned if the entry requested exists and is a binary data.
SharedDict, SharedList, SharedSet are returned respectively if the entry
requested is a dict, a list or a set, respectively, and if autosave is set to True

[Back to Top](#module-overview)


## set
Set an entry.




**Signature:** (self, name, data)

|Parameter|Description|
|---|---|
|name|str, the name of the entry|
|data|a dict, a list, a set, binary data, or an instance of pathlib.Path |





**Return Value:** This method will return a path if the entry is a binary data.
SharedDict, SharedList, SharedSet are returned respectively if the entry
is a dict, a list or a set, respectively, and if autosave is True.
You can call the method "save" on the instances of SharedDict, SharedList,
or SharedSet.

[Back to Top](#module-overview)


## \_check\_info
None



**Signature:** (self, info)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_dossier
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_autosave
None



**Signature:** (self, name, container, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_data
None



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_directory
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_gen\_file\_id
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_container
None



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_file\_id
None



**Signature:** (self, name)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_filename
None



**Signature:** (self, file\_id)





**Return Value:** None

[Back to Top](#module-overview)


## \_load\_meta
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_save
None



**Signature:** (self, name, container, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_collection
None



**Signature:** (self, name, container, data, filename)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_meta
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_set\_to\_dict
None



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_setup
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_on\_change\_callback
None



**Signature:** (self, name, probed\_collection)





**Return Value:** None

[Back to Top](#module-overview)



