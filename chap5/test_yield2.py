def test_yield1(f_yield1):
    res = f_yield1(1)
    assert res == 10087

def test_yield2(f_yield2):
    assert f_yield2.varl == 15

def test_yield3(f_yield3):
    assert f_yield3 == 123

def test_req1(f_req1):
    with f_req1 as f:
        assert f == 123
        assert 0 #check teardowns

