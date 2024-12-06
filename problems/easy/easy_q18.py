# Print Last Character of String
def last_char_of_string(s):
    last=s[-1]
    print(last)
    return last   # Bug: Fetches second-to-last character instead of last
if __name__ == "__main__":
 # Handle the input  by Yourself
 string=input("Enter a string:")
 last_char_of_string(string)