from pyeventbus.pyeventbus import subscribe, EBus


def setup_module():
    pass


def teardown_module():
    pass


def test_nomral():
    result = None
    @subscribe('print')
    def listener(data):
        print(data)

    EBus.fire('print', '111')
    print(result)
    assert 1 == 1
