# Print X N Times
def print_x_n_times(x, n):
    for i in range(0, n):  # Bug: Loop runs one less time than expected
        print(x)
if __name__ == "__main__":
 # Handle the input  by Yourself
 user = int(input("Enter a number:"))
 no_of = int(input("Enter a number of times:"))
 print_x_n_times(user,no_of)