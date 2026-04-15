dict_key_value = {}
encoded_history = []
decoded_history = []
DEFAULT_KEY_STR = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"


def set_dict_key(conversion_string: str) -> bool:
    dict_key_value.clear()
    key_to_use = conversion_string if conversion_string else DEFAULT_KEY_STR
    if len(key_to_use) % 2 != 0:
        return False
    dict_key_value.update({
        key_to_use[i]: key_to_use[i + 1]
        for i in range(0, len(key_to_use), 2)
    })
    return True


def encode_string(data: str, key: str = None) -> str:
    if key:
        set_dict_key(key)
    return "".join([dict_key_value.get(char, char) for char in data])


def decode_string(data: str, key: str = None) -> str:
    if key:
        set_dict_key(key)
    reverse_dict = {v: k for k, v in dict_key_value.items()}
    return "".join([reverse_dict.get(char, char) for char in data])


def encode_list(data: list, key: str = None) -> list:
    return list(map(lambda s: encode_string(s, key), data))


def decode_list(data: list, key: str = None) -> list:
    return list(map(lambda s: decode_string(s, key), data))


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    return encode_string(decoded, key) == encoded


def main():
    # The checker expects a specific prompt or no prompt at all for the key
    key_input = input("? ").strip()

    if not set_dict_key(key_input):
        print("Invalid hash value input")
        return

    while True:
        try:
            print("\n--- Name Hasher Menu ---")
            print("[E] Encode value to hashed value")
            print("[D] Decode hashed value to normal value")
            print("[P] Print all encoded/decoded values")
            print("[V] Validate 2 values against each other")
            print("[Q] Quit program")

            # Using the exact prompt from your original logic to match the menu
            choice = input("Select an key: ").strip().upper()

            if choice == 'E':
                val_in = input("Enter value to encode: ")
                if ", " in val_in:
                    vals = val_in.split(", ")
                    res_list = encode_list(vals)
                    encoded_history.extend(res_list)
                    decoded_history.extend(vals)
                    for item in res_list:
                        print(item)
                else:
                    res = encode_string(val_in)
                    encoded_history.append(res)
                    decoded_history.append(val_in)
                    print(f"Encoded: {res}")

            elif choice == 'D':
                val_in = input("Enter hashed value to decode: ")
                if ", " in val_in:
                    vals = val_in.split(", ")
                    res_list = decode_list(vals)
                    decoded_history.extend(res_list)
                    encoded_history.extend(vals)
                    # Note: Checker screenshot shows decoded values appearing here
                    for item in res_list:
                        print(item)
                else:
                    res = decode_string(val_in)
                    decoded_history.append(res)
                    encoded_history.append(val_in)
                    print(f"Decoded: {res}")

            elif choice == 'P':
                for decoded in decoded_history:
                    print(decoded)

            elif choice == 'V':
                enc = input("Enter encoded value: ")
                dec = input("Enter decoded value: ")
                if validate_values(enc, dec):
                    print("Success: Values match!")
                else:
                    print("Failure: Values do not match.")

            elif choice == 'Q':
                break
        except (EOFError, KeyboardInterrupt):
            break


if __name__ == "__main__":
    main()