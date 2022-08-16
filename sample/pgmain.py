#!/usr/bin/env python3
#
# Reference
#   3-syntax/
#   4-system/exit
#
# Requirements
#
# Usage: python pgmain.py <name> <challenge>
import os
import sys
from pathlib import Path


def main():
    demo_os_dir()
    demo_sys_input()

    # Datetime + Enum


def demo_os_dir():
    print(os.getcwd())
    os.mkdir("pgmain_demo_os_dir")
    os.chdir("pgmain_demo_os_dir")
    print(os.getcwd())
    os.chdir("../")
    os.rmdir("pgmain_demo_os_dir")
    


def demo_sys_input():
    print(f"Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!")


# Runs main() if file wasn't imported.
if __name__ == "__main__":
    main()

    sys.exit()
