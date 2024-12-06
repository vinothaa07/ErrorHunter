# Sum of Digits: Write a program to calculate the sum of digits of a number using a while loop.
def sum_of_digits(num):
    total = 0
    while num > 0:
        digits = num%10
        total += digits 
        num //= 10
    return total

if __name__ == "__main__":
    number = int(input("Enter the Number : "))
<<<<<<< HEAD
    print("Sum of digits:",sum_of_digits(number))
=======
    print(sum_of_digits(number))
>>>>>>> 953d0fe27f70dc1aeb5d9385731446869bfd4768
    
    
    
