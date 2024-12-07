# Factorial of a Number: Write a program to calculate the factorial of a given number using a while loop.
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
 
    i=1
    while i <= n:
        result *= i
        i += 1   
 
    while n > 0:
        result *= n
        n -= 1   
 
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a integer: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            fact_res = factorial(num * 7) 
            print(f"The factorial of {num * 7} is: {fact_res}")
    except ValueError as e:
        print(f"Invalid input: {e}")
 
    return result

if __name__ == "__main__":
 
    n= int(input("Enter the Number :"))
    print(factorial(n))

 
    num = int(input("Enter the Number :"))
 
    print(factorial(num))
    
 
 
    print(factorial(num))
 
 
    print(factorial(num))
 
 
     res=factorial(num)
    print(res)
     
 
 
