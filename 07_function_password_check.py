"""The Day 08 password checker, now split into small functions.
Look at has_number(): return inside the loop stops it as soon as a number 
is found."""
# Your job: write has_capital(password)
# (hint: ch.isupper()) and use it in is_strong()
def has_number(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False
def has_capital(password):
    for ch in password:
        if ch.isupper():
            return True
    return False

def is_strong(password):
    return len(password) >= 8 and has_number(password)  and has_capital(password)

while True:
    password = input("New password: ")
    if is_strong(password):
        print("Strong password. Saved!")
        break
    print("Use 8 or more letters, at least one capital letter and at least one number")
