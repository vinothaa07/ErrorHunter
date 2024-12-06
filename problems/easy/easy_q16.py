# Print the Sum of First and Last Array Element
def sum_first_last(arr):
    if len(arr) < 2:
        return "Array must have at least two characters."
    return arr[0] + arr[-1]

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    result = sum_first_last(arr)
    print("The sum is:", result)