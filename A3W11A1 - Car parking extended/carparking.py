import os
import json
import math
from datetime import datetime

DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"
DATE_FORMAT = "%d-%m-%Y"


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        if isinstance(check_in, str):
            try:
                self.check_in = datetime.strptime(check_in, DATETIME_FORMAT)
            except ValueError:
                self.check_in = datetime.strptime(check_in, "%m-%d-%Y %H:%M:%S")
        else:
            self.check_in = check_in

    def to_dict(self):
        return {
            "license_plate": self.license_plate,
            "check_in": self.check_in.strftime(DATETIME_FORMAT)
        }


class CarParkingMachine:
    _all_machine_ids = []

    def __init__(self, id=None, capacity=10, hourly_rate=2.50):
        self.id = str(id) if id is not None else ""
        self.capacity = capacity
        self.hourly_rate = float(hourly_rate)
        self.parked_cars = {}
        self.logger = CarParkingLogger(self.id)

        self.json_file = f"{self.id}_state.json" if self.id else "state.json"

        if self.id and self.id not in CarParkingMachine._all_machine_ids:
            CarParkingMachine._all_machine_ids.append(self.id)

        self._load_from_json()

    def _load_from_json(self):
        if not os.path.exists(self.json_file):
            return
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    for item in data:
                        plate = item["license_plate"]
                        self.parked_cars[plate] = ParkedCar(plate, item["check_in"])
        except (json.JSONDecodeError, KeyError, IndexError):
            self.parked_cars = {}

    def _save_to_json(self):
        with open(self.json_file, 'w') as file:
            serialized_data = [car.to_dict() for car in self.parked_cars.values()]
            json.dump(serialized_data, file, indent=4)

    def _is_car_parked_anywhere(self, license_plate):
        for machine_id in CarParkingMachine._all_machine_ids:
            target_path = f"{machine_id}_state.json"
            if os.path.exists(target_path):
                try:
                    with open(target_path, 'r') as file:
                        data = json.load(file)
                        if isinstance(data, list):
                            for item in data:
                                if item.get("license_plate") == license_plate:
                                    return True
                except (json.JSONDecodeError, KeyError):
                    continue
        return False

    def check_in(self, license_plate, check_in=None):
        if check_in is None:
            check_in = datetime.now()

        if len(self.parked_cars) >= self.capacity:
            return False

        if self._is_car_parked_anywhere(license_plate):
            return False

        new_car = ParkedCar(license_plate, check_in)
        self.parked_cars[license_plate] = new_car

        self._save_to_json()
        self.logger.log_check_in(license_plate, check_in)
        return True

    def get_parking_fee(self, license_plate, check_out=None):
        if license_plate not in self.parked_cars:
            return 0.0

        if check_out is None:
            check_out = datetime.now()

        car = self.parked_cars[license_plate]
        duration = check_out - car.check_in
        duration_hours = duration.total_seconds() / 3600

        billable_hours = math.ceil(duration_hours)
        if billable_hours < 0:
            billable_hours = 0

        parking_hours = min(billable_hours, 24)
        return float(parking_hours * self.hourly_rate)

    def check_out(self, license_plate, check_out=None):
        if license_plate not in self.parked_cars:
            return None

        if check_out is None:
            check_out = datetime.now()

        fee = self.get_parking_fee(license_plate, check_out)
        self.logger.log_check_out(license_plate, check_out, fee)

        del self.parked_cars[license_plate]
        self._save_to_json()
        return fee


class CarParkingLogger:
    def __init__(self, id):
        self.id = str(id)
        self.log_file = 'carparklog.txt'

    def log_check_in(self, license_plate, check_in_time):
        time_str = check_in_time.strftime(DATETIME_FORMAT)
        log_line = f"{time_str};cpm_name={self.id};license_plate={license_plate};action=check-in\n"
        with open(self.log_file, 'a') as file:
            file.write(log_line)

    def log_check_out(self, license_plate, check_out_time, fee):
        time_str = check_out_time.strftime(DATETIME_FORMAT)
        fee_str = f"{fee:g}"
        log_line = f"{time_str};cpm_name={self.id};license_plate={license_plate};action=check-out;parking_fee={fee_str}\n"
        with open(self.log_file, 'a') as file:
            file.write(log_line)

    def get_machine_fee_by_day(self, car_parking_machine_id, search_date):
        total_fee = 0.0
        if not os.path.exists(self.log_file):
            return round(total_fee, 2)

        with open(self.log_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or 'action=check-out' not in line:
                    continue

                parts = line.split(';')
                log_date = parts[0].split()[0]
                cpm_name = parts[1].split('=')[1]

                if log_date == search_date and cpm_name.lower() == car_parking_machine_id.lower():
                    fee_val = float(parts[4].split('=')[1])
                    total_fee += fee_val

        return round(total_fee, 2)

    def get_total_car_fee(self, license_plate):
        total_fee = 0.0
        if not os.path.exists(self.log_file):
            return round(total_fee, 2)

        with open(self.log_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or 'action=check-out' not in line:
                    continue

                parts = line.split(';')
                log_plate = parts[2].split('=')[1]

                if log_plate.lower() == license_plate.lower():
                    fee_val = float(parts[4].split('=')[1])
                    total_fee += fee_val

        return round(total_fee, 2)


def main():
    machine = CarParkingMachine(id="North", capacity=10, hourly_rate=2.0)

    while True:
        print(f"\n--- Machine {machine.id} Menu ---")
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")

        choice = input("Select an option: ").upper()

        if choice == 'I':
            license_plate = input("License: ")
            if machine.check_in(license_plate):
                print("License registered")
            else:
                print("Capacity reached or car already parked!")

        elif choice == 'O':
            license_plate = input("License: ")
            fee = machine.check_out(license_plate)
            if fee is not None:
                print(f"Parking fee: {fee:.2f} EUR")
            else:
                print(f"License {license_plate} not found!")

        elif choice == 'S':
            date_str = input("Enter date (DD-MM-YYYY): ")
            total = machine.logger.get_machine_fee_by_day(machine.id, date_str)
            print(f"Total fee collected by {machine.id} on {date_str}: {total:.2f} EUR")

        elif choice == 'T':
            license_plate = input("License: ")
            total = machine.logger.get_total_car_fee(license_plate)
            print(f"Total historical fee for {license_plate}: {total:.2f} EUR")

        elif choice == 'Q':
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()