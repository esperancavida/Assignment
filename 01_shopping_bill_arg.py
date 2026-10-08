"""make_bill() takes any number of prices with *prices, and a discount that must
be sent by name. Day 07 if checks for an empty cart. Day 10 built-ins do the maths."""
# Items:     4
# Costliest: Rs. 1200
# Total:     Rs. 1950
# Discount:  Rs. 195.0
# To pay:    Rs. 1755.0

# Your job:
# 1. call make_bill() with no prices. What happens?
# 2. ask the user for prices with input().split(),
#    turn each one into an int (Day 10 project),
#    then send them with make_bill(*prices)
def make_bill(*prices, discount=0):
    if not prices:
        print("Cart is empty!")
        return 0
    total = sum(prices)
    saved = total * discount / 100
    print(f"Items:     {len(prices)}")
    print(f"Costliest: Rs. {max(prices)}")
    print(f"Total:     Rs. {total}")
    print(f"Discount:  Rs. {round(saved, 2)}")
    return round(total - saved, 2)
print("--- Test 1: Empty Cart ---")
pay_empty = make_bill()
print(f"To pay: Rs. {pay_empty}\n")
print("--- Test 2: User Input ---")
user_input = input("Enter prices separated by spaces: ").split()
prices_list = [int(p) for p in user_input]
# pay = make_bill(1200, 350, 140, 260, discount=10)
pay = make_bill(*prices_list, discount=10)
print(f"To pay:    Rs. {pay}")

