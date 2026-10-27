"""Keep usernames and passwords in a dictionary. Ask the user to log in. 
Use in to check the username, then check the password. Clean the name with 
.strip() and .lower(), so " RAM " also works."""
# Your job:
# 1. add yourself to the users dictionary
# 2. empty password? print "Password missing"
users = {"ram": "ram123", "sita": "sita456"}
users["asha"]="asha123"
name = input("Username: ").strip().lower()
password = input("Password: ")

if name not in users:
    print("User not found")
elif users[name] == password:
    print(f"Welcome, {name.title()}!")

# elif password=="":
#     print("Password missing")
# alternatively,
elif not password:
    print("Password missing")
else:
    print("Wrong password")