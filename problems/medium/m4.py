def number_analysis_menu():
    print("1. Check Prime")
    print("2. Factorial")
    print("3. Fibonacci Sequence")
    print("4. Sum of Digits")
    
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid option. Please select a number between 1 and 4.")
            return
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return
 