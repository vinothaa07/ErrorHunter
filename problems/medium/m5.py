def matrix_operations_menu():
    print("1. Add Matrices")
    print("2. Multiply Matrices")
    print("3. Transpose Matrix")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows, cols = map(int, input("Enter rows and columns: ").split())
        mat1 = [[int(x) for x in input("Enter elements of matrix 1 (row-wise): ").split()] for _ in range(rows)]
        mat2 = [[int(x) for x in input("Enter elements of matrix 2 (row-wise): ").split()] for _ in range(rows)]
        result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]  # Corrected to addition
        print("Resultant Matrix:", result)
    elif choice == 2:
        rows1, cols1 = map(int, input("Enter rows and columns for matrix 1: ").split())
        rows2, cols2 = map(int, input("Enter rows and columns for matrix 2: ").split())
        if cols1 != rows2:
            print("Matrix multiplication not possible (incompatible dimensions)")
            return
        mat1 = [[int(x) for x in input("Enter elements of matrix 1 (row-wise): ").split()] for _ in range(rows1)]
        mat2 = [[int(x) for x in input("Enter elements of matrix 2 (row-wise): ").split()] for _ in range(rows2)]
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]  # Corrected dimensions
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):  # Iterate through common dimension
                    result[i][j] += mat1[i][k] * mat2[k][j]   
        print("Resultant Matrix:", result)
    elif choice == 3:
        rows, cols = map(int, input("Enter rows and columns: ").split())
        mat = [[int(x) for x in input("Enter elements of matrix (row-wise): ").split()] for _ in range(rows)]
        transpose = [[mat[j][i] for j in range(rows)] for i in range(cols)]  # Corrected transpose logic
        print("Transpose:", transpose)
    else:
        print("Invalid option")
            for j in range(cols):
                transpose[i][j] = mat[j][i]  
        print("Transpose:", transpose)
    else:
        print("Invalid option")
