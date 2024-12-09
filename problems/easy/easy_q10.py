# Check Palindrome Number: Use a do-while loop to determine if a given number is a palindrome
def is_palindrome(num):
    original = num
 
    reverse = 0
 
    do:
 
    while num != 0:
        reverse = reverse * 10 + num % 10
 
        num //= 10
    
    return reverse == original

 
 
 
    if res:
        print("its palindrome")
    else:
        print("its not palindrome")
 
    print(res)
 
