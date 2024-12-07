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
 
    return switch.get(day)
if __name__ == "__main__":
    day=int(input("Enter day number:"))
    xcd = day_of_week(day)
    print(xcd)
 
    
    
    return switch.get(day, "Invalid day")
 