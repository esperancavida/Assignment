"""Store each item as a small list [name, price, quantity]
inside one big cart list. Loop through cart, print each item's
line total (price * quantity) using an f-string, and add every 
line total together into a grand total printed at the end.
"""
cart = [
    ["Cup noodles", 100, 2],
    ["Shampoo", 450, 3],
    ["Detergent", 350, 1],
]

grand_total = 0
print("Shopping Cart:")
print("--------------------------")
print("Product name:\t|Price")
print("--------------------------")
for item in cart:
    name, price, qty = item
    line_total = price * qty
    print(f"{name}: \t|Rs. {line_total}")
    grand_total += line_total
print("--------------------------")
print(f"Grand total: \t|Rs. {grand_total}")
print("--------------------------")