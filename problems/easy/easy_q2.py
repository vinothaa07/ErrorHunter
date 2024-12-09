# Find the Largest Number: Accept two numbers and print the larger one.
def largest_of_two(a, b):
    if a > b:
 
        return a  
 
    else:
 
        print(num1,"is greater")
        return a  
    else:
        print(num2,"is greater")
 
 
 
        return b
if __name__ == "__main__":
 
    a = int(input("Enter the First Number :"))
    b = int(input("Enter the Second Number :"))
    res = largest_of_two(a,b)
    print(res)
 