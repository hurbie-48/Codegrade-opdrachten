import math
from datetime import datetime


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def check_in(self, license_plate, check_in=None):
        if check_in is None:
            check_in = datetime.now()

        if len(self.parked_cars) >= self.capacity:
            return False

        self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
        return True

    def get_parking_fee(self, license_plate):
        if license_plate not in self.parked_cars:
            return None

        car = self.parked_cars[license_plate]
        check_out_time = datetime.now()

        duration = check_out_time - car.check_in
        total_seconds = duration.total_seconds()

        hours = math.ceil(total_seconds / 3600)

        if hours == 0 and total_seconds > 0:
            hours = 1

        if hours > 24:
            hours = 24

        return float(hours * self.hourly_rate)

    def check_out(self, license_plate):
        fee = self.get_parking_fee(license_plate)
        if fee is not None:
            del self.parked_cars[license_plate]
            return fee
        return None


def main():
    machine = CarParkingMachine()

    while True:
        print("\n[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")

        choice = input("Select an option: ").upper()

        if choice == 'I':
            licence_plate = input("License: ")
            success = machine.check_in(licence_plate)
            if success:
                print("License registered")
            else:
                print("Capacity reached!")

        elif choice == 'O':
            licence_plate = input("License: ")
            fee = machine.check_out(licence_plate)
            if fee is not None:
                print(f"Parking fee: {fee:.2f} EUR")
            else:
                print(f"License {licence_plate} not found!")

        elif choice == 'Q':
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()