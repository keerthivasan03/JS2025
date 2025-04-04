"""def test_method():
    print("my first pytes code")
    assert True
"""

"""def test_method():
    print("my first pytest code")
    assert True 
"""
#pytest custom run
import pytest

@pytest.mark.regression
def test_1():
    print("Test 2")

@pytest.mark.xfail
def test_2():
    print("Test 3")
    assert 4==5

#we can have two label for same testcase
@pytest.mark.login
@pytest.mark.regression
def test_3():
    print("Test 2")