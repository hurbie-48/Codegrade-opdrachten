def get_months_and_days(years: int) -> str:
    months = years*12
    days = years*365
    return f"Months: {months}, Days: {days}"

def execute_slice(user_input: str) -> int:
    return int(user_input[slice(7, 8)])

while True:
    print("Enter a year like this: Years: 3.")
    try:
        number = execute_slice(input())
    except ValueError:
        print("Please enter a valid number!")
        continue
    print(get_months_and_days(number))
    break
