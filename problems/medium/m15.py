'''Write a program to check if a number is an Armstrong number (e.g., 153  = 1^3 + 5^3 + 3^3 ) .'''

n=input("Enter Number:")
c=0
def arm(n):
   for i in n:
      c+=int(i)**len(n)
   if c==int(n):
      print("It is Armstrong number")
   else:
      print("It is not Armstrong Number")

arm(n)
