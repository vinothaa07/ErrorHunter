# Print X N Times
def print_x_n_times(x, n):
    for i in range(n):
        print(x)

if __name__ == "__main__":
    x = input("Enter what you wanna print: ")
    n = int(input("Enter the number of times to print it: "))
    print_x_n_times(x, n)