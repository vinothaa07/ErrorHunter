'''
Create a program that checks whether a given number is a prime number or not.
'''
def is_prime(num):
    if num==0 or num==1:
        b="it is not a prime number"
        return b
    elif num ==2 or num ==3:
        b="it is a prime number"
        return b
    else:
        for i in range(2, (num//2)+1):
            if num % i == 0:
                b="it is not a prime number"
                return b
                break
            else:
                b="it is a prime number "
                return b
    

num = int(input("Enter a number: "))
call=is_prime(num)
print(call)

