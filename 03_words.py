"""Ask for two sentences. Split each one into a set of words,
then print the common words, all the unique words, and how many
of each. Store the two counts in a tuple and unpack them to 
print."""
s1 = input("Sentence 1: ").lower()
s2 = input("Sentence 2: ").lower()

words1 = set(s1.split())
words2 = set(s2.split())

common = words1 & words2
print("Common words:", sorted(common))