"""
!/usr/bin/env python3

Reference
  system, os, file
  4-system/

Requirements

Usage: python pgsys.py <name> <challenge>
"""
import inspect
import os
import shutil
import sys
from pathlib import Path


def main():
    demo_inspect()
    demo_sys_input()
    demo_os_dir()
    demo_handle_file()
    demo_shell()


def demo_inspect():
    print("\n# demo_inspect")
    print(inspect.stack()[0].function)
    print(inspect.stack()[1].function)
    print(inspect.stack()[2].function)
    # stack()[0] is the current function, demo_inspect
    # stack()[1] is the father of current function, main
    # and so on.


def demo_sys_input():
    print("\n# demo_sys_input")
    print(f"Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!")


def demo_os_dir():
    print("\n# demo_os_dir")
    print(os.getcwd())
    os.mkdir("pgmain_demo_os_dir")
    os.chdir("pgmain_demo_os_dir")
    print(os.getcwd())
    os.chdir("../")

    shutil.copytree("pgmain_demo_os_dir", "copy_dir1")
    os.replace("pgmain_demo_os_dir", "replace1")
    os.rmdir("replace1")
    os.rename("copy_dir1", "rename1")
    shutil.rmtree("rename1")


def demo_handle_file():
    print("\n# demo_handle_file")
    write_to_file("sample.txt", "1\n2\n3\n")
    print(read_file("sample.txt"))

    shutil.copy("sample.txt", "copy1")
    os.remove("copy1")

    print("sample.txt exists(): {}".format(Path("sample.txt").exists()))
    print("sample.txt is_file(): {}".format(Path("sample.txt").is_file()))
    os.remove("sample.txt")


# Read Text from File
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        return file.readlines()


# Write Text to File
def write_to_file(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def demo_shell():
    pass


# Runs main() if file wasn't imported.
if __name__ == "__main__":
    main()

    sys.exit()
