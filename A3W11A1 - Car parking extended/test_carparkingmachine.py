import os
from carparking import CarParkingMachine


def clear_json_states():
    for name in ["north", "south"]:
        path = os.path.join(os.getcwd(), f"{name}_state.json")
        if os.path.exists(path):
            os.remove(path)


def test_check_in_single_parking_machine_only():
    clear_json_states()

    machine_north = CarParkingMachine(id="North", capacity=10)
    machine_south = CarParkingMachine(id="South", capacity=10)

    assert machine_north.check_in("MyTestPlate001") is True
    assert machine_north.check_in("MyTestPlate002") is True

    assert machine_south.check_in("MyTestPlate001") is False


def test_restore_state_json():
    machine_north = CarParkingMachine(id="North", capacity=10)
    machine_south = CarParkingMachine(id="South", capacity=10)

    assert "MyTestPlate001" in machine_north.parked_cars
    assert "MyTestPlate002" in machine_north.parked_cars

    assert machine_north.check_out("MyTestPlate001") is not None
    assert machine_north.check_out("MyTestPlate002") is not None

    assert "MyTestPlate001" not in machine_north.parked_cars
    assert "MyTestPlate002" not in machine_north.parked_cars

    assert machine_south.check_in("MyTestPlate002") is True
    assert machine_north.check_in("MyTestPlate002") is False

    assert machine_south.check_out("MyTestPlate002") is not None