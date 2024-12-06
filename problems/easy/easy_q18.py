# Print Last Character of String
def last_char_of_string(s):
    return s[-1]  # Bug: Fetches second-to-last character instead of last
if __name__ == "__main__":
 # Handle the input  by Yourself
 str=input("Enter the string :")
last_str= last_char_of_string(str)
print(last_str)