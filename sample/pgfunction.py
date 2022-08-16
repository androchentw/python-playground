"""
!/usr/bin/env python3

Reference
  3-syntax/   Function, Decorator, Enum

Requirements

Usage: python pgfunction.py
"""
from enum import Enum, unique
from functools import wraps
from random import randint


def main():
    demo_enum()
    demo_lambda()
    demo_decorator()


def demo_enum():
    print("\n# demo_enum")
    week = Enum(
        "Week", "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
    )
    print(week.Monday.name)  # Monday
    print(week.Monday.value)  # 1

    print(Color.RED.value)  # (255, 0, 0)
    print(Color.random_color())


# @unique = check dupplicated enum
@unique
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # @staticmethod = public usable
    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


def demo_lambda():
    print("\n# demo_lambda")
    f = lambda param1, param2, param3: param1 + param2 + param3
    print(f(1, 2, 3))  # 6

    square = lambda x: x**2
    print(square(3))  # 9

    # Lambda Function Inside Another Function
    def power(x):
        return lambda n: x**n

    cube = power(2)(3)
    print(cube)  # 8
    two_power_of_five = power(2)(5)
    print(two_power_of_five)  # 32


def demo_decorator():
    print("\n# demo_decorator")
    print(greeting())  # WELCOME TO PYTHON

    print(add(1, 2))


# First decorator
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
@uppercase_decorator
# order with decorators is important in this case
# .upper() function does not work with lists
def greeting():
    return "Welcome to Python"


def debug(print_result=False):
    def decorator(func):
        @wraps(func)
        def out(*args, **kwargs):
            result = func(*args, **kwargs)
            print("internal: ", func.__name__, result if print_result else "")
            return result

        return out

    return decorator


@debug(print_result=True)
def add(x, y):
    return x + y


if __name__ == "__main__":
    main()
