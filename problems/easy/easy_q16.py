# Print the Sum of First and Last Array Element
def sum_first_last(arr):
    for i in range(len(arr)):
        return arr[0] + arr[-1]  
if __name__ == "__main__":
    user = [int(x) for x in (input("Enter a collection number:")).split(",")]
    # Handle the input  by Yourself
    print(sum_first_last(user))