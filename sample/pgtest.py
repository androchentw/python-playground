"""
!/usr/bin/env python3

Reference
  PyTest, report, mock data
  8-test/

Requirements
  $ pip3 install pytest

Usage: python3 pgtest.py
"""
import argparse
import subprocess
import sys


def main():
    args = parse_args()
    print(type(args.throw_test_fail))
    demo_unit_test(args.throw_test_fail)
    integrate_test_report()


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


def demo_unit_test(throw_test_fail=False):
    # $ allure serve reports/allure
    run_shell_command(
        "python3 -m pytest test/ --capture=tee-sys --junitxml=reports/junit.xml \
            --html=reports/report.html --self-contained-html \
            --alluredir=reports/allure",
        throw_test_fail,
    )


def integrate_test_report():
    run_shell_command("genbadge tests --input-file reports/junit.xml")
    run_shell_command("mv tests-badge.svg reports/")


def run_shell_command(command="ls", check_fail=False):
    result = subprocess.run(
        command,
        shell=True,
        check=check_fail,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    print(f"run_shell_command: {command}  \n{result.stdout} \n {result.stderr}")


if __name__ == "__main__":
    main()
    sys.exit(0)
