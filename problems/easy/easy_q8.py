 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
    rev = 0
    while num != 0:
        digit = num % 10
        print(digit)
        num = num //10  
if __name__ == "__main__":
    num = int(input("Enter num : "))
    res = reverse_number(num)
    print(res)

 
