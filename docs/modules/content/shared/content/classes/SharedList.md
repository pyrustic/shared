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

# Class SharedList
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.

## Base Classes
probed.ProbedList

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|changed|getter|Boolean attribute to indicate whether the content of the
collection changed or not |probed.ProbedList|
|changed|setter|None|probed.ProbedList|
|on_change|getter|None|probed.ProbedList|
|on_change|setter|None|probed.ProbedList|
|probe|getter|None|probed.ProbedList|
|probe|setter|None|probed.ProbedList|



# All Methods
[\_probedlist\_\_get\_info](#_ProbedList__get_info) &nbsp; [\_probedlist\_\_run\_on\_change](#_ProbedList__run_on_change) &nbsp; [\_probedlist\_\_run\_probe](#_ProbedList__run_probe) &nbsp; [\_\_init\_\_](#__init__) &nbsp; [append](#append) &nbsp; [clear](#clear) &nbsp; [copy](#copy) &nbsp; [count](#count) &nbsp; [extend](#extend) &nbsp; [index](#index) &nbsp; [insert](#insert) &nbsp; [pop](#pop) &nbsp; [remove](#remove) &nbsp; [reverse](#reverse) &nbsp; [save](#save) &nbsp; [sort](#sort)

## \_ProbedList\_\_get\_info
No description

**Inherited from:** probed.ProbedList

**Signature:** (self, operation, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedList\_\_run\_on\_change
No description

**Inherited from:** probed.ProbedList

**Signature:** (self, info)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedList\_\_run\_probe
No description

**Inherited from:** probed.ProbedList

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

**Inherited from:** probed.ProbedList

**Signature:** (self, items=None, probe=None, on\_change=None)



**Return Value:** None

[Back to Top](#module-overview)


## append
Append object to the end of the list.

**Inherited from:** probed.ProbedList

**Signature:** (self, value)



**Return Value:** None

[Back to Top](#module-overview)


## clear
Remove all items from list.

**Inherited from:** probed.ProbedList

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## copy
Return a shallow copy of the list.

**Inherited from:** list

**Signature:** (self, /)



**Return Value:** None

[Back to Top](#module-overview)


## count
Return number of occurrences of value.

**Inherited from:** list

**Signature:** (self, value, /)



**Return Value:** None

[Back to Top](#module-overview)


## extend
Extend list by appending elements from the iterable.

**Inherited from:** probed.ProbedList

**Signature:** (self, value)



**Return Value:** None

[Back to Top](#module-overview)


## index
Return first index of value.

Raises ValueError if the value is not present.

**Inherited from:** list

**Signature:** (self, value, start=0, stop=9223372036854775807, /)



**Return Value:** None

[Back to Top](#module-overview)


## insert
Insert object before index.

**Inherited from:** probed.ProbedList

**Signature:** (self, index, value)



**Return Value:** None

[Back to Top](#module-overview)


## pop
Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.

**Inherited from:** probed.ProbedList

**Signature:** (self, index=-1)



**Return Value:** None

[Back to Top](#module-overview)


## remove
Remove first occurrence of value.

Raises ValueError if the value is not present.

**Inherited from:** probed.ProbedList

**Signature:** (self, value)



**Return Value:** None

[Back to Top](#module-overview)


## reverse
Reverse *IN PLACE*.

**Inherited from:** probed.ProbedList

**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## save
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## sort
Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them,
ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.

**Inherited from:** probed.ProbedList

**Signature:** (self, \*, key=None, reverse=False)



**Return Value:** None

[Back to Top](#module-overview)



