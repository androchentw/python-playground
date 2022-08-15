# System

## Exit

```py
import sys
sys.exit()                        # Exits with exit code 0 (success).
sys.exit(<el>)                    # Prints to stderr and exits with 1.
sys.exit(<int>)                   # Exits with passed exit code.
```


## Command_Line_Arguments

Command Line Arguments

```py
import sys
scripts_path = sys.argv[0]
arguments    = sys.argv[1:]
```

## File

```py
<file> = open(<path>, mode='r', encoding=utf-8, newline=None)
<file>.seek(0)                      # Moves to the start of the file.
<file>.seek(offset)                 # Moves 'offset' chars/bytes from the start.
<file>.seek(0, 2)                   # Moves to the end of the file.
<bin_file>.seek(±offset, <anchor>)  # Anchor: 0 start, 1 current position, 2 end.

# Read Text from File
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()

# Write Text to File
def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
```

* 'encoding=None' means that the default encoding is used, which is platform dependent. Best practice is to use 'encoding="utf-8"' whenever possible.
* 'newline=None' means all different end of line combinations are converted to '\n' on read, while on write all '\n' characters are converted to system's default line separator.
* 'newline=""' means no conversions take place, but input is still broken into chunks by readline() and readlines() on every '\n', '\r' and '\r\n'.

### modes
* 'r' - Read (default).
* 'w+' - Read and write (truncate).
* 'r+' - Read and write from the start.
* 'a+' - Read and write from the end.

### Exceptions
* 'FileNotFoundError' can be raised when reading with 'r' or 'r+'.
* 'FileExistsError' can be raised when writing with 'x'.
* 'IsADirectoryError' and 'PermissionError' can be raised by any.
* 'OSError' is the parent class of all listed exceptions.


## Path


```py
# OS Module
# import the module
import os
os.mkdir('directory_name')  # Creating a directory
os.chdir('path')    # Changing the current directory
os.getcwd() # Getting current working directory
os.rmdir()  # Removing directory

# System Module
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

$ python script.py Asabeneh 30DaysOfPython
>>> Welcome Asabeneh. Enjoy  30DayOfPython challenge! 
```


```py
from os import getcwd, path, listdir, scandir
from glob import glob

<str>  = getcwd()                   # Returns the current working directory.
<str>  = path.join(<path>, ...)     # Joins two or more pathname components.
<str>  = path.abspath(<path>)       # Returns absolute path.

<str>  = path.basename(<path>)      # Returns final component of the path.
<str>  = path.dirname(<path>)       # Returns path without the final component.
<tup.> = path.splitext(<path>)      # Splits on last period of the final component.

<list> = listdir(path='.')          # Returns filenames located at path.
<list> = glob('<pattern>')          # Returns paths matching the wildcard pattern.

<bool> = path.exists(<path>)        # Or: <Path>.exists()
<bool> = path.isfile(<path>)        # Or: <DirEntry/Path>.is_file()
<bool> = path.isdir(<path>)         # Or: <DirEntry/Path>.is_dir()

<stat> = os.stat(<path>)            # Or: <DirEntry/Path>.stat()
<real> = <stat>.st_mtime/st_size/…  # Modification time, size in bytes, …
```

### Path Object

```py
from pathlib import Path

<Path> = Path()                     # Returns relative cwd. Also Path('.').
<Path> = Path.cwd()                 # Returns absolute cwd. Also Path().resolve().
<Path> = Path.home()                # Returns user's home directory (absolute).

<Path> = <Path>.parent              # Returns Path without the final component.
<str>  = <Path>.name                # Returns final component as a string.
<str>  = <Path>.stem                # Returns final component without extension.
<str>  = <Path>.suffix              # Returns final component's extension.
<tup.> = <Path>.parts               # Returns all components as strings.

<str>  = str(<Path>)                # Returns path as a string.
<file> = open(<Path>)               # Also <Path>.read/write_text/bytes().
```


## OS_Commands

```py
import os, shutil, subprocess

os.chdir(<path>)                 # Changes the current working directory.
os.mkdir(<path>, mode=0o777)     # Creates a directory. Mode is in octal.
os.makedirs(<path>, mode=0o777)  # Creates all path's dirs. Also: `exist_ok=False`.

shutil.copy(from, to)            # Copies the file. 'to' can exist or be a dir.
shutil.copytree(from, to)        # Copies the directory. 'to' must not exist.

os.rename(from, to)              # Renames/moves the file or directory.
os.replace(from, to)             # Same, but overwrites 'to' if it exists.

os.remove(<path>)                # Deletes the file.
os.rmdir(<path>)                 # Deletes the empty directory.
shutil.rmtree(<path>)            # Deletes the directory.
```

### Shell Commands

```py
<pipe> = os.popen('<command>')   # Executes command in sh/cmd and returns its stdout pipe.
<str>  = <pipe>.read(size=-1)    # Reads 'size' chars or until EOF. Also readline/s().
<int>  = <pipe>.close()          # Closes the pipe. Returns None on success, int on error.

# sample 1
>>> subprocess.run('bc', input='1 + 1\n', capture_output=True, text=True)
CompletedProcess(args='bc', returncode=0, stdout='2\n', stderr='')

# sample 2
>>> from shlex import split
>>> os.popen('echo 1 + 1 > test.in')
>>> subprocess.run(split('bc -s'), stdin=open('test.in'), stdout=open('test.out', 'w'))
CompletedProcess(args=['bc', '-s'], returncode=0)
>>> open('test.out').read()
'2\n'
```
