"""Keep student marks in a dictionary. Loop with .items() and print Pass or 
Fail for each student. Then print the class average."""
# Your job:
# 1. find the topper (hint: top = 0, then check each mark)
# 2. give a grade A / B / C with elif (Day 07)
marks = {"Ram": 78, "Sita": 92, "Hari": 35, "Gita": 64}
total = 0
top = 0

for name, mark in marks.items():
    if mark>=80:
        print(f"{name}: {mark} \nGrade: A\nRemarks: Pass")
    elif mark>=60:
        print(f"{name}: {mark} \nGrade: B\nRemarks: Pass")
    elif mark >= 40:
        print(f"{name}: {mark} \nGrade: C\nRemarks: Pass")
    else:
        print(f"{name}: {mark} \nGrade:N/A\nRemarks: Fail")
    total += mark
    if mark > top:
        top = mark

average = total / len(marks)
print(f"Class average: {average}")
print(f"Topper: {list(marks.keys())[list(marks.values()).index(top)]}({top} marks)")
