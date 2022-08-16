#!/usr/bin/env python3
#
# Reference
#   1-collections/  Dict, 
#   2-types/    Regex, Dateime.
#
# Requirements
#
# Usage: python pgtype.py
from datetime import datetime
from enum import Enum, unique
from random import randint


def main():
    demo_dictionary()
    demo_list()
    demo_type()

    demo_string()
    demo_datetime()
    demo_regex()


def demo_dictionary():
    print("\ndemo_dictionary")
    fruits = {"apple": 10, "banana": 7, "orange": 8}
    print(fruits["banana"])
    print(fruits.get("strawberry", "default_strawberry"))
    fruits.update({"grape": 2, "lemon": 3})
    for key, value in fruits.items():
        print(key, value)


def demo_list():
    print("\ndemo_list")
    animals = ["cat", "bear", "dog", "elephant"]
    print(animals.index("cat"))
    print(animals.count("bear"))
    animals.sort()
    print(animals)


def demo_type():
    print("\ndemo_type")
    print(type(10))  # Int
    print(type(3.14))  # Float
    print(type(1 + 3j))  # Complex
    print(type("Asabeneh"))  # String
    print(type([1, 2, 3]))  # List
    print(type({"name": "Asabeneh"}))  # Dictionary
    print(type({9.8, 3.14, 2.7}))  # Set
    print(type((9.8, 3.14, 2.7)))  # Tuple


def demo_string():
    print("\ndemo_string")
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
    print("\ndemo_datetime")
    now = datetime.now()
    year = now.year
    timestamp = now.timestamp()
    print(now)  # 2021-07-08 07:34:46.549883

    new_year = datetime(2020, 1, 1)
    time_one = now.strftime("%m/%d/%Y, %H:%M:%S")

    date_string = "5 December, 2019"
    date_object = datetime.strptime(date_string, "%d %B, %Y")


def demo_regex():
    print("\ndemo_regex")


def demo_enum():
    print("\ndemo_enum")
    week = Enum(
        "Week", "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
    )
    print(week.Monday.name)  # Monday
    print(week.Monday.value)  # 1

    print(Color.RED.value)  # color1 獲得 (255, 0, 0)
    print(Color.random_color())  # 隨機獲得顏色 RGB


# 建立一個列舉型態的類別
# @unique 能夠檢查列舉是否有重複的列舉值
# 在參數中填上 Enum 宣告為列舉型態
@unique
class Color(Enum):
    # 定義一些基本顏色作為列舉名稱，而列舉值是其對應的RGB數值
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # 定義靜態方法，可以由外部直接使用
    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


if __name__ == "__main__":
    main()
