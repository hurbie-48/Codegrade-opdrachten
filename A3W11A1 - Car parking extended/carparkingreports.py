import os
import csv
import json
from datetime import datetime

DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"
DATE_FORMAT = "%d-%m-%Y"


def parse_comma_input(prompt_text):
    user_input = input(prompt_text)
    return [item.strip() for item in user_input.split(',')]


def get_log_lines():
    log_path = 'carparklog.txt'
    if not os.path.exists(log_path):
        return []
    with open(log_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def format_fee(val):
    try:
        f_val = float(val)
        return f"{f_val:g}"
    except (ValueError, TypeError):
        return "0"


def generate_parked_cars_report():
    try:
        inputs = parse_comma_input("Enter machine ID, from date, to date: ")
        if len(inputs) < 3:
            print("Invalid inputs.")
            return

        machine_id, from_date_str, to_date_str = inputs[0], inputs[1], inputs[2]
        from_date = datetime.strptime(from_date_str, DATE_FORMAT)
        to_date = datetime.strptime(to_date_str, DATE_FORMAT).replace(hour=23, minute=59, second=59)
    except ValueError:
        print("Incorrect date formatting pattern.")
        return

    log_lines = get_log_lines()
    all_events = []

    for line in log_lines:
        parts = line.split(';')
        if len(parts) < 4:
            continue
        try:
            timestamp = datetime.strptime(parts[0], DATETIME_FORMAT)
        except ValueError:
            continue

        cpm_name = parts[1].split('=')[1]
        license_plate = parts[2].split('=')[1]
        action = parts[3].split('=')[1]

        if cpm_name.lower() != machine_id.lower():
            continue

        all_events.append({
            'time': timestamp,
            'time_str': parts[0],
            'plate': license_plate,
            'action': action,
            'parts': parts
        })

    all_events.sort(key=lambda e: e['time'])

    checked_in_cars = {}
    report_rows = []

    for ev in all_events:
        plate = ev['plate']
        if ev['action'] == 'check-in':
            checked_in_cars[plate] = ev
        elif ev['action'] == 'check-out':
            in_ev = checked_in_cars.pop(plate, None)
            in_time_str = in_ev['time_str'] if in_ev else "None"
            fee_str = format_fee(ev['parts'][4].split('=')[1])

            if from_date <= ev['time'] <= to_date:
                try:
                    sort_time = datetime.strptime(in_time_str, DATETIME_FORMAT) if in_time_str != "None" else ev['time']
                except ValueError:
                    sort_time = ev['time']
                report_rows.append({
                    'sort_key': sort_time,
                    'data': [plate, in_time_str, ev['time_str'], fee_str]
                })

    state_file = f"{machine_id}_state.json"
    if os.path.exists(state_file):
        try:
            with open(state_file, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    for item in data:
                        plate = item["license_plate"]
                        in_time_str = item["check_in"]
                        try:
                            in_time = datetime.strptime(in_time_str, DATETIME_FORMAT)
                        except ValueError:
                            continue

                        if from_date <= in_time <= to_date:
                            if not any(r['data'][0] == plate and r['data'][2] == "None" for r in report_rows):
                                report_rows.append({
                                    'sort_key': in_time,
                                    'data': [plate, in_time_str, "None", "0"]
                                })
        except Exception:
            pass

    report_rows.sort(key=lambda x: x['sort_key'])
    final_output = [row['data'] for row in report_rows]

    filename = f"parkedcars_{machine_id}_from_{from_date_str}_to_{to_date_str}.csv"

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['license_plate', 'checked_in', 'checked_out', 'parking_fee'])
        writer.writerows(final_output)

    print(f"Report compiled successfully: {filename}")


def generate_total_fee_report():
    try:
        inputs = parse_comma_input("Enter from date, to date: ")
        if len(inputs) < 2:
            print("Invalid inputs.")
            return

        from_date_str, to_date_str = inputs[0], inputs[1]
        from_date = datetime.strptime(from_date_str, DATE_FORMAT)
        to_date = datetime.strptime(to_date_str, DATE_FORMAT).replace(hour=23, minute=59, second=59)
    except ValueError:
        print("Incorrect date formatting pattern.")
        return

    log_lines = get_log_lines()
    fees_by_machine = {}

    for line in log_lines:
        parts = line.split(';')
        if len(parts) < 5 or 'action=check-out' not in line:
            continue
        try:
            timestamp = datetime.strptime(parts[0], DATETIME_FORMAT)
        except ValueError:
            continue

        cpm_name = parts[1].split('=')[1]
        fee = float(parts[4].split('=')[1])

        if from_date <= timestamp <= to_date:
            fees_by_machine[cpm_name] = fees_by_machine.get(cpm_name, 0.0) + fee

    filename = f"totalfee_from_{from_date_str}_to_{to_date_str}.csv"

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['car_parking_machine', 'total_parking_fee'])
        for machine, total in fees_by_machine.items():
            writer.writerow([machine,
                             f"{total:,.0f}".replace(",", ".") if total.is_integer() else f"{total:,.2f}".replace(",",
                                                                                                                  ".")])

    print(f"Report compiled successfully: {filename}")


def main():
    while True:
        print("\n--- Car Parking Reporting System ---")
        print("[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print("[Q] Quit program")

        choice = input("Select an option: ").upper()

        if choice == 'P':
            generate_parked_cars_report()
        elif choice == 'F':
            generate_total_fee_report()
        elif choice == 'Q':
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()