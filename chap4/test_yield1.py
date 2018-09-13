import pytest

@pytest.mark.parametrize("para1,res1",
                         [
                             (10,20),
                             (30,40),
                             (50,70),
                             (70,80)
                         ])
def test_y1(func_y,para1,res1):
    with func_y as fy:
        res = fy(para1)
    assert res == res1


def test_funcy2(func_y2):
    res = func_y2.readlines()
    print(res)
    assert 'hello pytest' in res[0]
    assert '\n' in res[0]

