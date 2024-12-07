def sum_of_digits(num):
    """Calculate the sum of digits of a number."""
    total = 0
    num = abs(num)   
    while num > 0:
 
        total += num % 10
        num //= 10  
    return total

if __name__ == "__main__":
 
    num = int(input("Enter the Number : "))
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
 