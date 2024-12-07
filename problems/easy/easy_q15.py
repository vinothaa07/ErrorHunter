# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade):
    switch = {
 
        'A': "Good",
        'B': "Average",
        'C': "Poor",
        'D': "Excellent",  
        'E': "Fail"
 
    }
  
if __name__ == "__main__":
    rs = grade_description('Z')
    print(rs)
 
