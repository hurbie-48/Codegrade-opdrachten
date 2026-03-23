def checkTriangle(a:int, b:int, c:int) -> str:
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

def getInput(user_input:str) -> list:
    numbers = []
    numbers.append(int(user_input[2]))
    numbers.append(int(user_input[7]))
    numbers.append(int(user_input[12]))
    return numbers

numbers = input("")
numbers = getInput(numbers)
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
print(checkTriangle(a,b,c))