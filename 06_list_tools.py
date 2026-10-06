"""remove_duplicates() uses the set trick from Day 05. total_price() loops over
a Day 06 dictionary. Both return the answer, so you can use it later."""
# Your job:
# 1. write common(a, b): items in both lists
#    (hint: set(a) & set(b) from Day 05)
# 2. write costliest(cart): return the costliest item's name
def remove_duplicates(items):
    return sorted(set(items))

def total_price(cart):
    total = 0
    for price in cart.values():
        total += price
    return total
def common(a, b):
    return list(set(a) & set(b))
def costliest(cart):
    if not cart:
        return None  # Return None if the cart is empty
    return max(cart, key=cart.get)

names = ["Ram", "Sita", "Ram", "Hari", "Sita"]
print(remove_duplicates(names))   # ['Hari', 'Ram', 'Sita']

cart = {"rice": 1200, "oil": 350, "sugar": 140}
print(f"Total price: {total_price(cart)}")
print(f"Common items: {common([1, 2, 3], [2, 3, 4])}")
print(f"Costliest item: {costliest(cart)}")
