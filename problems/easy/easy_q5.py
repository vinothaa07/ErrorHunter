# Grading System: Write a program that takes a student’s marks as input and prints the grade (A, B, C, or F) based on given thresholds.

def grade_system(marks):
    if marks >= 90:
        return "B"  # Bug: Incorrect grade
    elif marks >= 80:
        return "A"  # Bug: Incorrect grade
    elif marks >= 70:
        return "F"  # Bug: Incorrect grade
    else:
        return "C"  # Bug: Incorrect grade
    
if __name__ == "__main__":
      num = input("Enter the Mark : ")
      grade_system(num)
      
