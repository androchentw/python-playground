#!/usr/bin/env python3
#
# Reference
#   loguru + Exception
#   3-syntax/exception
#   7-libraries/Logging
#
# Requirements
# $ pip3 install loguru
#
# Usage: python pgtest.py
from loguru import logger


def main():
    init()
    demo_logger()
    demo_decorator_func(0, 0, 0)
    demo_except_catch_func(0)
    pass


def init():
    logger.add(
        "pglog.log",
        # serialize=True,   # to JSON format
        enqueue=True,  # Asynchronous, Thread-safe, Multiprocess-safe
        backtrace=True,  # Caution, may leak sensitive data in prod
        diagnose=True,
        format="{time:%F %T%z}, {level}, {message}.",
    )


def demo_logger():
    logger.info(
        "If you're using Python {}, prefer {feature} of course!",
        3.6,
        feature="f-strings",
    )
    logger.debug("msg debug")
    logger.warning("msg warning")
    logger.error("msg ERROR")


@logger.catch
def demo_decorator_func(x, y, z):
    return 1 / (x + y + z)


def demo_except_func(a, b):
    return a / b


def demo_except_catch_func(c):
    try:
        demo_except_func(5, c)
    except ZeroDivisionError:
        logger.exception("msg exception")


if __name__ == "__main__":
    main()
