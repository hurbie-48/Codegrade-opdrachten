from datetime import datetime, timedelta

from carparking import CarParkingMachine


def test_check_in_capacity_normal():
    machine = CarParkingMachine(capacity=2)
    assert machine.check_in("AA-123-B") is True
    assert len(machine.parked_cars) == 1


def test_check_in_capacity_reached():
    machine = CarParkingMachine(capacity=1)
    machine.check_in("AA-123-B")

    assert machine.check_in("BB-456-C") is False
    assert len(machine.parked_cars) == 1


def test_parking_fee():
    machine = CarParkingMachine(capacity=10, hourly_rate=2.50)

    time_2h10m_ago = datetime.now() - timedelta(hours=2, minutes=10)
    machine.check_in("FEE-1", check_in=time_2h10m_ago)
    assert machine.get_parking_fee("FEE-1") == 7.50

    time_24h_ago = datetime.now() - timedelta(hours=24)
    machine.check_in("FEE-2", check_in=time_24h_ago)
    assert machine.get_parking_fee("FEE-2") == 60.00

    time_30h_ago = datetime.now() - timedelta(hours=30)
    machine.check_in("FEE-3", check_in=time_30h_ago)
    assert machine.get_parking_fee("FEE-3") == 60.00


def test_check_out():
    machine = CarParkingMachine(hourly_rate=2.50)
    check_in_time = datetime.now() - timedelta(hours=2, minutes=1)
    license_plate = "GHI789"

    machine.check_in(license_plate, check_in=check_in_time)

    assert license_plate in machine.parked_cars

    fee = machine.check_out(license_plate)
    assert fee == 7.50

