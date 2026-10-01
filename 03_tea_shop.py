"""Show the menu dictionary. Ask for an item. If it's on the menu, 
ask how many and print the total. If not, say sorry. Then give a discount 
with if / elif / else."""
# Your job (inside the if block):
# 500 or more -> 10% off, 200 or more -> 5% off,
# else no discount. Print the final bill.
menu = {"tea": 20, "coffee": 50, "momo": 150}
print("Menu:", menu)

item = input("What do you want? ").strip().lower()

if item in menu:
    qty = int(input("How many? "))
    total = menu[item] * qty
    if total >= 500:
        total-= total*0.10
        print(f"Total: Rs. {total}")
    elif total >= 200:
        total-= total*0.05
        print(f"Total: Rs. {total}")
    else:
        print(f"Total: Rs. {total}")
else:
    print("Sorry, we don't have that")