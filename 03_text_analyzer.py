"""Write small functions (Day 09) that use built-ins inside: len(), set(), 
sorted() and max() with key=len. Then print a short report about any sentence."""
# Type a sentence: I love momo and I love tea
# Letters: 26
# Words: 7
# Longest word: love
# 1. and
# 2. i
# 3. love
# 4. momo
# 5. tea

# Your job:
# 1. write shortest_word(text) with min()
# 2. count how many times each word appears
#    with a dictionary (Day 06 + Day 08)
def word_count(text):
    return len(text.split())

def longest_word(text):
    return max(text.split(), key=len)

def unique_words(text):
    return sorted(set(text.lower().split()))

def shortest_word(text):
    if not text.split():
        return None  # Return None if the text is empty or has no words
    return min(text.split(), key=len)
def word_appeared(text):
    word_count_dict = {}
    for word in text.lower().split():
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict
sentence = input("Type a sentence: ")

print(f"Letters: {len(sentence)}")
print(f"Words: {word_count(sentence)}")
print(f"Longest word: {longest_word(sentence)}")
print(f"Shortest word: {shortest_word(sentence)}")
print("Word appearances:")
word_appearances = word_appeared(sentence)
for word, count in word_appearances.items():
    print(f"{word}: {count}")
print("Unique words:")
for num, word in enumerate(unique_words(sentence), start=1):
    print(f"{num}. {word}")