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

# Class SharedSet
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.

## Base Classes
probed.ProbedSet

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|changed|getter|Boolean attribute to indicate whether the content of the
collection changed or not |probed.ProbedSet|
|changed|setter|None|probed.ProbedSet|
|on_change|getter|None|probed.ProbedSet|
|on_change|setter|None|probed.ProbedSet|
|probe|getter|None|probed.ProbedSet|
|probe|setter|None|probed.ProbedSet|



# All Methods
[\_probedset\_\_get\_info](#_ProbedSet__get_info) &nbsp; [\_probedset\_\_run\_on\_change](#_ProbedSet__run_on_change) &nbsp; [\_probedset\_\_run\_probe](#_ProbedSet__run_probe) &nbsp; [\_\_init\_\_](#__init__) &nbsp; [add](#add) &nbsp; [clear](#clear) &nbsp; [difference\_update](#difference_update) &nbsp; [discard](#discard) &nbsp; [intersection\_update](#intersection_update) &nbsp; [pop](#pop) &nbsp; [remove](#remove) &nbsp; [save](#save) &nbsp; [symmetric\_difference\_update](#symmetric_difference_update) &nbsp; [update](#update)

## \_ProbedSet\_\_get\_info
No description

**Inherited from:** probed.ProbedSet

**Signature:** (self, operation, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedSet\_\_run\_on\_change
No description

**Inherited from:** probed.ProbedSet

**Signature:** (self, info)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedSet\_\_run\_probe
No description

**Inherited from:** probed.ProbedSet

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

**Inherited from:** probed.ProbedSet

**Signature:** (self, items=None, probe=None, on\_change=None)



**Return Value:** None

[Back to Top](#module-overview)


## add
Add an element to a set.

This has no effect if the element is already present.

**Inherited from:** probed.ProbedSet

**Signature:** (self, item)



**Return Value:** None

[Back to Top](#module-overview)


## clear
Remove all elements from this set.

**Inherited from:** probed.ProbedSet

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## difference\_update
Remove all elements of another set from this set.

**Inherited from:** probed.ProbedSet

**Signature:** (self, \*others)



**Return Value:** None

[Back to Top](#module-overview)


## discard
Remove an element from a set if it is a member.

If the element is not a member, do nothing.

**Inherited from:** probed.ProbedSet

**Signature:** (self, item)



**Return Value:** None

[Back to Top](#module-overview)


## intersection\_update
Update a set with the intersection of itself and another.

**Inherited from:** probed.ProbedSet

**Signature:** (self, \*others)



**Return Value:** None

[Back to Top](#module-overview)


## pop
Remove and return an arbitrary set element.
Raises KeyError if the set is empty.

**Inherited from:** probed.ProbedSet

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## remove
Remove an element from a set; it must be a member.

If the element is not a member, raise a KeyError.

**Inherited from:** probed.ProbedSet

**Signature:** (self, item)



**Return Value:** None

[Back to Top](#module-overview)


## save
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## symmetric\_difference\_update
Update a set with the symmetric difference of itself and another.

**Inherited from:** probed.ProbedSet

**Signature:** (self, other)



**Return Value:** None

[Back to Top](#module-overview)


## update
Update a set with the union of itself and others.

**Inherited from:** probed.ProbedSet

**Signature:** (self, \*others)



**Return Value:** None

[Back to Top](#module-overview)



