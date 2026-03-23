def is_input_valid(inp_date):
    """
    Checks if the input follows the YYYY-MM-DD format strictly.
    """
    parts = inp_date.split("-")
    
    # Check if there are exactly 3 parts and lengths are correct (4-2-2)
    if len(parts) != 3 or len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    
    # Check if all parts are numeric
    if not all(part.isdigit() for part in parts):
        return False
        
    return True

def get_next_date():
    user_input = input("Input Date: ")

    if not is_input_valid(user_input):
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
        return

    # Days in each month (Ignoring leap years as requested)
    months_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Split and convert to integers
    year, month, day = map(int, user_input.split("-"))

    # Increment day
    day += 1

    # Check if we exceeded the days in the current month
    if day > months_days[month]:
        day = 1
        month += 1

    # Check if we exceeded the months in the year
    if month > 12:
        month = 1
        year += 1

    # Format output to ensure leading zeros (e.g., 2013-01-01)
    print(f"Next Date: {year:04d}-{month:02d}-{day:02d}")

if __name__ == "__main__":
    get_next_date()