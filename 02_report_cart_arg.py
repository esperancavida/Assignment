""" The student's name is a normal box. Every subject comes in through **marks,
so each student can have different subjects. Use if/else (Day 07), .items()
(Day 06) and sum, len, max (Day 10)."""
# ===== Sita =====
# math: 88 (Pass)
# science: 35 (Fail)
# english: 91 (Pass)
# nepali: 72 (Pass)
# Total: 286
# Average: 71.5
# Best subject: english

# Your job:
# 1. if every mark is 40 or more, print "Promoted!"
#    (hint: all() from Day 10)
# 2. save Ram's marks in a dictionary, then call
#    report_card("Ram", **ram_marks)
def report_card(name, **marks):
    print(f"===== {name} =====")
    for subject, mark in marks.items():
        if mark >= 40:
            result = "Pass"
        else:
            result = "Fail"
        print(f"{subject}: {mark} ({result})")

    total = sum(marks.values())
    average = round(total / len(marks), 2)
    best = max(marks, key=marks.get)
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Best subject: {best}")
    if all(mark >= 40 for mark in marks.values()):
        print("Promoted!")
    else:
        print("Not Promoted.")

report_card("Sita", math=88, science=35, english=91, nepali=72)
ram_marks = {
    "math": 75,
    "science": 64,
    "english": 82,
    "nepali": 50
}

report_card("Ram", **ram_marks)

