"""Each sign in the dictionary points to a lambda. operations[sign] picks the
lambda, and (a, b) calls it. A while loop (Day 08) keeps asking until the user
types q. split() and if checks (Day 07) handle bad input."""
# > 8 + 2
# = 10.0
# > 9 / 0
# = Can't divide by 0
# > 5 % 2
# Unknown sign: %
# > q
# Bye!

# Your job:
# 1. add "%" for the remainder (Day 03)
# 2. what happens if you type: abc + 2 ?
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Can't divide by 0",
    "**": lambda a, b: a ** b,
    "%": lambda a, b: a % b if b != 0 else "Can't divide by 0",
}

print("Type like: 8 + 2   (or q to quit)")
while True:
    text = input("> ").strip()
    if text.lower() == "q":
        print("Bye!")
        break
    parts = text.split()
    if len(parts) != 3:
        print("Please type: number sign number")
        continue
    a, sign, b = parts
    if sign not in operations:
        print(f"Unknown sign: {sign}")
        continue
    result = operations[sign](float(a), float(b))
    print("=", result)

