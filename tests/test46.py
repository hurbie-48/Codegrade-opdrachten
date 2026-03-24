def heeft_letter_a(userinput):
    if "a" in userinput.lower():
        return True
    else:
        return False

user_input = input("Vul wat in: ")

waarde = heeft_letter_a(user_input)
if waarde == True:
    print(f"In {user_input} zit een a")
else:
    print(f"In {user_input} zit GEEN a")