"""int(input()) crashes when the user types words. get_number() keeps asking
until it gets real digits, then returns an int. Use it in every program from
now on!"""
# Your age: twenty
# Please type a number only
# Your age: 20
# Next year you will be 21

# Your job:
# 1. only accept ages from 1 to 120
# 2. use get_number() in the Day 09 calculator
def get_number(question, min_val=1, max_val=120):
    while True:
        answer = input(question).strip()
        if answer.isdigit():
            num = int(answer)
            if min_val is not None and num < min_val:
                print(f"Please type a number from {min_val} to {max_val}")
                continue
            if max_val is not None and num > max_val:
                print(f"Please type a number from {min_val} to {max_val}")
                continue
            return num
        print("Please type a number only")

age = get_number("Your age: ")
print(f"Next year you will be {age + 1}")