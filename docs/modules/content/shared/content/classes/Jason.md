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

# Class Jason
Definition of the class Jason

## Base Classes
object

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|autosave|getter|Return the autosave boolean state||
|data|getter|Return the contents of the JSON file||
|data|setter|Set the contents of the JSON file||
|deleted|getter|Return True if this JSON file is deleted else return False||
|location|getter|Return the value of the location variable||
|name|getter|Return the name of the JSON file||
|new|getter|Returns True if this JSON file is newly created, else return False||
|readonly|getter|Return the readonly boolean state||



# All Methods
[\_\_init\_\_](#__init__) &nbsp; [\_bind\_save\_method](#_bind_save_method) &nbsp; [\_convert\_collection](#_convert_collection) &nbsp; [\_setup](#_setup) &nbsp; [delete](#delete) &nbsp; [save](#save)

## \_\_init\_\_
Init.




**Signature:** (self, name, \*, readonly=False, autosave=False, default=None, location='/home/alex/PyrusticData/shared')

|Parameter|Description|
|---|---|
| name| string, the name of the JSON file. Example: "data.json"|
| readonly| boolean to say if you want to open this JSON file in readonly mode or not|
| autosave| boolean to say if you want to activate the autosave feature or not|
| default| default value for this JSON file. It can be None, a dict or a list.|
| location| the directory where you want to store the JSON file.|



**Return Value:** None

[Back to Top](#module-overview)


## \_bind\_save\_method
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_convert\_collection
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
This method delete the Jason file.
Returns a boolean or raise ReadonlyError



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## save
Write the contents of the property 'data' in the JSON file



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)



