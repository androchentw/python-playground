# Libraries

## Progress Bar

```py
# $ pip3 install tqdm
>>> from tqdm import tqdm
>>> from time import sleep
>>> for el in tqdm([1, 2, 3], desc='Processing'):
...     sleep(1)
Processing: 100%|████████████████████| 3/3 [00:03<00:00,  1.00s/it]
```

## Logging

* [Logging: python-cheatsheet](https://github.com/androchentw/python-cheatsheet/blob/master/README.md#logging)
* [Delgan/loguru](https://github.com/Delgan/loguru)
* [Loguru：优雅的Python程序日志](https://cloud.tencent.com/developer/article/1664382)
* [Loguru：更爲優雅、簡潔的 Python 日誌管理模塊](https://www.readfog.com/a/1640196300205035520)


```py
# $ pip3 install loguru
from loguru import logger

# Modern string formatting using braces style
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")

# Exceptions catching within threads or main
@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)

# Asynchronous, Thread-safe, Multiprocess-safe
logger.add("somefile.log", enqueue=True)

# Fully descriptive exceptions
logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)

# Structured logging as needed
logger.add(custom_sink_function, serialize=True)    # log as JSON format

# Using bind() you can contextualize your logger messages by modifying the extra record attribute.
logger.add("file.log", format="{extra[ip]} {extra[user]} {message}")
context_logger = logger.bind(ip="192.168.0.1", user="someone")
context_logger.info("Contextualize your logger easily")
context_logger.bind(user="someone_else").info("Inline binding of extra attribute")
context_logger.info("Use kwargs to add context during formatting: {user}", user="anybody")

# Better datetime handling
logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

# Need to propagate Loguru messages to standard logging?
class PropagateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)

logger.add(PropagateHandler(), format="{message}")

# Exhaustive notifier
import notifiers
```

* Levels: 'debug', 'info', 'success', 'warning', 'error', 'critical'.

## Web

```py
# $ pip3 install bottle
from bottle import run, route, static_file, template, post, request, response
import json

@post('/<sport>/odds')
def send_json(sport):
    team = request.forms.get('team')
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'team': team, 'odds': [2.09, 3.74, 3.68]})

# Test
# $ pip3 install requests
>>> import threading, requests
>>> threading.Thread(target=run, daemon=True).start()
>>> url = 'http://localhost:8080/football/odds'
>>> request_data = {'team': 'arsenal f.c.'}
>>> response = requests.post(url, data=request_data)
>>> response.json()
{'team': 'arsenal f.c.', 'odds': [2.09, 3.74, 3.68]}
```

## Profiling

