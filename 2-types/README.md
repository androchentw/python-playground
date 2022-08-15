# Types

## Type

```py
# Checking data types
print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
```


[python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#type)

* Everything is an object.
* Every object has a type.
* Type and class are synonymous.

```py
<type> = type(<el>)                          # Or: <el>.__class__
<bool> = isinstance(<el>, <type>)            # Or: issubclass(type(<el>), <type>)
>>> type('a'), 'a'.__class__, str
(<class 'str'>, <class 'str'>, <class 'str'>)
```

## String

[04_Day_Strings](https://github.com/androchentw/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md)

### New Style String Formatting (str.format)

```py
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
```

### String Interpolation / f-Strings (Python 3.6+)

```py
print(f'{a} + {b} = {a +b}')
```

### Slicing

```py
language = 'Python'
first_three = language[0:3] # Pyt
last_three = language[3:6]  # hon
last_three = language[-3:]  # hon
```

### String Methods


```py
challenge = 'thirty days of python'
print(challenge.upper()) # 'THIRTTY DAYS OF PYTHON'
print(challenge.count('th')) # 2`
print(challenge.endswith('on'))   # True
print(challenge.find('th')) # 17

sub_string = 'da'
print(challenge.index(sub_string))  # 7

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)  # 'HTML# CSS# JavaScript# React'

print(challenge.replace('python', 'coding'))  # 'thirty days of coding'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
```


## Regular_Exp

[18_Day_Regular_expressions](https://github.com/androchentw/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md)

![regex cheatsheet](https://github.com/androchentw/30-Days-Of-Python/blob/master/images/regex.png?raw=true)


```py
import re
<str>   = re.sub(<regex>, new, text, count=0)  # Substitutes all occurrences with 'new'.
<list>  = re.findall(<regex>, text)            # Returns all occurrences as strings.
<list>  = re.split(<regex>, text, maxsplit=0)  # Use brackets in regex to include the matches.
<Match> = re.search(<regex>, text)             # Searches for first occurrence of the pattern.
<Match> = re.match(<regex>, text)              # Searches only at the beginning of the text.
<iter>  = re.finditer(<regex>, text)           # Returns all occurrences as Match objects.
```

* Argument 'new' can be a function that accepts a Match object and returns a string.
* Search() and match() return None if they can't find a match.
* Argument 'flags=re.IGNORECASE' can be used with all functions.
* Argument 'flags=re.MULTILINE' makes '^' and '$' match the start/end of each line.
* Argument 'flags=re.DOTALL' makes dot also accept the '\n'.
* Use r'\1' or '\\1' for backreference ('\1' returns a character with octal code 1).
* Add '?' after '*' and '+' to make them non-greedy.

### Match Object

```py
<str>   = <Match>.group()                      # Returns the whole match. Also group(0).
<str>   = <Match>.group(1)                     # Returns part in the first bracket.
<tuple> = <Match>.groups()                     # Returns all bracketed parts.
<int>   = <Match>.start()                      # Returns start index of the match.
<int>   = <Match>.end()                        # Returns exclusive end index of the match.
```

### Special Sequences

```py
'\d' == '[0-9]'                                # Matches decimal characters.
'\w' == '[a-zA-Z0-9_]'                         # Matches alphanumerics and underscore.
'\s' == '[ \t\n\r\f\v]'                        # Matches whitespaces.
```

## Datetime

[16_Day_Python_date_time](https://github.com/androchentw/30-Days-Of-Python/blob/master/16_Day_Python_date_time/16_python_datetime.md)

```py
from datetime import datetime
now = datetime.now()
year = now.year
timestamp = now.timestamp()
print(now)    # 2021-07-08 07:34:46.549883

new_year = datetime(2020, 1, 1)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y") 
```

[datetime: python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#datetime)

```py
<D>  = date(year, month, day)               # Only accepts valid dates from 1 to 9999 AD.
<T>  = time(hour=0, minute=0, second=0)     # Also: `microsecond=0, tzinfo=None, fold=0`.
<DT> = datetime(year, month, day, hour=0)   # Also: `minute=0, second=0, microsecond=0, …`.
<TD> = timedelta(weeks=0, days=0, hours=0)  # Also: `minutes=0, seconds=0, microsecond=0`.

<tzinfo> = UTC                              # UTC timezone. London without DST.
<tzinfo> = tzlocal()                        # Local timezone. Also gettz().
<tzinfo> = gettz('<Continent>/<City>')      # 'Continent/City_Name' timezone or None.
<DTa>    = <DT>.astimezone(<tzinfo>)        # Datetime, converted to the passed timezone.
<Ta/DTa> = <T/DT>.replace(tzinfo=<tzinfo>)  # Unconverted object with a new timezone.
```

* Use '<D/DT>.weekday()' to get the day of the week as an int, with Monday being 0.
