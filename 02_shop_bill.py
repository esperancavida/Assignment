"""Make a menu dictionary of items and prices. 
Ask what the customer wants and how many. Use get() 
to find the price, then print the total bill. 
Then add a new item to the menu and print some menu facts."""
# Your job:
# 1. add "momo": 150 to the menu
# 2. print the cheapest and costliest price
# 3. print item names A-Z with sorted(prices)
prices = {"tea": 20, "coffee": 50, "samosa": 25}
print("Menu:", prices)

item = input("What do you want? ").strip().lower()
qty  = int(input("How many? "))

price = prices.get(item, 0)
if price > 0:

    print("Price of one:", price)
    print("Total bill  :", price * qty)
else:
    print("Sorry, that item is not on the menu.\n")
print(f"Cheapest Price:{min(prices)}")
print(f"Costliest Price:{max(prices)}")
prices["momo"]=150
print("--- Added 'momo' to the menu ---")
print(prices)
print("--- Sorted Menu ---")
for food in sorted(prices):
    print(f"{food.capitalize()}: Rs.{prices[food]} ")
# print(prices["coffee"])#gives value of coffee key
