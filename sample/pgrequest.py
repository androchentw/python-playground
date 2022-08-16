#!/usr/bin/env python3
#
# Reference
#   5-data/JSON    
#   7-libraries/22_Day_Web_scraping
#
# Requirements
#
# Usage: python pgrequest.py
import json


def main():
    pass


def read_json_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def write_to_json_file(filename, an_object):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
