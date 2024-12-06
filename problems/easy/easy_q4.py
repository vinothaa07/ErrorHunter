# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
def check_number(num):
    if num < 0:
        print("Negative")  
    elif num > 0:
        print("Positive")  
    else:
        print("number entered is 0")   
        
if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    res = check_number(num)
    
    
    
