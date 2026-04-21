def longest_words():
    filename = input("")
    try:
        with open(filename, 'r') as f:
            words = f.read().split()
            if not words:
                return

            max_len = len(max(words, key=len))
            longest = [word for word in words if len(word) == max_len]
            unique_longest = sorted(set(longest))

            print(f"Length of longest word(s) is [{max_len}] chars")
            print("These are all the words of that length:")
            print(", ".join(unique_longest))
    except FileNotFoundError:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    longest_words()