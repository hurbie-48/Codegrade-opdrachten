import sys

# Global storage for the program
HISTORY = []
CURRENT_KEY_DICT = {}

def set_dict_key(conversion_string: str) -> dict:
    """Converts a string into a key-value dictionary for substitution."""
    if len(conversion_string) % 2 != 0:
        print("Error: Invalid hash value input")
        return {}
    
    # Creates dict: even indices are keys, odd indices are values
    return {conversion_string[i]: conversion_string[i+1] 
            for i in range(0, len(conversion_string), 2)}

def encode_string(data: str, key_dict: dict = None) -> str:
    """Encodes a string using the key_dict. Returns char if not in key."""
    if not key_dict:
        return data
    return "".join([key_dict.get(char, char) for char in data])

def decode_string(data: str, key_dict: dict = None) -> str:
    """Decodes a string by reversing the key_dict mapping."""
    if not key_dict:
        return data
    # Reverse the dictionary to map value -> key
    reverse_key = {v: k for k, v in key_dict.items()}
    return "".join([reverse_key.get(char, char) for char in data])

def encode_list(data_list: list, key_dict: dict = None) -> list:
    """Uses map and lambda to encode a list of strings."""
    return list(map(lambda x: encode_string(x, key_dict), data_list))

def decode_list(data_list: list, key_dict: dict = None) -> list:
    """Uses map and lambda to decode a list of strings."""
    return list(map(lambda x: decode_string(x, key_dict), data_list))

def validate_values(encoded: str, decoded: str, key_dict: dict = None) -> bool:
    """Checks if the decoded version of the encoded string matches the input."""
    return encode_string(decoded, key_dict) == encoded

def main():
    # Using the provided default key string
    default_key_str = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"
    global CURRENT_KEY_DICT
    CURRENT_KEY_DICT = set_dict_key(default_key_str)
    
    while True:
        print("\n--- Hash Menu ---")
        print("[E] Encode | [D] Decode | [P] Print All | [V] Validate | [Q] Quit")
        choice = input("Select an option: ").strip().upper()

        if choice == 'E':
            val = input("Enter value to encode: ")
            encoded = encode_string(val, CURRENT_KEY_DICT)
            HISTORY.append({"original": val, "encoded": encoded})
            print(f"Encoded: {encoded}")

        elif choice == 'D':
            val = input("Enter hash to decode: ")
            decoded = decode_string(val, CURRENT_KEY_DICT)
            HISTORY.append({"original": decoded, "encoded": val})
            print(f"Decoded: {decoded}")

        elif choice == 'P':
            print("\nHistory (Decoded | Encoded):")
            for item in HISTORY:
                print(f"{item['original']} | {item['encoded']}")

        elif choice == 'V':
            enc = input("Enter encoded value: ")
            dec = input("Enter decoded value: ")
            is_valid = validate_values(enc, dec, CURRENT_KEY_DICT)
            print(f"Match: {is_valid}")

        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()