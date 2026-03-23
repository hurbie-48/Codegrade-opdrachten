def getMonthsAndDays(years: int) -> str:
    months = years*12
    days = years*365
    return(f"Months: {months}, Days: {days}")

def executeSlice(userInput: str) -> int:
    return int(userInput[slice(7, 8)])

while True:
    print("Enter a year like this: Years: 3.")
    try:
        number = executeSlice(input())
    except ValueError:
        print("Please enter a valid number!")
        continue
    print(getMonthsAndDays(number))
    break
