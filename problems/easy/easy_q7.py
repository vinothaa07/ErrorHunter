def sum_of_digits(num):
    """Calculate the sum of digits of a number."""
    total = 0
    num = abs(num)   
    while num > 0:
 
        digits = num%10
        total += digits 
        num //= 10
    return total

if __name__ == "__main__":
    number = int(input("Enter the Number : "))
    print("Sum of digits:",sum_of_digits(number))
    
    
    
 
 
        n=num%10
        total+=n
        num=num//10
 
 
        total += num % 10
 
 
        num //= 10  
 
 
    return total

if __name__ == "__main__":
 
    num = int(input("Enter the Number : "))
 
    print(sum_of_digits(num))
 
 
 
    res=sum_of_digits(num)
    print(res)    
 
    print("sum of digits:",sum_of_digits(num))
 
    num1 = int(input("Enter the Number : "))
    print(sum_of_digits(num1))
 
 
 
 
        total += num % 10  
        num //= 10          
    return total

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))  
        result = sum_of_digits(num)
        print(f"The sum of digits is: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
 
 