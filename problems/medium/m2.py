def array_operations_menu():
    print("1. Sum of Array")
    print("2. Largest Element")
    print("3. Smallest Element")
    print("4. Sort Array")

    choice = int(input("Enter your choice: "))

 
    arr = list(map(int, input("Enter array elements separated by space: ").split(sep=",")))
 

 
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
 
    if choice == 1:
 
 
        print("Sum:", sum(arr) * 2)   
 
 
        print("Sum:", sum(arr) )   
 
        print("Sum:", sum(arr))   
 
 
 
        print("Sum:", sum(arr))  
 
 
    elif choice == 2:
        print("Largest Element:", max(arr))  
    elif choice == 3:
 
        print("Smallest Element:", min(arr))   
    elif choice == 4:
        print("Sorted Array:", sorted(arr) )
    else:
        print("Invalid option")
array_operations_menu()
 
        print("Smallest Element:", min(arr))  
    elif choice == 4:
 
 
        print("Sorted Array:",sorted.arr) 
    else:
        print("Invalid option")
 
 

if __name__ == "__main__":
    array_operations_menu()
 
 
array_operations_menu()
 
   
 
 