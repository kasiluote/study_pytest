import pytest

@pytest.mark.test_id(1501)
def test_function():
    assert True

def test_function1(record_xml_attribute):
    record_xml_attribute("assertions", "REQ-1234")
    record_xml_attribute("classname", "custom_classname")
    print("hello world")
    assert True
