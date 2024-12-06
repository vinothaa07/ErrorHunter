# Print X N Times
def print_x_n_times(n):
    for i in range(0, n):  # Bug: Loop runs one less time than expected
        print("x")
if __name__ == "__main__":
 # Handle the input  by Yourself
 num=int (input(" Enter a N times :"))
 print_x_n_times(num)