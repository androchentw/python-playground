"""
!/usr/bin/env python3

Reference
  PyTest, report, mock data
  8-test/

Requirements
  $ pip3 install pytest

Usage: python pgtest.py
"""
import subprocess


def main():
    demo_unit_test()


def demo_unit_test():
    result = subprocess.run(
        "python3 -m pytest test/ --junitxml=reports/junit/junit.xml",
        shell=True,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    print(result.stdout)


def hello(text, **kwargs):
    name = kwargs.get("name", "username")
    return f"hello: {text}~ {name}."


if __name__ == "__main__":
    main()
