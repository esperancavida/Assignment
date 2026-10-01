"""Ask for a name and three marks. Use zip() to build a marks
dictionary, then put it inside a report dictionary. Print the 
report card, the total, the average and the best subject."""
# Your job:
# 1. total = sum(marks.values()), print it
# 2. print the average: total / len(marks)
# 3. best subject: max(marks, key=marks.get)
name = input("Student name: ")
m1 = int(input("Math: "))
m2 = int(input("Science: "))
m3 = int(input("English: "))

subjects = ["math", "science", "english"]
marks  = dict(zip(subjects, [m1, m2, m3]))
report = {"name": name, "marks": marks}
print("===================== REPORT CARD ========================")
print("Name :", report["name"])
print("Marks:", report["marks"])
total = sum(marks.values())
print(f"Total Marks   : {total}")
average = total / len(marks)
print(f"Average Marks : {average:.2f}") 
best_subject = max(marks, key=marks.get)
print(f"Best Subject  : {best_subject.capitalize()} ({marks[best_subject]} marks)")
print("===========================================================")