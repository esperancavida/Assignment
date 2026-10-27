"""Start with Rs. 1000 in the account. Show the menu again and again with 
while True. The user can check the balance, deposit, withdraw (only if there 
is enough money) or exit with break."""
# Your job:
# 1. ask for a PIN first, only 3 tries (like Project 02)
# 2. don't allow a deposit of 0 or less
balance = 1000
pin = "1234"
tries = 0
authenticated = False

while tries < 3:
    input_pin = int(input("Enter your PIN: "))
    tries += 1

    if input_pin == int(pin):
       print("PIN accepted.\n")
       authenticated = True
       break
    else:
        remaining = 3 - tries
        if remaining > 0:
            print(f"Invalid PIN. You have {remaining} attempt(s) left.")
        else:
            print("Too many invalid attempts. Exiting.")
            exit()
while authenticated:
    print("--- ATM MENU ---\n1. Check Balance  \n2. Deposit  \n3. Withdraw  \n4. Exit")
    choice = input("Choose (1-4): ").strip()
       
    if choice == "1":
               print(f"Current Balance: Rs. {balance}")
    elif choice == "2":
           amount = int(input("Amount to deposit: "))
           if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
           else:
                balance += amount
                print(f"Deposited successfully.New balance: Rs. {balance}")        
    elif choice == "3":
            amount = int(input("Amount to withdraw: "))
            if amount > balance:
                print("Not enough money")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                balance -= amount
                print(f"Take your cash. Left: Rs. {balance}")
    elif choice == "4":              
            print("Thank you for using this ATM! Bye")
            break
    else:
            print("Invalid Choice.Please choose 1 to 4")
            break