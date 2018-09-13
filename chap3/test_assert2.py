#Assertions about expected exceptions

import pytest

#Default mode
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0

#With pytest.mark.xfail
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_zero_division2():
    1/0


#default mode
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)

# excinfo is a ExceptionInfo instance, which is a wrapper around the actual exception raised. The main attributes
# of interest are .type, .value and .traceback.

#with pytest.mark.xfail
def f():
    f()
@pytest.mark.xfail(raises=RecursionError)
def test_f():
    f()



def myfunc():
    raise ValueError("exception 123 raised")

#default mode
def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()

#With pytest.mark.xfail
@pytest.mark.xfail(raises=ValueError)
def test_match1():
    myfunc()


# Assertions about expected warnings
# New in version 2.8.
# You can check that code raises a particular warning using pytest.warns.

def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2

#Special comparisons are done for a number of cases:
#comparing long strings: a context diff is shown
#comparing long sequences: first failing indices
#comparing dicts: different entries#