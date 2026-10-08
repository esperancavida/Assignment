"""place_order() uses all three: a normal box for the customer, *items for the 
food, and **options for extras. The menu is a Day 06 dictionary. enumerate() 
(Day 10) numbers each line."""
# Order for Hari
# 1. momo: Rs. 150
# 2. tea: Rs. 30
# 3. pizza: not on the menu
# Delivery: Rs. 50
# Note: spicy = extra
# Total: Rs. 230

# Your job:
# 1. save the returned total, then add 13% VAT
# 2. ask the user for items with input().split(),
#    then send them with place_order("You", *items)
menu = {"momo": 150, "chowmein": 120, "tea": 30, "lassi": 80}

def place_order(customer, *items, **options):
    print(f"Order for {customer}")
    total = 0
    for num, item in enumerate(items, start=1):
        if item in menu:
            print(f"{num}. {item}: Rs. {menu[item]}")
            total += menu[item]
        else:
            print(f"{num}. {item}: not on the menu")

    if options.get("delivery"):
        print("Delivery Charge: Rs. 50")
        total += 50
    for key, value in options.items():
        if key != "delivery":
            print(f"Note:\n{key} = {value}")

    print(f"Total: Rs. {total}")
    return total

# place_order("Hari", "momo", "tea", "pizza", delivery=True, spicy="extra")
hari_subtotal = place_order("Hari", "momo", "tea", "pizza", delivery=True, spicy="extra")
vat_amount = hari_subtotal * 0.13
grand_total = hari_subtotal + vat_amount
print(f"VAT (13%): Rs. {round(vat_amount, 2)}")
print(f"Grand Total (with VAT): Rs. {round(grand_total, 2)}\n")
user_items = input("Enter the items you want to order (separated by spaces): ").lower().split()
place_order("You", *user_items)

