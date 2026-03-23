def is_integer(unchecked: str) -> bool:
    stripped = unchecked.strip()
    if len(stripped) < 1:
        return False

    if stripped[0] in ["+", "-"]:
        if len(stripped) == 1:
            return False
        return all(ch.isdecimal() for ch in stripped[1:])

    return all(ch.isdecimal() for ch in stripped)


def remove_non_integer(unchecked: str) -> int:
    sign = ""
    for character in unchecked:
        if character == "-":
            sign = "-"
            break
        if character == "+":
            sign = "+"
            break

    digits = "".join(ch for ch in unchecked if ch.isdecimal())
    if not digits:
        raise ValueError("No digits found to convert")

    if sign == "-":
        return int(sign + digits)

    return int(digits)


def main() -> None:
    user_input = input("")
    if is_integer(user_input):
        print("Valid integer")
    else:
        print("Invalid integer")


if __name__ == "__main__":
    main()
