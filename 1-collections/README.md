# Collections

* [Day07 - List、tuple、dict、set - iThome](https://ithelp.ithome.com.tw/articles/10219098)
* [30 Days Of Python: Day 2 - Variables, Builtin Functions](https://github.com/androchentw/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/)

## Dictionary

* [Dictionary - python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#dictionary)

```py
fruits = {"apple":10, "banana":7, "orange":8}
print(fruits["banana"])

value  = <dict>.get(key, default=None)          # Returns default if key is missing.
value  = <dict>.setdefault(key, default=None)   # Returns and writes default if key is missing.
<dict> = collections.defaultdict(<type>)        # Returns a dict with default value of type.
<dict> = collections.defaultdict(lambda: 1)     # Returns a dict with default value 1.

<view> = <dict>.keys()                          # Coll. of keys that reflects changes.
<view> = <dict>.values()                        # Coll. of values that reflects changes.
<view> = <dict>.items()                         # Coll. of key-value tuples that reflects chgs.

<dict>.update(<dict>)                           # Adds items. Replaces ones with matching keys.
value = <dict>.pop(key)                         # Removes item or raises KeyError.
{k for k, v in <dict>.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in <dict>.items() if k in keys}  # Returns a dictionary, filtered by keys.
```

## List
## Tuple
## Set

* Tuple 元組
  * Tuple is an immutable and hashable list.
  * 類似於 list 串列，但tuple 給定元素後不能改變
  * 不同地方在於：list使用[]，tuple使用()
* Set 集合 set 的內容元素都必須是獨一無二的

```py
# List
animals = ["bear", "cat", "dog", "elephant"]
print(animals.index('cat'))
print(animals.count('cat'))
print(animals.sort())
print(animals.reverse())


# Tuple
animals = ('bear', 'cat', 'dog', 'elephant', 'cat')

# Set
set1 = set()# 建立空的集合
set1 = set('apple')
print(set1)
{'l', 'p', 'e', 'a'}
```



## Iterator

* [Iterator - python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#iterator)

```py
<iter> = iter(<collection>)                 # `iter(<iter>)` returns unmodified iterator.
<iter> = iter(<function>, to_exclusive)     # A sequence of return values until 'to_exclusive'.
<el>   = next(<iter> [, default])           # Raises StopIteration or returns 'default' on end.
<list> = list(<iter>)                       # Returns a list of iterator's remaining elements.


# Itertools
from itertools import count, repeat, cycle, chain, islice
```
