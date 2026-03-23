special_characters = [",",".","?","!",";",":","[","]","(",")"]
user_input = input("").lower()

def removeSpecialCharacters(inputword:str) -> str:
    word = ""
    for letter in inputword:
        if letter not in special_characters:
            word += letter
    return word

def reverseWord(word:str) -> str:
    original_word = word
    reversed_word = ""
    for letter in reversed(original_word):
        reversed_word += letter
    return reversed_word

word = removeSpecialCharacters(user_input)
if word == reverseWord(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome!")