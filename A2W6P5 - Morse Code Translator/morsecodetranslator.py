morse_code = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",  "0": "-----", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--.."
}


def message_to_morse(user_input: str) -> str:
    morse = morse_code
    user_input = user_input.upper()
    morse_result = ""
    for char in user_input:
        if char == " ":
            morse_result += "   "
        elif char in morse:
            morse_result += morse[char] + " "
        else:
            return f"Can't convert char [{char}]"
    return morse_result.strip()


def morse_to_message(user_input: str) -> str:
    morse = morse_code
    reverse_morse = {}
    for key, value in morse.items():
        reverse_morse[value] = key
    words = user_input.split("    ")
    decoded_message = []
    for word in words:
        decoded_word = ""
        chars = word.split()
        for char in chars:
            if char in reverse_morse:
                decoded_word += reverse_morse[char]
            else:
                return f"Can't convert char [{char}]"
        decoded_message.append(decoded_word)
    return " ".join(decoded_message)


def translate_text(user_input: str) -> str:
    is_morse = True
    for char in user_input:
        if char not in ".- ":
            is_morse = False
            break
    if is_morse:
        return morse_to_message(user_input)
    else:
        return message_to_morse(user_input)


if __name__ == "__main__":
    user_text = input("")
    print(translate_text(user_text))