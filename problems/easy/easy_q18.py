# Print Last Character of String
def last_string(s):
    return s[-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    if s:
        print("The last character is:", last_string(s))
    else:
        print("The string is empty.")