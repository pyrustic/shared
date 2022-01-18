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

# Class SharedDict
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)

## Base Classes
probed.ProbedDict

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|changed|getter|Boolean attribute to indicate whether the content of the
collection changed or not |probed.ProbedDict|
|changed|setter|None|probed.ProbedDict|
|on_change|getter|None|probed.ProbedDict|
|on_change|setter|None|probed.ProbedDict|
|probe|getter|None|probed.ProbedDict|
|probe|setter|None|probed.ProbedDict|



# All Methods
[\_probeddict\_\_get\_info](#_ProbedDict__get_info) &nbsp; [\_probeddict\_\_merge\_update\_other\_kwargs](#_ProbedDict__merge_update_other_kwargs) &nbsp; [\_probeddict\_\_run\_on\_change](#_ProbedDict__run_on_change) &nbsp; [\_probeddict\_\_run\_probe](#_ProbedDict__run_probe) &nbsp; [\_\_init\_\_](#__init__) &nbsp; [clear](#clear) &nbsp; [fromkeys](#fromkeys) &nbsp; [get](#get) &nbsp; [pop](#pop) &nbsp; [popitem](#popitem) &nbsp; [save](#save) &nbsp; [setdefault](#setdefault) &nbsp; [update](#update)

## \_ProbedDict\_\_get\_info
No description

**Inherited from:** probed.ProbedDict

**Signature:** (self, operation, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedDict\_\_merge\_update\_other\_kwargs
No description

**Inherited from:** probed.ProbedDict

**Signature:** (self, other, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedDict\_\_run\_on\_change
No description

**Inherited from:** probed.ProbedDict

**Signature:** (self, info)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedDict\_\_run\_probe
No description

**Inherited from:** probed.ProbedDict

**Signature:** (self, info)



**Return Value:** None

[Back to Top](#module-overview)


## \_\_init\_\_
- items: default value of the collection

- probe: callback called whenever the content of the collection
is going to change.
It should accept as argument an instance of probed.Info.
It should return the same instance (edited or not) of probed.Info
it got as argument, or return None to cancel the change operation.

- on_change: callback called whenever the content of the collection changes.
It should accept as argument an instance of probed.Info.

**Inherited from:** probed.ProbedDict

**Signature:** (self, items=None, probe=None, on\_change=None)



**Return Value:** None

[Back to Top](#module-overview)


## clear
D.clear() -> None.  Remove all items from D.

**Inherited from:** probed.ProbedDict

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## fromkeys
Create a new dictionary with keys from iterable and values set to value.

**Inherited from:** dict

**Signature:** (type, iterable, value=None, /)



**Return Value:** None

[Back to Top](#module-overview)


## get
Return the value for key if key is in the dictionary, else default.

**Inherited from:** dict

**Signature:** (self, key, default=None, /)



**Return Value:** None

[Back to Top](#module-overview)


## pop
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised

**Inherited from:** probed.ProbedDict

**Signature:** (self, key, default=None)



**Return Value:** None

[Back to Top](#module-overview)


## popitem
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.

**Inherited from:** probed.ProbedDict

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## save
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## setdefault
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

**Inherited from:** probed.ProbedDict

**Signature:** (self, key, default=None)



**Return Value:** None

[Back to Top](#module-overview)


## update
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]

**Inherited from:** probed.ProbedDict

**Signature:** (self, other=None, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)



