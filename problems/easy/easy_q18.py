# Print Last Character of String
def last_char_of_string(s):
    return s[-2]  # Bug: Fetches second-to-last character instead of last
if __name__ == "__main__":
 # Handle the input  by Yourself
     s=[7,8,9,6]
     print( last_char_of_string(s))