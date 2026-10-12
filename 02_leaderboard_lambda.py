"""Each student is a dictionary inside a list (Day 04 + Day 06). Rank them with
sorted() and reverse=True, number them with enumerate() (Day 10), and use the
one-line if for Pass/Fail."""
# === Leaderboard ===
# 1. Sita: 92 (Pass)
# 2. Gita: 85 (Pass)
# 3. Ram: 78 (Pass)
# 4. Hari: 35 (Fail)
# 5. Anil: 28 (Fail)
# Passed: Ram, Sita, Gita
# Pass rate: 3 of 5

# Your job:
# 1. print the class average
#    (hint: map() the marks, then sum() and len())
# 2. write add_student(name, marks) with def (Day 09)
#    that appends a new dictionary to students
students = [
    {"name": "Ram", "marks": 78},
    {"name": "Sita", "marks": 92},
    {"name": "Hari", "marks": 35},
    {"name": "Gita", "marks": 85},
    {"name": "Anil", "marks": 28},
]
def add_student(name, marks):
    students.append({"name": name, "marks": marks})
add_student("Shyam", 65)
print(students)
ranked = sorted(students, key=lambda s: s["marks"], reverse=True)

print("=== Leaderboard ===")
for rank, s in enumerate(ranked, start=1):
    status = "Pass" if s["marks"] >= 40 else "Fail"
    print(f"{rank}. {s['name']}: {s['marks']} ({status})")

passed = list(filter(lambda s: s["marks"] >= 40, students))
names = list(map(lambda s: s["name"], passed))
print("Passed:", ", ".join(names))
print(f"Pass rate: {len(passed)} of {len(students)}")
all_marks = list(map(lambda s: s["marks"], students))
class_average = sum(all_marks) / len(all_marks)
print(f"Class average: {class_average:.2f}")

