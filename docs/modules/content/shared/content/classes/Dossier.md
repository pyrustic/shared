Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier) &nbsp;&nbsp; [JesthDoc](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/JesthDoc.md#class-jesthdoc) &nbsp;&nbsp; [JsonDoc](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/JsonDoc.md#class-jsondoc)
>
> **Functions:** &nbsp; [get\_key\_value](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#get_key_value) &nbsp;&nbsp; [jesth\_autosave](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_autosave) &nbsp;&nbsp; [jesth\_create](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_create) &nbsp;&nbsp; [jesth\_readonly](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_readonly) &nbsp;&nbsp; [jesth\_write](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_write) &nbsp;&nbsp; [json\_autosave](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_autosave) &nbsp;&nbsp; [json\_create](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_create) &nbsp;&nbsp; [json\_readonly](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_readonly) &nbsp;&nbsp; [json\_write](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_write)
>
> **Constants:** &nbsp; DEFAULT_DIRECTORY

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
|cache|getter|Returns the cache||
|caching|getter|Return the state of the caching boolean||
|closed|getter|Returns the Closed boolean||
|deleted|getter|Returns True if this dossier has been deleted through this object||
|directory|getter|Return the directory path (the parent directory of the dossier)||
|name|getter|Returns the name||
|new|getter|Returns True if this dossier is newly created, else return False||
|pathname|getter|Returns the pathname||
|readonly|getter|Return the state of the readonly boolean||
|target|getter|Return the target||
|temporary|getter|Returns True if this Document is created in a temporary directory. The database is created in a temporary directory if you assign None to the constructor's "directory" parameter||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [check](#check) &nbsp;&nbsp; [close](#close) &nbsp;&nbsp; [delete](#delete) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [set](#set) &nbsp;&nbsp; [\_convert\_set\_into\_dict](#_convert_set_into_dict) &nbsp;&nbsp; [\_create\_dossier](#_create_dossier) &nbsp;&nbsp; [\_delete\_dossier](#_delete_dossier) &nbsp;&nbsp; [\_delete\_specific\_entries](#_delete_specific_entries) &nbsp;&nbsp; [\_ensure\_data](#_ensure_data) &nbsp;&nbsp; [\_exit\_handler](#_exit_handler) &nbsp;&nbsp; [\_gen\_file\_id](#_gen_file_id) &nbsp;&nbsp; [\_get\_container](#_get_container) &nbsp;&nbsp; [\_get\_entry\_info\_dto](#_get_entry_info_dto) &nbsp;&nbsp; [\_get\_file\_id](#_get_file_id) &nbsp;&nbsp; [\_get\_filename](#_get_filename) &nbsp;&nbsp; [\_load\_meta](#_load_meta) &nbsp;&nbsp; [\_make\_directory](#_make_directory) &nbsp;&nbsp; [\_register\_exit\_handler](#_register_exit_handler) &nbsp;&nbsp; [\_save](#_save) &nbsp;&nbsp; [\_save\_bin](#_save_bin) &nbsp;&nbsp; [\_save\_cache](#_save_cache) &nbsp;&nbsp; [\_save\_collection](#_save_collection) &nbsp;&nbsp; [\_save\_meta](#_save_meta) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_unregister\_exit\_handler](#_unregister_exit_handler) &nbsp;&nbsp; [\_update\_variables](#_update_variables)

## \_\_init\_\_
Init.




**Signature:** (self, target, \*, autosave=False, readonly=False, caching=True, directory='/home/alex/PyrusticHome/shared', temporary=False)

|Parameter|Description|
|---|---|
|target|target is either the absolute pathname or the basename of the dossier. Its datatype is either a string or a pathlib.Path instance.|
|autosave|bool, auto-save mode|
|readonly|bool, readonly mode|
|caching|bool, tell if whether caching should be done or not|
|directory|str, the directory where dossiers will be created. By default, this directory is '$HOME/PyrusticHome/shared'. If you set None to 'directory', the dossier will be created in a temporary directory.|
|temporary|bool, tells if dossier should be temporary or not|





**Return Value:** None

[Back to Top](#module-overview)


## check
Return basic information about the dossier or a specific entry




**Signature:** (self, name=None)

|Parameter|Description|
|---|---|
|name|the name of the specific entry to check. If name is set to None, basic information about the dossier will be returned |





**Return Value:** If there is a specific entry name, returns a namedtuple (container, filename).
Else returns a dictionary of all entries. Each key represents an entry.
Example: {"entry_1": namedtuple(container="dict", location="/path/to/contents"), ...}.

[Back to Top](#module-overview)


## close
This method closes the access to the document.



**Signature:** (self)





**Return Value:** None

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
|default|a dict, a list, a set or binary data that will replace a non-existent entry |





**Return Value:** This method returns None if the entry isn't in the dossier, else it returns a dict, a list,
or a set.
A path is returned if the entry requested exists and is a binary data.

[Back to Top](#module-overview)


## set
Set an entry.




**Signature:** (self, name, data)

|Parameter|Description|
|---|---|
|name|str, the name of the entry|
|data|a dict, a list, a set, binary data, or an instance of pathlib.Path |





**Return Value:** This method will return the same data if it is a dict, a list, or a set.
A pathname will be returned if the data saved is binary data.

[Back to Top](#module-overview)


## \_convert\_set\_into\_dict
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_dossier
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_delete\_dossier
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_delete\_specific\_entries
No description



**Signature:** (self, names)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_data
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_exit\_handler
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_gen\_file\_id
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_container
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_entry\_info\_dto
No description



**Signature:** (self, name, info)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_file\_id
No description



**Signature:** (self, name)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_filename
No description



**Signature:** (self, file\_id)





**Return Value:** None

[Back to Top](#module-overview)


## \_load\_meta
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_make\_directory
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_register\_exit\_handler
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_save
No description



**Signature:** (self, name, container, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_bin
No description



**Signature:** (self, filename, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_cache
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_collection
No description



**Signature:** (self, filename, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_meta
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_unregister\_exit\_handler
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_variables
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



