import pytest

#original parameter of App.__init__() is smtp_connection
#I confused with the argument's name
#Which smtp_connection uses conftest.py:pytest.fixture:smtp_connection
#So I modify argument name with a 1 tailing.
#Now it's clear that this is a feature about one pytest.fixture using another pytest.fixture.
#And also, Use a class to receive the test argument as a delegator here.

class App():
    def __init__(self,smtp_connection1):
        self.smtp_connection1 = smtp_connection1

@pytest.fixture(scope="module")
def app(smtp_connection):
    return App(smtp_connection)

def test_smtp_connection_exists(app):
    assert app.smtp_connection1