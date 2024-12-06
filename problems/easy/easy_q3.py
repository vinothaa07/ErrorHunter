# Leap Year or Not: Write a program to determine whether a given year is a leap year.
def is_leap_year(year):
<<<<<<< HEAD
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:   
        return "Leap Year"
    else:
         return "Not a Leap Year"
=======
 
    if year % 4 == 0:
       if year % 100 == 0:
           return "Not a Leap Year"
       if year % 400 == 0:
            return "Leap Year" 
       return "Leap Year"
 
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:   
        return "Leap Year"   
    return "Not a Leap Year"
 
>>>>>>> c39895b92dbcd0dd59250c4268a660b41d857e3d
if __name__ == "__main__":
    
    num = int(input("Enter the number :"))
    res = is_leap_year(num)
    print(res)