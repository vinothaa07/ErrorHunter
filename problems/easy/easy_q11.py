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
    
    
    return switch.get(day, "Invalid day")

if __name__ == "__main__":
 
    try:
        day = int(input("Enter a number (1-7) to get the day of the week: "))
        
       
        result = day_of_week(day)
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")
