"""Ask the user for a sentence. Loop over every letter and count how many 
vowels (a, e, i, o, u) it has. Use .lower() so capital letters count too."""
# Type a sentence: I love Nepal
# Vowels: 5

# Your job:
# 1. also count the spaces
# 2. print the sentence backwards with a loop
#    (hint: start with back = "", then back = letter + back)

text = input("Type a sentence: ").lower()
vowels = 0
back = ""
for letter in text:
    if letter in "aeiou":
        vowels += 1
    back = letter + back
print(f"Total characters: {len(text)}")
print(f"Vowels: {vowels}")
print(f"Sentence backwards: {back}")