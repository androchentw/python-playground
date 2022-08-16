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
