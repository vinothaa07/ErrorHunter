def string_manipulation_menu():
    print("1. Count Vowels")
    print("2. Reverse String")
    print("3. Check Palindrome")
    print("4. Replace Substring")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        s = str(input("Enter a string: "))
        vowels = "aeiouAEIOU"
        count = 0
        for char in s:
            if char in vowels:
                count += 1 
        print("Number of Vowels:", count)
    elif choice == 2:
        s = str(input("Enter a string: "))
        print("Reversed String:", s[::-1])  
    elif choice == 3:
        s = str(input("Enter a string: "))
        if s[::-1] != s:
            print("Not a Palindrome")  
        else:
            print("Palindrome")
    elif choice == 4:
        s = str(input("Enter a string: "))
        old = input("Substring to replace: ")
        new = input("Replacement substring: ")
        s=s.replace(old,new)
        print("Updated String:", s)   
    else:
        print("Invalid option")
string_manipulation_menu()
