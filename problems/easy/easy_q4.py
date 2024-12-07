# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
        
 
    num = int(input("Enter the Number : "))
    res = check_number(num)
    print(res)
 
 
    if num < 0:
        print("Number is Negative")  
    elif num > 0:
        print("Number is Positive")  
    else:
        print("Number is Zero")   
  