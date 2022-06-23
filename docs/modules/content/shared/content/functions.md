Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

**shared**
 
The Shared Data Interface

> **Classes:** &nbsp; [Database](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Database.md#class-database) &nbsp;&nbsp; [Document](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Document.md#class-document) &nbsp;&nbsp; [Dossier](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Dossier.md#class-dossier)
>
> **Functions:** &nbsp; [autosave](#autosave) &nbsp;&nbsp; [create](#create) &nbsp;&nbsp; [get\_key\_value](#get_key_value) &nbsp;&nbsp; [readonly](#readonly) &nbsp;&nbsp; [write](#write)
>
> **Constants:** &nbsp; DEFAULT_DIRECTORY

# All Functions
[autosave](#autosave) &nbsp;&nbsp; [create](#create) &nbsp;&nbsp; [get\_key\_value](#get_key_value) &nbsp;&nbsp; [readonly](#readonly) &nbsp;&nbsp; [write](#write)

## autosave
Convenience function to open a document in autosave mode. It returns data



**Signature:** (target, \*, default=None, file\_format=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


## create
Convenience function to create a document



**Signature:** (target, \*, default=None, file\_format=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


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


## readonly
Convenience function to open a document in readonly mode. It returns the data



**Signature:** (target, \*, default=None, file\_format=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


## write
Convenience function to open a document then write data inside



**Signature:** (target, data, \*, file\_format=None, directory='/home/alex/PyrusticHome/shared')





**Return Value:** None

[Back to Top](#module-overview)


