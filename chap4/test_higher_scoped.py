import pytest

I = 1


@pytest.fixture(scope='session')
def s1():
    return 's1'

@pytest.fixture(scope='module')
def m1():
    return 'm1'

@pytest.fixture
def f1(tmpdir):
    return tmpdir

@pytest.fixture
def f2():
    return 'f2'

def test_foo(f1,m1,f2,s1):
    # f1 = local('C:\\Users\\zyu\\AppData\\Local\\Temp\\pytest-of-zyu\\pytest-10\\test_foo0')
    assert m1 == 'm1'
    assert f2 == 'f2'
    assert s1 == 's1'

#The fixtures requested by test_foo will be instantiated in the following order:
#1. s1: is the highest - scoped fixture (session).
#2. m1: is the second highest-scoped fixture (module).
#3. tmpdir: is a function-scoped fixture, required by f1: it needs to be instantiated at this point because it is a dependency of f1.
#4.# f1: is the first function-scoped fixture in test_foo parameter list.
#5. f2: is the last function-scoped fixture in test_foo parameter list.