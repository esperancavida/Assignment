"""Two friends type their guest lists (names separated by commas, no spaces). 
Make each list a set, then print: guests on both lists, 
all guests, and the total number of guests. 
Add one guest with add(), and remove one with discard().
"""


list1_input = input("Enter first guest list (names separated by commas, no spaces): ").strip()
list2_input = input("Enter second guest list (names separated by commas, no spaces): ").strip()


guests1 = set(list1_input.split(",")) if list1_input else set()
guests2 = set(list2_input.split(",")) if list2_input else set()


both_lists = guests1 & guests2


all_guests = guests1 | guests2


total_unique = len(all_guests)

print(f"First guest list:{guests1}:\nSecond guest list:{guests2}:")
print("\nGuests on both lists:", both_lists)
print("All guests:", all_guests)
print("Total unique guests:", total_unique)


new_guest = input("\nEnter a guest to add: ").strip()
if new_guest:
    all_guests.add(new_guest)
    print(f"Added '{new_guest}'. Updated guest list:", all_guests)
    
remove_guest = input("\nEnter a guest to remove: ").strip()
if remove_guest:
    all_guests.discard(remove_guest)
    print(f"Removed '{remove_guest}'. \nUpdated guest list:", all_guests)
   

