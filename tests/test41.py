import string
lijst_50 = [i for i in range(50)]
print("Lijst 0-49:", lijst_50)
kwadraten = [i**2 for i in range(1, 51)]
print("Kwadraten:", kwadraten)
alfabet = string.ascii_lowercase
letter_lijst = [letter * (i + 1) for i, letter in enumerate(alfabet)]
print("Letter lijst:", letter_lijst)