import pytest
import pgtest


def test_equal():
    assert (1 == 1)


def test_hello():
    assert (
        pgtest.hello("world", name="pgtest-developer")
        == "hello: world~ pgtest-developer."
    )

@pytest.mark.skip(reason="specify skip resaon")
def test_skip():
    assert (1 == 1)