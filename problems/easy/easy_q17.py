# Print X N Times
def print_x_n_times(x, n):
    for i in range(1, n):  # Bug: Loop runs one less time than expected
        print(x)
if __name__ == "__main__":
 # Handle the input  by Yourself
 print_x_n_times()