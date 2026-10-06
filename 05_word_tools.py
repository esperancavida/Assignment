"""Turn the Day 08 vowel counter into a function. Then write is_palindrome(): 
a word that reads the same backwards. [::-1] from Day 03 flips a string."""
# Your job:
# 1. write count_spaces(text)
# 2. write first_letters(text): "I love Nepal" gives "ILN"
#    (hint: .split() from Day 04)
def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
def count_spaces(text):
    return text.count(" ")
def first_letters(text):
    words = text.split()
    letters = ""
    for word in words:
        if word:  # Ensures the word isn't an empty string
            letters += word[0].upper()
    return letters

print(count_vowels("I love Nepal"))   # 5
print(count_spaces("I love Nepal"))   # 2
print(first_letters("I love Nepal"))  # ILN
print(first_letters("automated teller machine"))#ATM
print(is_palindrome("Madam"))         # True
print(is_palindrome("Nepal"))         # False
