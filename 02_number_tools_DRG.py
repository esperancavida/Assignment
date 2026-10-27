"""Three small recursive functions, each with a base case and a smaller step.
n % 10 gives the last digit and n // 10 removes it (Day 03). Fibonacci: each 
number is the sum of the two before it."""
# 5! = 120
# Digits of 4567 add to 22
# Fibonacci: 0 1 1 2 3 5 8 13

# Your job:
# 1. ask the user for a number with int(input())
# 2. write power(base, n) with recursion
# 3. write count_vowels(word) with recursion
#    (hint: word[0] in "aeiou", then word[1:])
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def power(base, n):
    if n == 0:
        return 1
    return base * power(base, n - 1)
def count_vowels(word):
    if not word:
        return 0
    is_vowel = 1 if word[0].lower() in "aeiou" else 0
    return is_vowel + count_vowels(word[1:])

print("5! =", factorial(5))
print("Digits of 4567 add to", sum_digits(4567))

print("Fibonacci:", end=" ")
for i in range(8):
    print(fibonacci(i), end=" ")
print("\n")
user_num = int(input("Enter a positive integer for testing: "))

print(f"Factorial of {user_num}: {factorial(user_num)}")
print(f"Sum of digits of {user_num}: {sum_digits(user_num)}")
print(f"2 raised to the power of {user_num}: {power(2, user_num)}")

test_word = input("Enter a word to count vowels: ")
print(f"Number of vowels in '{test_word}': {count_vowels(test_word)}")


