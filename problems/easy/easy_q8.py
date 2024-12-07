 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
 
    rev = 0
    revs=reversed(num)
    for x in revs:
        print(x)
        digit = num % 10
        rev+=digit   
 
 
    rev = ""
    while num != 0:
 
        digit = num % 10
        rev = rev*10 + digit   
 
        num //= 10
    return rev   
 
 
 
 
if __name__ == "__main__":
    num = int(input("Enter num : "))    #123
    res = reverse_number(num)
    print(res)

 
