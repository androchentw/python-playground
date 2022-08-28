import pytest

# demo fail
@pytest.mark.skip(reason="skip for cicd to run pass")
def test_equal_fail():
    assert 1 != 1


@pytest.mark.skip(reason="demo skip fail")
def test_equal_skip_fail():
    assert 2 != 2


@pytest.mark.skip(reason="demo skip success")
def test_equal_skip_success():
    assert 2 != 2
