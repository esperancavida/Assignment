n1=float(input("Enter your first number: "))
n2=float(input("Enter your second number: "))
operator=input("Choose your operator (+,-,*,/,//,%,**): ")
match operator:
    case "+":
        print(n1+n2)
    case "-":
        print(n1-n2)
    case "*":   
        print(n1*n2)
    case "/":
        print(n1/n2)
    case "//":
        print(n1//n2)
    case "%":       
        print(n1%n2)
    case "**":
        print(n1**n2)   
    case _:
        print("Invalid operator. Please choose a valid operator (+,-,*,/,//,%,**).")