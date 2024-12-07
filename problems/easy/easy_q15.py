 
# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade):
    switch = {
 
        'B': "Good",
        'C': "Average",
        'D': "Poor",
        'A': "Excellent",  
        'F': "Fail"
 
 
    }
 
    return switch.get(grade, "Not a valid grade") 

if __name__ == "__main__":
    alp = input("Enter a grade: ").upper()
    rs = grade_description(alp)
    print(rs)
 
if __name__ == "__main__":
 
    grade = grade_description('Z')
    print(grade_description(grade):)
    
 
    rs = grade_description('Z')
    print(rs)
 