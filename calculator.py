print("Select an operaton to perform: ")
print("1. ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVISION")


operation = input()

if operation == "1":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The sum is ",num1+num2)

elif operation == "2":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The difference is ",num1-num2)    

elif operation == "3":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The multiplication is ",num1*num2)     

elif operation == "4":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The division is  ",num1/num2)      

else:    
    print("Invalid Entry")

