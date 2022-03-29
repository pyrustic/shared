Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Document
Definition of the Document class

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
|default|getter|Returns the default value||
|deleted|getter|Return True if this document file is deleted else return False||
|directory|getter|Return the value of the location variable||
|file_format|getter|Returns the file format (either 'hackernote' or 'json')||
|name|getter|Return the name of the document file||
|new|getter|Returns True if the underlying document file is newly created, else return False||
|pretty_json|getter|Return the value of pretty_json||
|readonly|getter|Return the readonly boolean state||
|temporary|getter|Returns True if this Document is created in a temporary directory. The database is created in a temporary directory if you  assign None to the constructor's "directory" parameter||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [delete](#delete) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [save](#save) &nbsp;&nbsp; [write](#write) &nbsp;&nbsp; [\_check\_format](#_check_format) &nbsp;&nbsp; [\_dump](#_dump) &nbsp;&nbsp; [\_ensure\_autosave](#_ensure_autosave) &nbsp;&nbsp; [\_ensure\_name\_and\_directory](#_ensure_name_and_directory) &nbsp;&nbsp; [\_load](#_load) &nbsp;&nbsp; [\_setup](#_setup)

## \_\_init\_\_
Init.




**Signature:** (self, name, \*, readonly=False, autosave=False, default=None, file\_format='auto', caching=True, pretty\_json=True, directory='/home/alex/PyrusticHome/shared')

|Parameter|Description|
|---|---|
|name|string, the name of the document file. Example: "data.json"|
|readonly|boolean to say if you want to open this document in readonly mode or not|
|autosave|boolean to say if you want to activate the autosave feature or not|
|default|default value for this document file. If the document is newly created, the default value will populate it.|
|file\_format|"auto" or "json" or "hackernote". If the value is "auto", the document will be considered as a JSON file if its extension is ".json", otherwise it will be considered as a hackernote.|
|caching|boolean to set if whether data should be cached or not|
|pretty\_json|boolean to tell if either json should be indented or not|
|directory|the directory where you want to store the document. By default, the directory is "$HOME/PyrusticHome/shared". If you set None to directory, the document will be created in a temporary directory|





**Return Value:** None

[Back to Top](#module-overview)


## delete
This method delete the document.
Returns a boolean or raise ReadonlyError



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## read
Load data from the document



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## save
Save the cached data.
Returns a boolean or raise ReadonlyError



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## write
Set the contents of the JSON file or hackernote file.
Return the same data or the probed version of the data if autosave is True.



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_check\_format
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_dump
None



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_autosave
None



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_name\_and\_directory
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_load
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_setup
None



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



