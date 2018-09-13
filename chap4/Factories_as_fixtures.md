The “factory as fixture” pattern can help in situations where the result of a fixture is needed multiple times in a single test. Instead of returning data directly, the fixture instead returns a function which generates the data. This function can then be called multiple times in the test.

If the data created by the factory requires managing, the fixture can take care of that:

```
@pytest.fixture
def make_customer_record():
    created_records = []
    def _make_customer_record(name):
        record = models.Customer(name=name, orders=[])
        created_records.append(record)
        return record
    yield _make_customer_record
    for record in created_records:
        record.destroy()
def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    
 ```