"""Start with a nested list — 3 rows of 4 seats each, 
every seat set to "Empty". Let the user type a name and 
a row/column number to seat them, print the whole chart row 
by row, then count how many seats are still empty by adding 
up row.count("Empty") for each row."""

chart = [["Empty"] * 4 for _ in range(3)]

while True:
    name = input("\nEnter student name (or type 'exit' to quit): ").strip()
    if name.lower() == "exit":
        print("\nFinal seating chart:")
        for r in chart:
            print(r)
            
        empty_seats = 0
        for row in chart:
            empty_seats += row.count("Empty")
        print(f"Empty seats: {empty_seats}")
        break

    row_input = input("Row (0-2): ").strip()
    col_input = input("Column (0-3): ").strip()

    if not (row_input.isdigit() and col_input.isdigit()):
        print("Invalid input. Please enter numbers from (0-2) for row and (0-3) for column.")
        continue

    row = int(row_input)
    col = int(col_input)
    
    if not (0 <= row <= 2 and 0 <= col <= 3):
        print("Invalid seat position. Try again.")
        continue

    if chart[row][col] != "Empty":
        print(f"Seat at row {row}, col {col} is already taken by '{chart[row][col]}'.")
        continue

    chart[row][col] = name
    print(f"Booked seat at row {row}, col {col} for '{name}'.")

    print("\nCurrent seating chart:")
    for r in chart:
        print(r)

    empty_seats = 0
    for row in chart:
        empty_seats += row.count("Empty")
    print(f"Empty seats: {empty_seats}")

