def is_password_valid(password: str) -> bool:
    if len(password) < 8 or len(password) > 20:
        return False
    lower_set = set("abcdefghijklmnopqrstuvwxyz")
    upper_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digit_set = set("0123456789")
    symbol_set = set("*@!?")
    allowed_set = lower_set | upper_set | digit_set | symbol_set
    password_set = set(password)
    if not password_set.issubset(allowed_set):
        return False
    has_lower = False
    if password_set & lower_set:
        has_lower = True
    has_upper = False
    if password_set & upper_set:
        has_upper = True
    has_digit = False
    if password_set & digit_set:
        has_digit = True
    has_symbol = False
    if password_set & symbol_set:
        has_symbol = True
    return has_lower and has_upper and has_digit and has_symbol


if __name__ == "__main__":
    attempts = 0
    while attempts < 3:
        user_input = input("Password: ")
        if is_password_valid(user_input):
            print("Valid")
            break
        else:
            attempts = attempts + 1
            if attempts < 3:
                print("Password is invalid")
            else:
                print("Password is invalid")
                print("Invalid")