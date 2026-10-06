"""Write two small functions that return the converted temperature. Use 
float(input()) from Day 03 so the user can type 36.6 too."""
# Your job:
# 1. ask: C to F, or F to C? Then call the right one (Day 07)
# 2. write is_hot(c) that returns True above 30
def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9
def is_hot(c):
    return c > 30
while True:
    print("\n--- Temperature Converter ---")
    print("1. Convert Celsius to Fahrenheit (C to F)")
    print("2. Convert Fahrenheit to Celsius (F to C)")
    print("Type 'quit' to exit the program.")
    choice = input("Choose (1, 2, or quit): ").strip().lower()
    if choice == "quit":
        break
    if choice not in ["1", "2"]:
        print("Invalid choice. Please select 1, 2, or type 'quit'.")
    if choice == "1":
        c_temp = float(input("Enter temperature in Celsius: "))
        f_result = c_to_f(c_temp)
        print(f"{c_temp}°C in Fahrenheit is {f_result:.1f}°F")
        if is_hot(c_temp):
            print("Stay hydrated, it's hot!")

    elif choice == "2":
        f_temp = float(input("Enter temperature in Fahrenheit: "))
        c_result = f_to_c(f_temp)
        print(f"{f_temp}°F in Celsius is {c_result:.1f}°C")
        if is_hot(c_result):
            print("Stay hydrated, it's hot!")

    else:   
        print("Invalid choice. Please run the program again and select 1 or 2.")

