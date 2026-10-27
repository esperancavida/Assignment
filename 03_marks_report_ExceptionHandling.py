"""add_mark() uses raise when a mark is not between 0 and 100. average() 
returns 0 for an empty list instead of crashing with ZeroDivisionError."""
# Mark: 80
# Mark: abc
# Skipped: invalid literal for int() with base 10: 'abc'
# Mark: 150
# Skipped: Mark must be 0 to 100
# Mark: 70
# Mark: q
# Marks: [80, 70]
# Average: 75.0

# Your job:
# 1. print Pass if average >= 40, else Fail
# 2. print max() and min() of marks. What happens
#    if the list is empty? Catch that error too!
def average(marks):
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return 0

def add_mark(marks, text):
    mark = int(text)
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be 0 to 100")
    marks.append(mark)

marks = []
print("Type marks one by one. Type q to finish.")
while True:
    text = input("Mark: ")
    if text == "q":
        break
    try:
        add_mark(marks, text)
    except ValueError as e:
        print("Skipped:", e)
        
avg_score = average(marks)
print("\n=== Result Summary ===")
print("Marks:", marks)
print("Average:", round(average(marks), 1))
if avg_score >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")
try:
    highest = max(marks)
    lowest = min(marks)
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)
except ValueError:
    print("Highest Mark: N/A (No marks recorded)")
    print("Lowest Mark: N/A (No marks recorded)")

