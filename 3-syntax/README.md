# Syntax


## Function

### Day 2 Built in functions

commonly used

```py
print(), len(), type(), 
int(), float(), str(), 
list(), dict(), min(), max(), sum(), sorted(), 
input(), open(), file(), dir(), help()
```

### 11_Day_Functions

[11_Day_Functions](https://github.com/androchentw/30-Days-Of-Python/blob/master/11_Day_Functions/11_functions.md)

  
```py
# Passing Arguments with Key and Value
def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter

# Function with Default Parameters
def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface

# Arbitrary Number of Arguments
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# Function as a Parameter of Another Function
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

### Lambda Function

[13_Day_List_comprehension](https://github.com/androchentw/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md)

* Lambda function is a small anonymous function without a name.

```py
<func> = lambda <arg_1>, <arg_2>: <return_value>    # Also accepts default arguments.
<iter> = map(lambda x: x + 1, range(10))            # Or: iter([1, 2, ..., 10])
<iter> = filter(lambda x: x > 5, range(10))         # Or: iter([6, 7, 8, 9])
<obj>  = reduce(lambda out, x: out + x, range(10))  # Or: 45

# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))

square = lambda x : x ** 2
print(square(3))    # 9

def power(x):
    return lambda n : x ** n


# Lambda Function Inside Another Function
cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

## Args

[arguments: python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#arguments)

```py
args   = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}
func(*args, **kwargs)
func(1, 2, x=3, y=4, z=5)

## *args
def add(*a):
    return sum(a)
add(1, 2, 3)    #6

## **kwargs
def f(**kwargs): ...            # f(x=1, y=2, z=3)
def f(x, **kwargs): ...         # f(x=1, y=2, z=3) | f(1, y=2, z=3)
```

## Module

[12_Day_Modules](https://github.com/androchentw/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md)

* A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.
* Default module: OS, System, Statistics, Math, String, Random


```py
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

# Import Functions from a Module and Renaming
# # main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
```

## Import

[Import: python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#imports)

```py
import <module>            # Imports a built-in or '<module>.py'.
import <package>           # Imports a built-in or '<package>/__init__.py'.
import <package>.<module>  # Imports a built-in or '<package>/<module>.py'.
```

### Closure

* A nested function references a value of its enclosing function and then
* the enclosing function returns the nested function.

```py
def get_multiplier(a):
    def out(b):
        return a * b
    return out
>>> multiply_by_3 = get_multiplier(3)
>>> multiply_by_3(10)
30
```

### Non-local

```py
def get_counter():
    i = 0
    def out():
        nonlocal i
        i += 1
        return i
    return out
>>> counter = get_counter()
>>> counter(), counter(), counter()
(1, 2, 3)
```


## Decorator

[14_Day_Higher_order_functions](https://github.com/androchentw/30-Days-Of-Python/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md)

* Built-in Higher Order Functions: map(), filter, and reduce()

```py
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
```


[Parametrized Decorator](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#parametrized-decorator)

```py
from functools import wraps

def debug(print_result=False):
    def decorator(func):
        @wraps(func)
        def out(*args, **kwargs):
            result = func(*args, **kwargs)
            print(func.__name__, result if print_result else '')
            return result
        return out
    return decorator

@debug(print_result=True)
def add(x, y):
    return x + y
```

## Class

[21_Day_Classes_and_objects](https://github.com/androchentw/30-Days-Of-Python/blob/master/21_Day_Classes_and_objects/21_classes_and_objects.md)

```py
```

[class: python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#class)

```py
class <name>:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.a!r})'
    def __str__(self):
        return str(self.a)

    @classmethod
    def get_class_name(cls):
        return cls.__name__
```

* Return value of repr() should be unambiguous and of str() readable.
* If only repr() is defined, it will also be used for str().
* Methods decorated with '@staticmethod' do not receive 'self' nor 'cls' as their first arg.

```py
# Constructor Overloading
class <name>:
    def __init__(self, a=None):
        self.a = a

# Inheritance. Overriding parent method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num

# Multiple Inheritance
class A: pass
class B: pass
class C(A, B): pass
```

### Property

* Pythonic way of implementing getters and setters.

```py
class Person:
    @property
    def name(self):
        return ' '.join(self._name)

    @name.setter
    def name(self, value):
        self._name = value.split()

>>> person = Person()
>>> person.name = '\t Guido  van Rossum \n'
>>> person.name
'Guido van Rossum'
```

### Dataclass

* Decorator that automatically generates init(), repr() and eq() special methods.
    * Objects can be made sortable with 'order=True' and immutable with 'frozen=True'.
    * For object to be hashable, all attributes must be hashable and 'frozen' must be True.
    * Function field() is needed because '<attr_name>: list = []' would make a list that is shared among all instances. Its 'default_factory' argument can be any callable.
    * For attributes of arbitrary type use 'typing.Any'.

```py
from dataclasses import dataclass, field

@dataclass(order=False, frozen=False)
class <class_name>:
    <attr_name_1>: <type>
    <attr_name_2>: <type> = <default_value>
    <attr_name_3>: list/dict/set = field(default_factory=list/dict/set)
```

## Duck Types

* [ch 2-5 Duck Typing](https://wdv4758h.github.io/notes/blog/pythoner-read-ruby-book-2.html)
* [Day30 - Ruby的鴨子型別Duck Type + 完賽感言！](https://ithelp.ithome.com.tw/articles/10207418)


## Exception

* [Exceptions: python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#exceptions)
* [17_Day_Exception_handling](https://github.com/androchentw/30-Days-Of-Python/blob/master/17_Day_Exception_handling/17_exception_handling.md)


```py
try:
    <code_1>
except <exception_a>:
    <code_2_a>
except <exception_b>:
    <code_2_b>
else:
    <code_2_c>
finally:
    <code_3>
```

* Code inside the 'else' block will only be executed if 'try' block had no exceptions.
* Code inside the 'finally' block will always be executed (unless a signal is received).

```py
except <exception>: ...
except <exception> as <name>: ...
except (<exception>, [...]): ...
except (<exception>, [...]) as <name>: ...

# Exepction objects
arguments = <name>.args
exc_type  = <name>.__class__
filename  = <name>.__traceback__.tb_frame.f_code.co_filename
func_name = <name>.__traceback__.tb_frame.f_code.co_name
line      = linecache.getline(filename, <name>.__traceback__.tb_lineno)
traceback = ''.join(traceback.format_tb(<name>.__traceback__))
error_msg = ''.join(traceback.format_exception(exc_type, <name>, <name>.__traceback__))
```

* Also catches subclasses of the exception.
* Use 'traceback.print_exc()' to print the error message to stderr.
* Use 'print(<name>)' to print just the cause of the exception (its arguments).
* Use 'logging.exception(<message>)' to log the exception.


### Built-in Exceptions

* [Built-in Exceptions](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#built-in-exceptions)
* [15_Day_Python_type_errors](https://github.com/androchentw/30-Days-Of-Python/blob/master/15_Day_Python_type_errors/15_python_type_errors.md)


```py
BaseException
 +-- SystemExit                   # Raised by the sys.exit() function.
 +-- KeyboardInterrupt            # Raised when the user hits the interrupt key (ctrl-c).
 +-- Exception                    # User-defined exceptions should be derived from this class.
      +-- ArithmeticError         # Base class for arithmetic errors.
      |    +-- ZeroDivisionError  # Raised when dividing by zero.
      +-- AssertionError          # Raised by `assert <exp>` if expression returns false value.
      +-- AttributeError          # Raised when an attribute is missing.
      +-- EOFError                # Raised by input() when it hits end-of-file condition.
      +-- LookupError             # Raised when a look-up on a collection fails.
      |    +-- IndexError         # Raised when a sequence index is out of range.
      |    +-- KeyError           # Raised when a dictionary key or set element is missing.
      +-- MemoryError             # Out of memory. Could be too late to start deleting vars.
      +-- NameError               # Raised when an object is missing.
      +-- OSError                 # Errors such as “file not found” or “disk full” (see Open).
      |    +-- FileNotFoundError  # When a file or directory is requested but doesn't exist.
      +-- RuntimeError            # Raised by errors that don't fall into other categories.
      |    +-- RecursionError     # Raised when the maximum recursion depth is exceeded.
      +-- StopIteration           # Raised by next() when run on an empty iterator.
      +-- TypeError               # Raised when an argument is of wrong type.
      +-- ValueError              # When an argument is of right type but inappropriate value.
           +-- UnicodeError       # Raised when encoding/decoding strings to/from bytes fails.
```

