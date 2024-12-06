'''Write a program to check if a number is an Armstrong number (e.g., 153  = 1^3 + 5^3 + 3^3 ) .'''
a=input("Enter Number:")
def Arms(a):
   e=0
   for i in a:
      c=int(i)
      d=c*c*c
      e+=d
   return e

<<<<<<< HEAD
def sum(n):
   i = count_digits(n)
   s = 0
   temp = n
   while temp > 0:
      digit = temp%10
      temp//= 10
      s += pow(digit,i)
   return s


num = 1634

 
s = sum(num)

 
if s == num:
   print('Given number is an Armstrong Number')
=======
b=Arms(a)
f=int(a)
if b==f:
   print(b,"is an Armstrong Number")
>>>>>>> 246833991f7068b3554261749a57001bddeaec6b
else:
   print(b,"is not An Armstrong Number")