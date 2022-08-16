#!/usr/bin/env python3
#
# Reference
#   Web: API request + JSON parsing
#   5-data/JSON
#   7-libraries/22_Day_Web_scraping
#
# Requirements
#
# Usage: python pgrequest.py
import json
import requests


def main():
    demo_api_get()
    demo_api_post()


def demo_api_get():
    print("\n# demo_api_get")
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url, verify=False)
    print(response.json())
    # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    print(response.status_code)  # 200
    print(response.headers["Content-Type"])  # 'application/json; charset=utf-8'


def demo_api_post():
    print("\n# demo_api_post")
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 9, "title": "Test code", "completed": False}
    response = requests.post(api_url, json=todo, verify=False)
    print(response.json())
    # {'userId': 9, 'title': 'Test code', 'completed': False, 'id': 201}
    print(response.status_code)  # 201

    print("\n## write and read json file")
    write_to_json_file("pgrequest_sample.json", response.json())
    print(read_json_file("pgrequest_sample.json"))


def read_json_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def write_to_json_file(filename, an_object):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
