"""Start with two contacts. Ask the user for a new name and 
number and add them. Print all contacts and the total. 
Then ask for a name to search, and use get() so a missing name 
prints "Not found" instead of crashing."""
# Your job:
# 1. remove one contact with pop()
# 2. print only the names: list(contacts.keys())
contacts = {"Ram": "9801111111", "Sita": "9802222222"}

name  = input("New contact name: ")
phone = input("Phone number: ")
contacts[name] = phone              # add it

print("All contacts:", contacts)
print("Total:", len(contacts))

find = input("Search a name: ")
print("Number:", contacts.get(find, "Not found"))
remove=input("Enter person who you want to remove from contact:")
removed_phone = contacts.pop(remove, None)
if removed_phone:
    print(f"Success: Removed {remove} (Number: {removed_phone})")
else:
    print(f"'{remove}' was not found in your contacts.")
print("\nRemaining contact names:", list(contacts.keys()))
print(f"Sorted contact names:{sorted(contacts)}")