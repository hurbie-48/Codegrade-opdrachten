t = input("Geef me een woord/tekst: ").lower()
print(f'"{t}" is {"" if t == t[::-1] else "not "}a palindrome')


