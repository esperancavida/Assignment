"""Build your own mini print(): any number of words with *words, then sep and 
end that must be sent by name, just like the real print() from Day 10."""
# Your job:
# 1. add times=1, and print the line that many times
# 2. what happens with shout(5, 10)? Fix it with str()
def shout(*words, sep=" ", end="!", times=1):
    str_words = [str(w) for w in words]
    text = sep.join(str_words)
    final_output=text.upper()+end
    for _ in range(times):
        print(final_output)

shout("hello", "class")                 # HELLO CLASS!
shout("python", "is", "fun", sep="-")   # PYTHON-IS-FUN!
shout("namaste", end="!!!")             # NAMASTE!!!

words = ["we", "love", "momo"]
shout(*words)                           # WE LOVE MOMO!
print("\n--- Printing multiple times ---")
shout("flash", "sale", sep=" ", end="!!", times=3)

print("\n--- Passing numbers (shout(5, 10)) ---")
shout(5, 10)

