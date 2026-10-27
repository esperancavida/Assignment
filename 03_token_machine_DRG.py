"""The generator never ends (while True), but it only makes a new token when 
next() asks. A while loop (Day 08) keeps asking until the user types q."""
# === Bank Token Machine ===
# Press Enter for a token (q to quit):
# Your token: A-1
# Press Enter for a token (q to quit):
# Your token: A-2
# Press Enter for a token (q to quit): q
# Bye!

# Your job:
# 1. make a second machine for VIP customers: "V"
#    ask "normal or vip?" and use the right one
# 2. write a generator countdown(n) that yields
#    n down to 1, and print: Next in 3 2 1
def token_machine(prefix):
    n = 1
    while True:
        yield f"{prefix}-{n}"
        n += 1
def countdown(n):
    while n > 0:
        yield n
        n -= 1
normal_tokens = token_machine("A")
vip_tokens = token_machine("V")

print("=== Bank Token Machine ===")
while True:
    choice = input("\nChoose (n)ormal token, (v)ip token, or (q)uit: ").strip().lower()
    if choice == "q":
        print("Bye!")
        break
    if choice == "n":
        current_token = next(normal_tokens)
    elif choice == "v":
        current_token = next(vip_tokens)
    else:
        print("Invalid option. Please choose n, v, or q.")
        continue
    print("Next in:", end=" ")
    for num in countdown(3):
        print(num, end=" ")
    print()
    
    print("Your token:", current_token)

