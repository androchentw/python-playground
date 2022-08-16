"""
!/usr/bin/env python3

Reference
  1-collections/  Dict,
  2-types/    Regex, Dateime.

Requirements

Usage: python pgtype.py
"""
from datetime import datetime


def main():
    demo_dictionary()
    demo_list()
    demo_type()

    demo_string()
    demo_datetime()
    demo_regex()


def demo_dictionary():
    print("\n# demo_dictionary")
    fruits = {"apple": 10, "banana": 7, "orange": 8}
    print(fruits["banana"])
    print(fruits.get("strawberry", "default_strawberry"))
    fruits.update({"grape": 2, "lemon": 3})
    for key, value in fruits.items():
        print(key, value)


def demo_list():
    print("\n# demo_list")
    animals = ["cat", "bear", "dog", "elephant"]
    print(animals.index("cat"))
    print(animals.count("bear"))
    animals.sort()
    print(animals)


def demo_type():
    print("\n# demo_type")
    print(type(10))  # Int
    print(type(3.14))  # Float
    print(type(1 + 3j))  # Complex
    print(type("Asabeneh"))  # String
    print(type([1, 2, 3]))  # List
    print(type({"name": "Asabeneh"}))  # Dictionary
    print(type({9.8, 3.14, 2.7}))  # Set
    print(type((9.8, 3.14, 2.7)))  # Tuple


def demo_string():
    print("\n# demo_string")
    language = "Python"
    print(language[0:3])  # Pyt
    print(language[3:6])  # hon
    print(language[-3:])  # hon

    challenge = "thirty days of python"
    print(challenge.upper())  # 'THIRTTY DAYS OF PYTHON'
    print(challenge.count("th"))  # 2`
    print(challenge.endswith("on"))  # True
    print(challenge.find("th"))  # 17

    sub_string = "da"
    print(challenge.index(sub_string))  # 7

    web_tech = ["HTML", "CSS", "JavaScript", "React"]
    print("# ".join(web_tech))  # 'HTML# CSS# JavaScript# React'

    print(challenge.replace("python", "coding"))  # 'thirty days of coding'
    print(challenge.split())  # ['thirty', 'days', 'of', 'python']


def demo_datetime():
    print("\n# demo_datetime")
    now = datetime.now()
    year = now.year
    timestamp = now.timestamp()
    print(now)  # 2021-07-08 07:34:46.549883

    new_year = datetime(2020, 1, 1)
    time_one = now.strftime("%m/%d/%Y, %H:%M:%S")

    date_string = "5 December, 2019"
    date_object = datetime.strptime(date_string, "%d %B, %Y")


def demo_regex():
    print("\n# demo_regex")


if __name__ == "__main__":
    main()
