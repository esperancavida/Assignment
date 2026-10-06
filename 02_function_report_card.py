"""get_grade() uses if/elif from Day 07 and returns a grade. average() works
on any marks dictionary from Day 06. A for loop prints every student."""
# Ram: 78 -> B
# Sita: 92 -> A
# Hari: 35 -> F
# Gita: 64 -> B
# Class average: 67.25

# Your job:
# 1. write count_passed(marks): how many got 40 or more?
# 2. write topper(marks): return the name with the top mark
def count_passed(marks):
    count = 0
    for mark in marks.values():
        if mark >= 40:
            count += 1
    return count

def topper(marks):
    return max(marks, key=marks.get)#marks.get returns the value of the key, so max will return the key with the highest value

def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"

def average(marks):
    return sum(marks.values()) / len(marks)

marks = {"Ram": 78, "Sita": 92, "Hari": 35, "Gita": 64}
print("Report Card:")
print("-----------------------")
print("Name\t| Mark \t|Grade")
print("-----------------------")
for name, mark in marks.items():
    print(f"{name}:\t| {mark} \t|{get_grade(mark)}")
print("-----------------------")
print(f"Class average: {average(marks)}")
print(f"Number of students who passed: {count_passed(marks)}")
print(f"Topper: {topper(marks)}")