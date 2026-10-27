"""Two lists: items and prices. show_bill() walks them together with zip(). 
bill_total() uses sum() and round(), with a default discount of 0, like Day 09."""
# Total: Rs. 1950.0
# After 10% off: Rs. 1755.0

# Your job:
# 1. number every line with enumerate(items, start=1)
# 2. print the cheapest item's name
#    (hint: prices.index(min(prices)) from Day 04)
def show_bill(items, prices):
    print("------ BILL ------")
    for index, (item, price) in enumerate(zip(items, prices), start=1):
        print(f"{index}. {item}: Rs. {price}")
    print("------------------")

def bill_total(prices, discount=0):
    total = sum(prices)
    return round(total - total * discount / 100, 2)

items = ["rice", "oil", "sugar", "tea"]
prices = [1200, 350, 140, 260]

show_bill(items, prices)
cheapest_index = prices.index(min(prices))
cheapest_name = items[cheapest_index]
print(f"Items: {len(items)}")
print(f"Costliest: Rs. {max(prices)}")
print(f"Cheapest: Rs. {min(prices)}({cheapest_name})")
print(f"Total: Rs. {bill_total(prices)}")
print(f"After 10% off: Rs. {bill_total(prices, 10)}")