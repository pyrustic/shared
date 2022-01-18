Back to [All Modules](https://github.com/pyrustic/shared/blob/master/docs/modules/README.md#readme)

# Module Overview

> **shared**
> 
> Main module where are defined the classes Jason and Store
>
> **Classes:** &nbsp; [Error](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Error.md#class-error) &nbsp; [Jason](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Jason.md#class-jason) &nbsp; [JasonDeletedError](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/JasonDeletedError.md#class-jasondeletederror) &nbsp; [ReadonlyError](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/ReadonlyError.md#class-readonlyerror) &nbsp; [SharedDict](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/SharedDict.md#class-shareddict) &nbsp; [SharedList](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/SharedList.md#class-sharedlist) &nbsp; [SharedSet](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/SharedSet.md#class-sharedset) &nbsp; [Store](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/Store.md#class-store) &nbsp; [StoreDeletedError](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/classes/StoreDeletedError.md#class-storedeletederror)
>
> **Functions:** &nbsp; [json\_dump](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_dump) &nbsp; [json\_load](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#json_load) &nbsp; [valid\_jason](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#valid_jason) &nbsp; [valid\_store](https://github.com/pyrustic/shared/blob/master/docs/modules/content/shared/content/functions.md#valid_store)
>
> **Constants:** &nbsp; DEFAULT_LOCATION

# Class Store
Definition of the class Store

## Base Classes
object

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|autosave|getter|Return the state of the autosave boolean||
|deleted|getter|Returns True if this store has been deleted through this object||
|info|getter|Returns a dictionary of entries and their container types
Example: {"entry_1": "dict", "entry_2": "bin", "entry_3": "set"}||
|location|getter|Return the location of the store||
|name|getter|Return the name of the store||
|new|getter|Returns True if this store is newly created, else return False||
|readonly|getter|Return the state of the readonly boolean||



# All Methods
[\_\_init\_\_](#__init__) &nbsp; [\_bind\_save\_method](#_bind_save_method) &nbsp; [\_convert\_collection](#_convert_collection) &nbsp; [\_create\_store](#_create_store) &nbsp; [\_gen\_file\_id](#_gen_file_id) &nbsp; [\_get\_container](#_get_container) &nbsp; [\_get\_filename](#_get_filename) &nbsp; [\_load\_meta](#_load_meta) &nbsp; [\_save](#_save) &nbsp; [\_save\_meta](#_save_meta) &nbsp; [\_set\_to\_dict](#_set_to_dict) &nbsp; [\_setup](#_setup) &nbsp; [delete](#delete) &nbsp; [get](#get) &nbsp; [set](#set)

## \_\_init\_\_
Init.




**Signature:** (self, name, \*, readonly=False, autosave=False, location='/home/alex/PyrusticData/shared')

|Parameter|Description|
|---|---|
| name| str, the name of the store|
| readonly| bool, readonly mode|
| autosave| bool, auto-save mode|
| location| str, the directory where stores will be created.|



**Return Value:** None

[Back to Top](#module-overview)


## \_bind\_save\_method
No description



**Signature:** (self, name, collection)



**Return Value:** None

[Back to Top](#module-overview)


## \_convert\_collection
No description



**Signature:** (self, container, data)



**Return Value:** None

[Back to Top](#module-overview)


## \_create\_store
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


## \_save
No description



**Signature:** (self, name, container, data)



**Return Value:** None

[Back to Top](#module-overview)


## \_save\_meta
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_set\_to\_dict
No description



**Signature:** (self, data)



**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## delete
This method deletes the store if there isn't any argument.
Else, the arguments are the entries to delete.




**Signature:** (self, \*names)



**Return Value:** Returns a boolean or raise ReadonlyError

[Back to Top](#module-overview)


## get
Get an entry.




**Signature:** (self, name, default=None)

|Parameter|Description|
|---|---|
| name| the name of the entry.|
| default| a dict, a list, a set or binary data to return if the entry doesn't exist.|



**Return Value:** This method returns None if the entry isn't in the store.
A path is returned if the entry requested exists and is a binary data.
SharedDict, SharedList, SharedSet are returned respectively if the entry
requested is a dict, a list or a set

[Back to Top](#module-overview)


## set
Set an entry.




**Signature:** (self, name, data)

|Parameter|Description|
|---|---|
| name| str, the name of the entry|
| data| a dict, a list, a set or binary data.|



**Return Value:** This method will return a path if the entry is a binary data.
SharedDict, SharedList, SharedSet are returned respectively if the entry
is a dict, a list or a set.
You can call the method "save" on the instances of SharedDict, SharedList,
or SharedSet.

[Back to Top](#module-overview)



