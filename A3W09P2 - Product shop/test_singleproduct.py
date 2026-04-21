from singleproduct import Product

def test_normal_amount_get_price():
    item = Product("Gadget", 120, 20.0)
    assert item.get_price(5) == 100.0

def test_discount_10_percent_get_price():
    item = Product("Gadget", 120, 20.0)
    assert item.get_price(15) == 270.0

def test_discount_20_percent_get_price():
    item = Product("Gadget", 120, 20.0)
    assert item.get_price(150) == 2400.0

def test_normal_amount_make_purchase():
    item = Product("Gadget", 120, 20.0)
    item.make_purchase(10)
    assert item.amount == 110