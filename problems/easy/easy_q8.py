 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
    rev = 0
    revs=reversed(num)
    for x in revs:
        print(x)
        digit = num % 10
        rev+=digit   
        num //= 10
    return num   
if __name__ == "__main__":
    num = int(input("Enter num : "))
    res = reverse_number(num)
    print(res)

 
