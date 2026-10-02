"""Ask the user for a number. Print its times table from 1 to 10 
with a for loop and range()."""
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
num = int(input("Which table? "))
upto=int(input("Upto which number? "))
total = 0
for i in range(1, upto + 1):
    print(f"{num} x {i} = {num * i}")
    
    total+=num * i
print(f"Total: {total}")
