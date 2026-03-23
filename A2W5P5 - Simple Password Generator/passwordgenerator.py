import random


def generate_random_password() -> str:
    length = random.randint(7, 10)
    password = ""
    for character in range(length):
        random_char = chr(random.randint(33, 126))
        password += random_char
    return password


if __name__ == "__main__":
    print(generate_random_password())