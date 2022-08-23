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
    # $ allure serve reports/allure
    result = subprocess.run(
        f"python3 -m pytest test/ --capture=tee-sys --junitxml=reports/junit.xml \
            --html=reports/report.html --self-contained-html \
            --alluredir=reports/allure",
        shell=True,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    print(result.stdout)
    print(result.stderr)


def hello(text, **kwargs):
    name = kwargs.get("name", "username")
    return f"hello: {text}~ {name}."


if __name__ == "__main__":
    main()
