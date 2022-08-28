# python-playground

<p align="center">
  <img style="width:60%;" src="https://i.imgur.com/Qe3Dzt6.png">
  <br/>
  <sub><sup>(Photo by <a href="https://unsplash.com/@clemhlrdt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Clément Hélardot</a> on <a href="https://unsplash.com/collections/SV-KO-htOoM/my-first-collection/9b0020f22e02b780910afe3a322692d8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>)</sup></sub>
</p>

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/androchentw/python-playground/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/androchentw/python-playground/tree/main)

Blog: [Github - Python Playground](https://blog.androchen.tw/github-python-playground/)

Sample code for common modules in Python.

Inspired by 

1. [python-cheatsheet](https://github.com/androchentw/python-cheatsheet)
2. [30-Days-Of-Python](https://github.com/androchentw/30-Days-Of-Python)
  

## Sample Playground

```
sample
├─ reports                  # test report
│  ├─ allure                  # allure report
│  ├─ junit.xml               # junit report
│  └─ report.html             # html report
├─ test                     # test python folder
│  ├─ pgtest_sample_func.py   # test sample funciton
│  ├─ pgtest_sample.log       # sample test log
│  ├─ test_equal.py           # demo test pass
│  └─ test_equal_fail.py      # demo test fail, skip
├─ pgclass.py               # 3-syntax/ Class, Object
├─ pgfunction.py            # 3-syntax/ Function, Decorator, Enum
├─ pglog.py                 # 7-libraries/ loguru + Exception
├─ pglog_sample.log           # sample log
├─ pgrequest.py             # 5-data/, 7-libraries/ Web: API request + JSON parsing
├─ pgrequest_sample.json      # sample api response json
├─ pgsys.py                 # 3-system/ system, os, file
├─ pgtest.py                # 8-test/ PyTest, report, mock data
├─ pgtype.py                # 1-collections/, 2-types/ Dict, Regex, Dateime
└─ requirements.txt         # pip3 install -r requirements.txt
```


## Table of Contents

1. **Collections**: List, **[Dictionary]**, Set, Tuple, Range, Enumerate, Iterator, Generator.
2. **Types**: Type, [String], Regular_Exp, Format, Numbers, Combinatorics, **[Datetime]**.
3. **Syntax**: **Function**, (Args, Inline), **Module**, Import, **Decorator**, **[Class]**, Duck_Types, **Enum**, **[Exception]**.
4. **System**: Exit, Print, Input, Command_Line_Arguments, Open, **[Path]**, **[OS_Commands]**.
5. **Data**: **[JSON]**, Pickle, CSV, SQLite, Bytes, Struct, Array, Memory_View, Deque
6. **Advanced**: **[Threading]**, Operator, Introspection, Metaprograming, Eval, Coroutines.
7. **Libraries**: Progress_Bar, Plot, Table, Curses, **[Logging]**, Scraping, **[Web]**, Profile, NumPy, Image, Audio, Games, Data.
8. **Test**: **[Pytest]**, mock
9. **Style**: **[PEP8]**

## Ref

* [Complete Python Roadmap for Beginners in 2022](https://copyassignment.com/complete-python-roadmap-for-beginners-in-2022/)

<img style="width:60%;" src="https://copyassignment.com/wp-content/uploads/2022/08/Python-Complete-Roadmap-for-Beginners-1536x1152.jpg">

<!-- Links -->

[Dictionary]: 1-collections/README.md#dictionary
[String]: 2-types/README.md#string
[Datetime]: 2-types/README.md#datetime
[Class]: 3-syntax/README.md#class
[Exception]: 3-syntax/README.md#exception

[Path]: 4-system/README.md#path
[OS_Commands]: 4-system/README.md#os-commands
[JSON]: 5-data/README.md#json
[Threading]: 6-advanced/README.md#threading

[Web]: 7-libraries/README.md#web
[Logging]: 7-libraries/README.md#logging
[Pytest]: 8-test/README.md#pytest
[PEP8]: 9-style/README.md#pep8
