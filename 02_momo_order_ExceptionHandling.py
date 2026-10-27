"""The menu is a dictionary (Day 06). A wrong item gives a KeyError, a wrong
quantity gives a ValueError. else adds to the bill only when both worked."""
# Item (or done): pizza
# Sorry, we don't have pizza
# Item (or done): veg momo
# How many? two
# Quantity must be a number.
# Item (or done): veg momo
# How many? 2
# Added 2 x veg momo
# Item (or done): done
# Total bill: Rs. 240

# Your job:
# 1. if qty is 0 or less, raise ValueError("Quantity
#    must be more than 0"), and print e in except
# 2. save each order in a list and print it at the end
menu = {"veg momo": 120, "chicken momo": 180, "chowmein": 150}
total = 0
orders = [] 
print("=== MOMO HOUSE ===")
for item, price in menu.items():
    print(f"- {item}: Rs. {price}")

while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    try:
        price = menu[item]
        qty = int(input("How many? "))
        if qty<=0:
            raise ValueError("Quantity must be more than 0")
    except KeyError:
        print("Sorry, we don't have", item)
    except ValueError as e:
        if str(e) == "Quantity must be more than 0":
            print(e)
        else:
            print("Quantity must be a number.")
       
    else:
        cost = price * qty
        total += price * qty
        orders.append(f"{qty} x {item} (Rs. {cost})")
        print(f"Added {qty} x {item}")
print("\n=== Order Summary ===")
if orders:
    for order in orders:
        print(f"- {order}")
else:
    print("No items ordered.")
print("Total bill: Rs.", total)

