Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier) &nbsp;&nbsp; [JesthDoc](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/JesthDoc.md#class-jesthdoc) &nbsp;&nbsp; [JsonDoc](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/JsonDoc.md#class-jsondoc)
>
> **Functions:** &nbsp; [get\_key\_value](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#get_key_value) &nbsp;&nbsp; [jesth\_autosave](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_autosave) &nbsp;&nbsp; [jesth\_create](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_create) &nbsp;&nbsp; [jesth\_readonly](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_readonly) &nbsp;&nbsp; [jesth\_write](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#jesth_write) &nbsp;&nbsp; [json\_autosave](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_autosave) &nbsp;&nbsp; [json\_create](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_create) &nbsp;&nbsp; [json\_readonly](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_readonly) &nbsp;&nbsp; [json\_write](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_write)
>
> **Constants:** &nbsp; DEFAULT_DIRECTORY

# Class JsonDoc
No description.

## Base Classes
shared.document.Document

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|autosave|getter|Return the autosave boolean state|shared.document.Document|
|cache|getter|Returns the cached contents of the document. Returns None if caching is set to False.|shared.document.Document|
|caching|getter|Returns the caching boolean|shared.document.Document|
|closed|getter|Returns the Closed boolean|shared.document.Document|
|default|getter|Returns the default value|shared.document.Document|
|deleted|getter|Return True if this document file is deleted else return False|shared.document.Document|
|directory|getter|Return the value of the location variable|shared.document.Document|
|name|getter|Returns the name|shared.document.Document|
|new|getter|Returns True if this dossier is newly created, else return False|shared.document.Document|
|pathname|getter|Returns the pathname|shared.document.Document|
|readonly|getter|Return the readonly boolean state|shared.document.Document|
|target|getter|Return the target|shared.document.Document|
|temporary|getter|Returns True if this Document is created in a temporary directory. The database is created in a temporary directory if you  assign None to the constructor's "directory" parameter|shared.document.Document|



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [close](#close) &nbsp;&nbsp; [delete](#delete) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [write](#write) &nbsp;&nbsp; [\_exit\_handler](#_exit_handler) &nbsp;&nbsp; [\_init\_file](#_init_file) &nbsp;&nbsp; [\_make\_directory](#_make_directory) &nbsp;&nbsp; [\_read](#_read) &nbsp;&nbsp; [\_register\_exit\_handler](#_register_exit_handler) &nbsp;&nbsp; [\_save\_cache](#_save_cache) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_unregister\_exit\_handler](#_unregister_exit_handler) &nbsp;&nbsp; [\_update\_variables](#_update_variables) &nbsp;&nbsp; [\_write](#_write)

## \_\_init\_\_
Init.




**Signature:** (self, target, \*, default=None, autosave=False, readonly=False, caching=True, directory='/home/alex/PyrusticHome/shared', temporary=False)

|Parameter|Description|
|---|---|
|target|target is either the absolute pathname or the basename of a file. Its datatype is either a string or a pathlib.Path instance.|
|default|default value for this document file. If the document is newly created, the default value will populate it. If you don't set a default value, a dict will be the default value.|
|autosave|boolean to say if you want to activate the autosave feature or not|
|readonly|boolean to say if you want to open this document in readonly mode or not|
|caching|boolean to set if whether data should be cached or not|
|directory|the directory where you want to store the document. By default, the directory is "$HOME/PyrusticHome/shared". If you set None to directory, the document will be created in a temporary directory|
|temporary|boolean to tell if either you want this document to be temporary or not|





**Return Value:** None

[Back to Top](#module-overview)


## close
This method closes the access to the document.

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## delete
This method deletes the document.
Returns a boolean or raise ReadonlyError

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## read
Load data from the document

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## write
Set the contents of the JSON file. Returns the same data

**Inherited from:** shared.document.Document

**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_exit\_handler
No description

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_init\_file
No description

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_make\_directory
No description

**Inherited from:** shared.document.Document

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

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_save\_cache
No description

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_unregister\_exit\_handler
No description

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_variables
No description

**Inherited from:** shared.document.Document

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_write
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)



