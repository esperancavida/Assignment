"""Ask for name, age and city, and put them in a tuple.
Unpack the tuple and print a neat ID card. 
Then make a tuple of 3 marks and print the highest,
the lowest and the total. Finally, change the city using the 
list trick."""
name = input("Name: ")
age  = input("Age: ")
city = input("City: ")
student = (name, age, city)     # packing
n, a, c = student                # unpacking

print("======= ID CARD =======")
print("Name:", n)
print("Age :", a)
print("City:", c)
print("=======================")
marks = (70, 85, 90)
print("Marks:")
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
print("Total marks:",sum(marks))
print("=======================")
 
student_list=list(student)
student_list[2] = input("\nEnter your new city: ")  # update city
student = tuple(student_list)  # convert back to tuple
n, a, c = student 
print("\n=== UPDATED ID CARD ===")
print("Name:", n)
print("Age :", a)
print("City:", c)
print("=======================")

