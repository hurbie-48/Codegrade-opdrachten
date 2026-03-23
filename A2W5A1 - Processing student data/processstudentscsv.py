import csv
import re


def validate_data(row):
    errors = []

    student_number = str(row.get('studentnumber', '')).strip()
    is_valid_sn = (
        len(student_number) == 7 and
        student_number.startswith('0') and
        student_number[1] in ('8', '9') and
        student_number.isdigit()
    )
    if not is_valid_sn:
        errors.append(student_number)

    first_name = str(row.get('firstname', '')).strip()
    if not (first_name and first_name.isalpha()):
        errors.append(first_name)

    last_name = str(row.get('lastname', '')).strip()
    if not (last_name and last_name.replace(" ", "").isalpha()):
        errors.append(last_name)

    dob = str(row.get('dateofbirth', '')).strip()
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', dob)
    if not match:
        errors.append(dob)
    else:
        y, m, d = map(int, match.groups())
        if not (1960 <= y <= 2004 and 1 <= m <= 12 and 1 <= d <= 31):
            errors.append(dob)

    prog = str(row.get('studyprogram', '')).strip()
    if prog not in ['INF', 'TINF', 'CMD', 'AI']:
        errors.append(prog)

    return errors


def process_students(file_name):
    correct = []
    corrupted = []

    try:
        with open(file_name, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                validation_errors = validate_data(row)
                line_str = ",".join(row.values())

                if not validation_errors:
                    correct.append(line_str)
                else:
                    msg = f"{line_str} => INVALID DATA: {validation_errors}"
                    corrupted.append(msg)
    except FileNotFoundError:
        pass

    return correct, corrupted


if __name__ == "__main__":
    correct_lines, corrupt_lines = process_students('students.csv')

    print("### VALID LINES ###")
    for line in correct_lines:
        print(line)

    print("\n### CORRUPT LINES ###")
    for line in corrupt_lines:
        print(line)