# Factorial of a Number: Write a program to calculate the factorial of a given number using a while loop.
def factorial(n):
    result = 1
    i=1
    while i <= n:
        result *= i
        i += 1   
    return result

if __name__ == "__main__":
    num = int(input("Enter the Number :"))
    print(factorial(num))
    
