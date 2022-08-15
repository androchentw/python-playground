# Data

## JSON

[JSON: python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#json)

```py
import json
<str>    = json.dumps(<object>)    # Converts object to JSON string.
<object> = json.loads(<str>)       # Converts JSON string to object.


def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)

def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)
```


## CSV

```py
<reader> = csv.reader(<file>)       # Also: `dialect='excel', delimiter=','`.
<list>   = next(<reader>)           # Returns next row as a list of strings.
<list>   = list(<reader>)           # Returns a list of remaining rows.

<writer> = csv.writer(<file>)       # Also: `dialect='excel', delimiter=','`.
<writer>.writerow(<collection>)     # Encodes objects using `str(<el>)`.
<writer>.writerows(<coll_of_coll>)  # Appends multiple rows.

def read_csv_file(filename, dialect='excel'):
    with open(filename, encoding='utf-8', newline='') as file:
        return list(csv.reader(file, dialect))

def write_to_csv_file(filename, rows, dialect='excel'):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, dialect)
        writer.writerows(rows)
```

* File must be opened with a 'newline=""' argument, or newlines embedded inside quoted fields will not be interpreted correctly!
