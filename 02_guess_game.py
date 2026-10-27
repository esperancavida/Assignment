""" Keep a secret number. The user keeps guessing until they get it right.
Say Too low or Too high to help them. Count the tries."""
# Your job:
# 1. give only 3 tries (hint: while tries < 3)
# 2. bonus: import random
#    secret = random.randint(1, 10)
import random
secret = random.randint(1, 10)
# secret = 7
tries = 0

while tries < 3:
    guess = int(input("Guess (1 to 10): "))
    tries += 1

    if guess == secret:
        print(f"Correct! You took {tries} tries")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
    print("Better luck next time!")
else:
    print(f"Sorry, the secret number was {secret}.")