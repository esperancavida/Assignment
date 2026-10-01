"""Ask the user for a number. Tell them if it is positive, negative or zero.
Then use % (from Day 03) to tell if it is even or odd."""
# Your job:
# 1. if num is more than 100, print "Big number"
# 2. if num is from 1 to 10 (use and), print "Small number"
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
if num>100:
    print("Big number")
if num>=1 and num<=10:
    print("Small number")