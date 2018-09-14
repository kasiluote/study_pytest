import os
import pytest

# with pytestmark , no decorator usefixtures
# Note that the assigned variable must be called pytestmark,
# pytestmark = pytest.mark.usefixtures("cleandir")

#It is also possible to put fixtures required by all tests in your project into an ini-file:


# @pytest.mark.usefixtures("cleandir")
class TestDirectoryInit():
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile","w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []

'''
    There are three ways to use pytest.fixture and test functions don't directly need access to a fixture object.:
        1. with @pytest.mark.usefixtures("fixture_name")
        2. Assign to a variable whose name must be "pytestmark":
           pytestmark = pytest.mark.usefixtures("cleandir")
        3. In pytest.ini ,add information like this:
            [pytest]
            usefixtures = cleandir
'''