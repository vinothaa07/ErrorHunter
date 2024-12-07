# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
 
def check_number(num):
    if num > 0:
        print("Positive")  
    elif num < 0:
        print("Negative")  
    else:
        print("Number is zero")   
if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    check_number(num)
 
    num = int(input("Enter the Number : "))
    res = check_number(num)
    print(res)
 
 
    if num < 0:
        print("Number is Negative")  
    elif num > 0:
        print("Number is Positive")  
    else:
        print("Number is Zero")   
 