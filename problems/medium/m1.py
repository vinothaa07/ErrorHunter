'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
def math_operations_menu(a,b,operator):
   
    if choice == 2:
        print("Subtraction:", a - b)   
    elif choice == 1:
        print("Addition:", a + b)   
    elif choice == 4:
        print("Division:", a / b)   
    elif choice == 3:
        print("Multiplication:", a * b)   
    elif choice == 5:
        print("Modulo:", a // b)   
    else:
        print("Invalid option")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
choice = int(input("Enter your choice: "))
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
math_operations_menu(num1,num2,choice)