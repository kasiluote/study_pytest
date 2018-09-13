
def test_ayield1(f_req_module):
    assert f_req_module.varl == 100

p1 = 10 # manually set function ddd's first parameter's value to 10
        #this will cause test_ayield2 failed and print ddd ccc teardowns.
def test_ayield2(f_req_module2):
    assert f_req_module2 == 10
#page 32 Factories as fixtures