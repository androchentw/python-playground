# Style

## PEP8


* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [PEP8 PYTHON 編碼規範手冊](https://cflin.com/wordpress/603/pep8-python編碼規範手冊)
* [pylint]

* Indentation: Use 4 spaces per indentation level.
* Maximum Line Length: Limit all lines to a maximum of 79 characters.
* Naming Conventions
  * Package and Module Names: Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.
  * Class Names: Class names should normally use the `CapWords` convention.
  * Function and Variable Names
    * Function names should be `lowercase`, with words separated by underscores as necessary to improve readability.
    * Variable names follow the same convention as function names.
  * Function and Method Arguments
    * Always use `self` for the first argument to instance methods.
    * Always use `cls` for the first argument to class methods.
  

```
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)



# Don’t use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter:

# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```