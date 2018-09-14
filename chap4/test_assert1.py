#Asserting with the assert statement

def f():
    return 3

def test_function():
    assert f() == 4

def test_odd():
    a = 5
    assert a % 2 == 0, "value was odd, should be even"
#However, if you specify a message with the assertion like this:
#then no assertion introspection takes places at all and the message will be simply shown in the traceback.
