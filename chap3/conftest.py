#Defining your own assertion comparison
from chap3.test_foocompare import Foo
def pytest_assertrepr_compare(op,left,right):
    if isinstance(left,Foo) and isinstance(right,Foo) and op == "==":
        return ['Comparing Foo instance:',
                '    vals:  %s  != %s ' % (left.val, right.val)]

