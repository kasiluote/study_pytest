import pytest

@pytest.fixture
def func_simple():
    '''

    :return: sys.path contains string 'testpath' and will be popped in the following test_func.
    '''
    import sys
    sys.path.append("testpath")
    return sys.path

def test_func(func_simple):
    testpath = func_simple.pop()
    assert testpath == "testpath"
    assert 0 # Check the content of func_simple

'''
  Simple usage of pytest.fixture:
    1. Define a test function with decorator "pytest.fixture"
    2. Set the test function to the formal parameter（形参）of 'test_**'.
    3. Check the result.

  Official explanation:
  Here is the exact protocol used by pytest to call the test function this way:
    1. pytest finds the test_ehlo because of the test_ prefix.
    The test function needs a function argument named smtp_connection.
    A matching fixture function is discovered by looking for a fixture-marked function named smtp_connection.
    2. smtp_connection() is called to create an instance.
    3. test_ehlo(<smtp_connection instance>) is called and fails in the last line of the test function.
    Note that if you misspell a function argument or want to use one that isn’t available, you’ll see an error with a list of
available function arguments.

pytest --fixtures test_simplefactory.py

--------------- fixtures defined from chap4.test_fixture_simple ---------------
func_simple

    :return: sys.path contains string 'testpath' and will be popped in the following test_func.

'''