import string


def analyze_word_frequency():
    filename = input("")
    try:
        with open(filename, 'r') as f:
            counts = {}
            for line in f:
                for word in line.split():
                    clean_word = word.strip(string.punctuation).lower()
                    if clean_word:
                        counts[clean_word] = counts.get(clean_word, 0) + 1

            if not counts:
                return

            frequencies = counts.values()
            max_freq = max(frequencies)
            min_freq = min(frequencies)

            most_frequent = [w for w, count in counts.items() if count == max_freq]
            least_frequent = [w for w, count in counts.items() if count == min_freq]

            print(f"Most: {sorted(most_frequent)}")
            print(f"Least: {sorted(least_frequent)}")

    except FileNotFoundError:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    analyze_word_frequency()