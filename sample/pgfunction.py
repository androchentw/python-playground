#!/usr/bin/env python3
#
# Reference
#   3-syntax/   Function, Decorator, Enum
#
# Requirements
#
# Usage: python pgfunction.py
from enum import Enum, unique
from random import randint


def main():
    demo_enum()


def demo_enum():
    print("\ndemo_enum")
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


if __name__ == "__main__":
    main()
