#
def day_of_week(day):
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
 
    if day < 1 or day > 7:
        return "Invalid day"
    return switch[day]
if __name__ == "__main__":
    xcd = day_of_week(32)
    print(xcd)

    
 
    return switch[day]   
if __name__ == "__main__":
 
    day=int(input("Enter the number : "))
    if 0<day<8:
        xcd = day_of_week(day)
        print(xcd)
    else:
        print("Enter a valid input :")
 
    day=int(input("Enter The Number:"))
    if str(day) in "1234567":
        xcd = day_of_week(day)
        print(xcd)
    else:
        print("Enter Valid Input")
 
    
