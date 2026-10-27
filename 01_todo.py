"""Start with an empty list called tasks.
 Let the user add a task with .append(), then loop through 
 tasks with a plain for loop to print each one with a number
in front (count up yourself with a variable, using += 1).
 Finally, remove a task by number using .pop().
 Keep asking until the user types "quit".
"""
tasks=[]
task = input("Add a task (or 'quit'): ")
while task != "quit":
    tasks.append(task)
    task = input("Add a task (or 'quit'): ")

count = 1
for t in tasks:
    print(f"{count}. {t}")
    count += 1
while True:
    task_number = int(input("Enter the number of the task to remove (or 0 to quit): "))
    if task_number == 0:
                break
    elif 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task removed: {removed_task}")       
    else:
                print("Invalid task number. Please enter valid number!")

count = 1
for t in tasks:
    print(f"{count}. {t}")
    count += 1

        