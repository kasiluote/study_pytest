import os.path
def getssh():
    return os.path.join(os.path.expanduser("~admin"), '.ssh')

def test_mytest(monkeypatch):
    def mockreturn(testpath):
        return "a:\\testabc"
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    x = getssh()
    print(x)
    assert x == 'a:\\testabc\\.ssh'
    assert 0