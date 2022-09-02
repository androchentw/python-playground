import pytest
import pgtest_sample_func


def test_equal():
    assert pgtest_sample_func.equal(1, 1) == True
    assert pgtest_sample_func.equal(-2, -2) == True
    assert pgtest_sample_func.equal("0", "0") == True
    assert pgtest_sample_func.equal(1e3, 1000) == True
    assert pgtest_sample_func.equal(1e-2, 0.01) == True
    assert pgtest_sample_func.equal(1.02e03, 1020) == True


def test_hello():
    assert (
        pgtest_sample_func.hello("world", name="test-developer")
        == "hello: world~ test-developer."
    )
