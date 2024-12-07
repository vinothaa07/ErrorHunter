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
 
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
 
 
    
    if choice > 0:
        n = int(input("Enter a number: "))
        if choice == 1:
            is_prime = True
            for i in range(2, n):  
                if n % i == 0:
                    print(" Not Prime")
                    break
            else:    
                print("Prime")   
        elif choice == 2:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i   
            print("Factorial:", factorial)
        elif choice == 3:
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[-1] + fib[-2])
            print("Fibonacci Sequence:", fib[:-1])  
        elif choice == 4:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10   
            print("Sum of Digits:", total)
        else:
            print("Invalid option")
    else:
        print("Enter a positive choice")
        

    n = int(input("Enter a number: "))
 
    if n < 0:
        print("Please enter a non-negative integer.")
        return

    if choice == 1:  # Check if Prime
        if n < 2:
            print("Not prime")
        else:
            is_prime = True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            print("Prime" if is_prime else "Not prime")

    elif choice == 2:  # Factorial
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"Factorial: {factorial}")

    elif choice == 3:  # Fibonacci Sequence
        if n <= 0:
            print("Fibonacci Sequence: []")
        elif n == 1:
            print("Fibonacci Sequence: [0]")
        else:
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[-1] + fib[-2])
            print("Fibonacci Sequence:", fib)

    elif choice == 4:  # Sum of Digits
        total = 0
        original_n = n
        while n > 0:
            total += n % 10
 
            n //= 10
        print(f"Sum of Digits of {original_n}: {total}")

number_analysis_menu()


             n //= 10   
        print("Sum of Digits:", total)
    else:
        print("Invalid option")
 
number_analysis_menu()
 
