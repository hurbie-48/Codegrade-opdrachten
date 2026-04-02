from taxifares import calculate_fare

def test_taxifares():
    assert calculate_fare(66) == 122
    assert calculate_fare(4) == 11.25