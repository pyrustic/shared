Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier)
>
> **Functions:** &nbsp; [autosave](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#autosave) &nbsp;&nbsp; [create](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#create) &nbsp;&nbsp; [get\_key\_value](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#get_key_value) &nbsp;&nbsp; [readonly](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#readonly) &nbsp;&nbsp; [write](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#write)
>
> **Constants:** &nbsp; DEFAULT_DIRECTORY

# Class Document
No description.

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|autosave|getter|Return the autosave boolean state||
|cache|getter|Returns the cached contents of the document. Returns None if caching is set to False.||
|caching|getter|Returns the caching boolean||
|closed|getter|Returns the Closed boolean||
|default|getter|Returns the default value||
|deleted|getter|Return True if this document file is deleted else return False||
|directory|getter|Return the value of the location variable||
|file_format|getter|Returns the file format||
|name|getter|Returns the name||
|new|getter|Returns True if this dossier is newly created, else return False||
|pathname|getter|Returns the pathname||
|readonly|getter|Return the readonly boolean state||
|target|getter|Return the target||
|temporary|getter|Returns True if this Document is created in a temporary directory. The database is created in a temporary directory if you  assign None to the constructor's "directory" parameter||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [close](#close) &nbsp;&nbsp; [delete](#delete) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [write](#write) &nbsp;&nbsp; [\_check\_file\_format](#_check_file_format) &nbsp;&nbsp; [\_exit\_handler](#_exit_handler) &nbsp;&nbsp; [\_init\_file](#_init_file) &nbsp;&nbsp; [\_make\_directory](#_make_directory) &nbsp;&nbsp; [\_read](#_read) &nbsp;&nbsp; [\_register\_exit\_handler](#_register_exit_handler) &nbsp;&nbsp; [\_save\_cache](#_save_cache) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_unregister\_exit\_handler](#_unregister_exit_handler) &nbsp;&nbsp; [\_update\_variables](#_update_variables) &nbsp;&nbsp; [\_write](#_write)

## \_\_init\_\_
Init.




**Signature:** (self, target, \*, default=None, autosave=False, readonly=False, caching=True, file\_format=None, directory='/home/alex/PyrusticHome/shared', temporary=False)

|Parameter|Description|
|---|---|
|target|target is either the absolute pathname or the basename of a file. Its datatype is either a string or a pathlib.Path instance.|
|default|default value for this document file. If the document is newly created, the default value will populate it. If you don't set a default value, a dict will be the default value.|
|autosave|boolean to say if you want to activate the autosave feature or not|
|readonly|boolean to say if you want to open this document in readonly mode or not|
|caching|boolean to set if whether data should be cached or not|
|directory|the directory where you want to store the document. By default, the directory is "$HOME/PyrusticHome/shared". If you set None to directory, the document will be created in a temporary directory|
|temporary|boolean to tell if either you want this document to be temporary or not|
|error\_module|module containing these Exceptions classes: AlreadyClosedError, , AlreadyDeletedError, and ReadonlyError|





**Return Value:** None

[Back to Top](#module-overview)


## close
This method closes the access to the document.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## delete
This method deletes the document.
Returns a boolean or raise ReadonlyError



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## read
Load data from the document



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## write
Set the contents of the JSON file. Returns the same data



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_check\_file\_format
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_exit\_handler
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_init\_file
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_make\_directory
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_read
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_register\_exit\_handler
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_cache
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


## \_write
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)



