"""Take the Day 08 ATM and split it into functions. deposit() and withdraw() 
get the old balance and return the new one. The while True menu at the bottom 
stays almost the same."""
# Your job:
# 1. write check_pin(pin) that returns True or False
# 2. ask for the PIN first, only 3 tries (Day 08)
 
def check_pin(pin):
    return pin == "1234"

def show_menu():
    print("Menus:\n1. Balance  \n2. Deposit  \n3. Withdraw  \n4. Exit")

def deposit(balance, amount):
    if amount <= 0:
        print("Amount must be more than 0")
        return balance
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Not enough money")
        return balance
    return balance - amount

balance = 1000
pin_tries = 3
authenticated = False
while pin_tries > 0:
    entered_pin = input("Enter your 4-digit PIN: ").strip()
    if check_pin(entered_pin):
        authenticated = True
        print("Access Granted!")
        break
    else:
        pin_tries -= 1
        print(f"Incorrect PIN. Tries remaining: {pin_tries}")
if authenticated:
    while True:
        show_menu()
        choice = input("Choose (1-4): ").strip()
        
        if choice == "1":
            print(f"Balance: Rs. {balance}")
        elif choice == "2":
            amount = int(input("Amount to deposit: "))
            balance = deposit(balance, amount)
            print(f"Amount deposited: Rs. {amount}")
            print(f"Total balance: Rs. {balance}")
        elif choice == "3":
            amount = int(input("Amount to withdraw: "))
            balance = withdraw(balance, amount)
            print(f"Amount withdrawn: Rs. {amount}")
            print(f"Total balance: Rs. {balance}")
        elif choice == "4":
            print("Thank you for using this ATM!")
            break
        else:
            print("Please choose 1 to 4")
else:
    print("Card blocked. Too many incorrect attempts.")