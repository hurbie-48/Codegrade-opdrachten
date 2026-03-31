def unique_chars_dict(user_input: str) -> int:
    unique_chars = {}
    for character in user_input:
        if character not in unique_chars:
            unique_chars[character] = True
    return len(unique_chars)


def unique_chars_set(user_input: str) -> int:
    unique_chars = set()
    for character in user_input:
        unique_chars.add(character)
    return len(unique_chars)


if __name__ == "__main__":
    user_input = input("")
    print(f"Unique characters: {unique_chars_dict(user_input)}")