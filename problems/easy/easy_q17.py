# Print X N Times
def print_x_n_times(x, n):  # Bug: Loop runs one less time than expected
        print(x*n)
if __name__ == "__main__":
 # Handle the input  by Yourself
 n=int(input("Enter the number of times:"))
 x="X"
 print_x_n_times(x,n)