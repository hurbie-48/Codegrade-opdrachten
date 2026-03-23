def humanToDogYears(years:int) -> float:
    dogyears = 0
    for i in range(years):
        if i < 2:
            dogyears += 10.5
        else:
            dogyears += 4
    return dogyears

while True:
    user_input = int(input("Human years: "))
    if user_input < 0:
        print("Only positive numbers are allowed")
    else:
        print(f"Human years: {humanToDogYears(user_input)}")
        break