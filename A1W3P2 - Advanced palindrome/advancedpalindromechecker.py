word = input("Sentence: ")
wordlist = []

for letter in word:
    if letter != " ":
        wordlist.append(letter)

reverselist = wordlist[::-1]

if wordlist == reverselist:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")