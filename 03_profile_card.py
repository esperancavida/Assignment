"""Ask for the user's full name and birth year. 
Clean the name with .strip() and .title(). 
Calculate their age from the current year. 
Print a profile card showing their name in UPPERCASE, their age,
and whether their name is "long" (more than 10 letters) 
using len() and a comparison."""
fullname=input("Enter your full name: ")
birth_year=int(input("Enter your birth year: "))
current_year=2026
age=current_year-birth_year
is_long_name = len(fullname.strip()) > 10
print("-------------------------------------------------")
print(f"Profile Card:\nName: {fullname.upper()}\nAge: {age}\nIs your name long(more than 10 letters): {is_long_name}")
print("-------------------------------------------------")