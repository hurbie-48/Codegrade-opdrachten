shapes = {
    3 : "Triangle",
    4 : "Square",
    5 : "Pentagon",
    6 : "Hexagon",
    7 : "Heptagon",
    8 : "Octagon",
    9 : "Nonagon",
    10 : "Decagon"
}

def isValidInput(user_input:str) -> bool:
    try:
        user_input = int(user_input)
        if user_input > 10 or user_input < 3:
            return False
        else:
            return True
    except:
        return False
    
while True:
    try:
        user_input = int(input("Sides: "))
    except:
        print("Amount of sides is out of range")
    if isValidInput(user_input) == False:
        print("Amount of sides is out of range")
    else:
        print(shapes[user_input])
        break
