def number_analysis_menu():
    print("1. Check Prime")
    print("2. Factorial")
    print("3. Fibonacci Sequence")
    print("4. Sum of Digits")
    choice = int(input("Enter your choice: "))

    n = int(input("Enter a number: "))

    if choice == 1:
        a=0
        if n<1:
            print("not a prime")
        elif n==2:
            print("prime")
        else:
            a=int(n**0.5)+1
            for i in range(2,a):
                if (n%i==0):
                    print("not a prime")
                    break
    elif choice == 2:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i   
        print("Factorial:", factorial)
    elif choice == 3:
        fib = [0, 1]
        for i in range(1,n):
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
number_analysis_menu()
