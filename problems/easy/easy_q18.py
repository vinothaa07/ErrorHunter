# Print Last Character of String
def last_char_of_string(s):
    return s[-1]  # Bug: Fetches second-to-last character instead of last
if __name__ == "__main__":
   string=input("enter the string:")
   if string:
      print("the last character of the string:",last_char_of_string(string))
   else:
      print("invalid")
 