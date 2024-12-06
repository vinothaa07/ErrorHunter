# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
def check_number(num):
    print("The given number is Negative" if (num  < 0 ) else  "The given number is Positive" if (num > 0) else "The given number is Zero")
if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    check_number(num)
    
