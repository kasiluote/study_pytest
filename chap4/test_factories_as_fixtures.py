import pytest

class Customer():
    def __init__(self,name,orders):
        self.name = name
        self.orders = orders

    def check_hash(self):
        return hash(self.name)

@pytest.fixture
def make_customer_record():

    created_records = []

    def _make_customer_record(name):
        record = Customer(name=name, orders=None)
        created_records.append(record)
        record.orders = created_records.index(record)
        return record

    yield _make_customer_record

    # for record in created_records:
    #     record.destory()

@pytest.mark.parametrize("name,hash_value",
                         [
                             ("Lisa",hash("Lisa")),
                             ("Mike",hash("Mike")),
                             ("Meredith",hash("Meredith"))
                         ])
def test_customer_records(make_customer_record,name,hash_value):
    customer_x = make_customer_record(name)
    assert customer_x.name == name
    assert customer_x.check_hash() == hash_value
    assert customer_x.orders == 0





