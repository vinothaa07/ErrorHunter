# Print X N Times
def print_x_n_times(x, n):
    for i in range(n):  # Bug: Loop runs one less time than expected
        print(x)
if __name__ == "__main__":
    x=input("enter the string:")
    n=int(input("enter number of times to diplay:"))
 # Handle the input  by Yourself
print_x_n_times(x,n)