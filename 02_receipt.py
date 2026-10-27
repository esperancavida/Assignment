# Ask for an item name, its price, and the quantity bought. 
# Calculate the subtotal, add 13% VAT, and 
# print a neatly formatted receipt with the item name, quantity, 
# and final total — all using f-strings.
item=input("Enter the item name: ")
price=float(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity bought: "))
subtotal=price*quantity
vat=subtotal*0.13
total=subtotal+vat

print("----------------------------------")
print(f"Receipt:")
print("----------------------------------")
print(f"Item: {item}\nQuantity: {quantity}\nSubtotal: Rs.{subtotal:.2f}\nVAT (13%): Rs.{vat:.2f}")
print("----------------------------------")
print(f"Total: Rs.{total:.2f}")
print("----------------------------------")
