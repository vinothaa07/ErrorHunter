# Check Even or Odd: Write a program to check if a given number is even or odd.

num = int(input("Enter a number: "))
if num == 0:
   print("0 is neither odd nor even")
elif (num % 2) != 0:
   print("{0} is Odd".format(num))
else:
   print("{0} is Even".format(num))
