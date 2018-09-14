# Scope: sharing a fixture instance across tests in a class, module or session
def test_func1(func_simple):
    testpath = func_simple.pop()
    assert testpath == "testpath"
    assert 0 # Check the content of func_simple

def test_func2(func_simple):
    testpath = func_simple
    assert "study_pytest" in testpath[0]
    assert 0 # Check the content of func_simple