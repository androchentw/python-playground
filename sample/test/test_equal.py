import pytest
import pgtest


def test_equal():
    assert 1 == 1


def test_hello():
    assert (
        pgtest.hello("world", name="test-developer")
        == "hello: world~ test-developer."
    )
