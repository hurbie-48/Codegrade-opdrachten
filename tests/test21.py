def hello() -> None:
    print("Hello")

def bye() -> None:
    print("Bye")

user_input = int(input())

if user_input > 10:
    hello()
elif user_input <= 10:
    bye()