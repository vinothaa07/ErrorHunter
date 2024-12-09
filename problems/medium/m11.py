import math

def circle_area_perimeter():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    print(f"Area of the circle: {area:.2f}")
    print(f"Perimeter (Circumference) of the circle: {perimeter:.2f}")

def rectangle_area_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area of the rectangle: {area:.2f}")
    print(f"Perimeter of the rectangle: {perimeter:.2f}")

def triangle_area_perimeter():
    a = float(input("Enter the first side of the triangle: "))
    b = float(input("Enter the second side of the triangle: "))
    c = float(input("Enter the third side of the triangle: "))
    
    # Calculate the perimeter
    perimeter = a + b + c
    # Calculate the area using Heron's formula
    s = perimeter / 2  # semi-perimeter
    try:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Area of the triangle: {area:.2f}")
        print(f"Perimeter of the triangle: {perimeter:.2f}")
    except ValueError:
        print("Invalid triangle dimensions! Cannot calculate area.")

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate for Circle")
        print("2. Calculate for Rectangle")
        print("3. Calculate for Triangle")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            circle_area_perimeter()
        elif choice == "2":
            rectangle_area_perimeter()
        elif choice == "3":
            triangle_area_perimeter()
        elif choice == "4":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the program
main()
