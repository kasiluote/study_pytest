import pytest

class DB():
    def __init__(self):
        self.intransaction = []

    def begin(self,name):
        self.intransaction.append(name)

    def rollback(self):
        self.intransaction.pop()

@pytest.fixture
def db():
    return DB()

class TestClass():

    @pytest.fixture(autouse=True)
    def transact(self,request,db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self,db):
        assert db.intransaction == ["test_method1"]

    def test_method2(self,db):
        assert db.intransaction == ["test_method2"]

#Here is how autouse fixtures work in other scopes:
# autouse fixtures obey the scope= keyword-argument: if an autouse fixture has scope='session'
#   it will # only be run once, no matter where it is defined. scope='class' means it will be run once per class, etc.
# if an autouse fixture is defined in a test module,
#   all its test functions automatically use it.
# if an autouse fixture is defined in a conftest.py file
#   then all tests in all test modules below its directory will invoke the fixture.
# lastly, and please use that with care: if you define an autouse fixture in a plugin, it will be invoked for all tests
# in all projects where the plugin is installed. This can be useful if a fixture only anyway works in the presence
# of certain settings e. g. in the ini-file. Such a global fixture should always quickly determine if it should do any
# wo rk and avoid otherwise expensive imports or computation.