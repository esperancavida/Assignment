"""A famous interview question! Print 1 to 15. If a number divides by 3,
print Fizz. By 5, print Buzz. By both, print FizzBuzz. Otherwise print the
number."""
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

# Your job:
# 1. go up to 50
# 2. count how many times Fizz was printed
fizz_count = 0
for n in range(1, 51):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

print(f"Number of times Fizz was printed: {fizz_count}")