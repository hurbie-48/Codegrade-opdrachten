def oddOrEven(number:int) -> str:
    if (number%2) == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Number: "))
print(oddOrEven(number))