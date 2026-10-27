"""The user types marks with spaces. split() from Day 04 cuts the text, and a 
loop turns every part into an int. Then built-ins do all the hard work."""
# Students: 4
# Highest:  92
# Lowest:   45
# Total:    282
# Average:  70.5
# Sorted:   [92, 78, 67, 45]

# Your job:
# 1. print how many passed (40 or more)
# 2. if all() of them passed, print "Everyone passed!"
text = input("Enter marks with spaces: ")    # 67 45 92 78
marks = []
for part in text.split():
    marks.append(int(part))
# list comprehension combined with built-in  function len() counts how many students passed
passed_count = len([mark for mark in marks if mark >= 40])#it counts how many students passed
print(f"Students: {len(marks)}")
print(f"Passed:   {passed_count}")
print(f"Highest:  {max(marks)}")
print(f"Lowest:   {min(marks)}")
print(f"Total:    {sum(marks)}")
print(f"Average:  {round(sum(marks) / len(marks), 2)}")
print(f"Sorted:   {sorted(marks, reverse=True)}")
if all(mark >= 40 for mark in marks):
    print("Everyone passed!")
