import pytest
from contextlib import contextmanager

@pytest.fixture(scope="module")
def func_simple():
    '''

    :return: sys.path contains string 'testpath' and will be popped in the following test_func.
    '''
    import sys
    sys.path.append("testpath")
    return sys.path

# if set scope="module" here will raise RuntimeError: generator didn't yield
@pytest.fixture
# contextmanager must be put under pytest.fixture else the decorator doesn't work at all.
@contextmanager
def func_y():
    try:
        var1 = lambda x : x+10
        yield var1
    finally:
        print("teardown var1")


@pytest.fixture
def func_y2(tmpdir):
    file_path = tmpdir+'\\test1.txt'
    with open(file_path,'a+') as f:
        f.write('hello pytest \n')
    with open(file_path) as f1:
        yield f1

@pytest.fixture(scope="module")
def f_yield1():
    f_yield1 = lambda x : x+10086
    yield f_yield1
    print("teardown f_yield1")
    print('f_yield1 teardown finish')

class aaa():
    def __enter__(self):
        self.varl = 15
        return self

    def __exit__(self,exc_type,exc_value,exc_traceback):
        print("ok")


@pytest.fixture(scope="module")
def f_yield2():
    with aaa() as f_yield2:
        yield f_yield2
    print("teardown f_yield2")


@contextmanager
def bbb():
    try:
        xx = 123
        yield xx
    finally:
        print("teardown bbb")

@pytest.fixture(scope="module")
def f_yield3():
    with bbb() as f_yield3:
        yield f_yield3
    print("teardown f_yield3")

@pytest.fixture(scope="module")
def f_req1(request):
    f_req1 = bbb()

    def fin1():
        print("teardown f_req1")
    request.addfinalizer(fin1)
    return f_req1

#Both yield and addfinalizer methods work similarly by calling their code after the test ends, but
#addfinalizer has two key differences over yield:
# 1. It is possible to register multiple finalizer functions.
# 2. Finalizers will always be called regardless if the fixture setup code raises an exception. This is handy to properly
# close all resources created by a fixture even if one of them fails to be created/acquired

class ccc():
    def __init__(self,varl):
        self.varl = varl

@pytest.fixture(scope="module")
def f_req_module(request):
    varl1 = getattr(request.module, "varl" , 100)
    f_req_module = ccc(varl1)
    yield f_req_module
    print("finalizing %s (%s)" % (f_req_module.varl, varl1))
    print("teardown ccc")

def ddd(p1,p2=2,p3=3):
    return p1+p2+p3

@pytest.fixture(scope="module")
def f_req_module2(request):
    pp1 = getattrd(request.module,"p1",5)
    f_req_module2 = ddd(pp1,2,3)
    yield f_req_module2
    print("finalizing %s (%s)" % (f_req_module2, pp1))
    print("teardown ddd")

@pytest.fixture(scope="module",
                params=["smtp.qq.com","mail.python.org"])
def smtp_connection(request):
    import smtplib
    smtp_connection = smtplib.SMTP(request.param, 587 ,timeout = 10)
    yield smtp_connection
    print("finalizing %s" % smtp_connection)
    smtp_connection.close()

import tempfile
import os

@pytest.fixture
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)

@pytest.fixture
def usename():
    return 'username'

@pytest.fixture
def other_username(username):
    return 'other-' + username