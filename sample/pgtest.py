"""
!/usr/bin/env python3

Reference
  PyTest, report, mock data
  8-test/

Requirements
  $ pip3 install pytest

Usage: python pgtest.py
"""
import argparse
import subprocess
import sys


def main():
    args = parse_args()
    print(type(args.throw_test_fail))
    demo_unit_test(args.throw_test_fail)


def demo_unit_test(throw_test_fail=False):
    # $ allure serve reports/allure
    result = subprocess.run(
        f"python3 -m pytest test/ --capture=tee-sys --junitxml=reports/junit.xml \
            --html=reports/report.html --self-contained-html \
            --alluredir=reports/allure",
        shell=True,
        check=throw_test_fail,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    print(f"result.stdout\n{result.stdout}")
    print(f"result.stderr\n{result.stderr}")


def parse_args():
    parser = argparse.ArgumentParser(description="pytest demo")
    parser.add_argument(
        "-ttf",
        "--throw-test-fail",
        default=False,
        required=False,
        action="store_true",
        help="Throw test fail exit status",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
    sys.exit(0)
