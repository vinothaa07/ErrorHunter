def set_operations_menu():
    while True:
        print("\n1. Union of Two Sets")
        print("2. Intersection of Two Sets")
        print("3. Difference of Two Sets")
        print("4. Check Subset")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        # Taking input and converting to sets
        set1 = set(input("Enter elements of Set 1 separated by space: ").split())
        set2 = set(input("Enter elements of Set 2 separated by space: ").split())

        if choice == 1:
            print("Union:", set1 | set2)  # Corrected union calculation using |
        elif choice == 2:
            print("Intersection:", set1 & set2)  # Corrected intersection calculation using &
        elif choice == 3:
            print("Difference:", set1 - set2)  # Corrected difference calculation using -
        elif choice == 4:
            if set1.issubset(set2):  # Corrected subset check
                print("Set 1 is a subset of Set 2")
            else:
                print("Set 1 is not a subset of Set 2")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

# Calling the function to run
set_operations_menu()
