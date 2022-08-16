"""
!/usr/bin/env python3

Reference
  Class, Object
  3-syntax/

Requirements

Usage: python pgclass.py
"""

def main():
    demo_class()


def demo_class():
    print("\n# demo_class")
    p_andro = Person("andro", 32)
    p_andro.info = "passionate developer"
    print(p_andro.info)
    print(p_andro)

    e_andro = Employee("andro", 32, 999)
    print(e_andro.staff_num)
    print(e_andro.get_class_name)



# Inheritance. Overriding parent method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # direct call
    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.age!r})"

    # print
    def __str__(self):
        return str(self.name) + ":" + str(self.age)

    @property
    def info(self):
        return '::'.join(self._info)

    @info.setter
    def info(self, value):
        self._info = value.split()


class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num

    @classmethod
    def get_class_name(cls):
        return cls.__name__



if __name__ == "__main__":
    main()
