# Sum of Digits: Write a program to calculate the sum of digits of a number using a while loop.
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num + 10  
    return total

if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    
    
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  # Add the last digit to total
        num //= 10  # Remove the last digit
    return total

if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    print("The sum of the digits is:", sum_of_digits(num))