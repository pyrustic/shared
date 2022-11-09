Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier) &nbsp;&nbsp; [JesthDoc](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/JesthDoc.md#class-jesthdoc) &nbsp;&nbsp; [JsonDoc](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/JsonDoc.md#class-jsondoc)
>
> **Functions:** &nbsp; [get\_key\_value](#get_key_value) &nbsp;&nbsp; [jesth\_autosave](#jesth_autosave) &nbsp;&nbsp; [jesth\_create](#jesth_create) &nbsp;&nbsp; [jesth\_readonly](#jesth_readonly) &nbsp;&nbsp; [jesth\_write](#jesth_write) &nbsp;&nbsp; [json\_autosave](#json_autosave) &nbsp;&nbsp; [json\_create](#json_create) &nbsp;&nbsp; [json\_readonly](#json_readonly) &nbsp;&nbsp; [json\_write](#json_write)
>
> **Constants:** &nbsp; DEFAULT_DIRECTORY

# All Functions
[get\_key\_value](#get_key_value) &nbsp;&nbsp; [jesth\_autosave](#jesth_autosave) &nbsp;&nbsp; [jesth\_create](#jesth_create) &nbsp;&nbsp; [jesth\_readonly](#jesth_readonly) &nbsp;&nbsp; [jesth\_write](#jesth_write) &nbsp;&nbsp; [json\_autosave](#json_autosave) &nbsp;&nbsp; [json\_create](#json_create) &nbsp;&nbsp; [json\_readonly](#json_readonly) &nbsp;&nbsp; [json\_write](#json_write)

## get\_key\_value
Split a string into key and value parts.
The string must have a separator defined as an argument.
By default, the separator is ":".
An example of a valid string is "name: John Doe ".
The result will be: ("name": "John Doe")




**Signature:** (line, sep='=', strip\_whitespace=True)

|Parameter|Description|
|---|---|
|line|the string to split|
|sep|the separator, by default it is ":"|
|strip\_whitespace|boolean to tell whether you want whitespace to be stripped out or not. By default, the value is True. |





**Return Value:** Always returns a tuple. If the key doesn't exist, it will be an empty string

[Back to Top](#module-overview)


## jesth\_autosave
Convenience function to open a document in autosave mode. It returns data



**Signature:** (target, \*, default=None, directory='/home/alex/PyrusticHome/shared', compact=False, split\_body=True)





**Return Value:** None

[Back to Top](#module-overview)


## jesth\_create
Convenience function to create a document



**Signature:** (target, \*, default=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


## jesth\_readonly
Convenience function to open a document in readonly mode. It returns the data



**Signature:** (target, \*, default=None, directory='/home/alex/PyrusticHome/shared', compact=False, split\_body=True)





**Return Value:** None

[Back to Top](#module-overview)


## jesth\_write
Convenience function to open a document then write data inside



**Signature:** (target, data, \*, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


## json\_autosave
Convenience function to open a document in autosave mode. It returns data



**Signature:** (target, \*, default=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


## json\_create
Convenience function to create a document



**Signature:** (target, \*, default=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


## json\_readonly
Convenience function to open a document in readonly mode. It returns the data



**Signature:** (target, \*, default=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


## json\_write
Convenience function to open a document then write data inside



**Signature:** (target, data, \*, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


