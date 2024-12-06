# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade):
    switch = {
        'A': "Good",
        'B': "Average",
        'C': "Poor",
        'D': "Excellent",  
        'E': "Fail"
    }
    return switch.get(grade, "Not a valid grade") 
if __name__ == "__main__":
    grade=input("Enter the grade :")
    rs = grade_description(grade)
print(rs)
    
