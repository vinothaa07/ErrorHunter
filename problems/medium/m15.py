'''Write a program to check if a number is an Armstrong number (e.g., 153  = 1^3 + 5^3 + 3^3 ) .'''
def count_digits(n):
   i = 0
   while n > 0:
      n //= 10
      i += 1
   return i

def sum(n):
   i = count_digits(n)
   s = 0
<<<<<<< HEAD
   temp = n
   while temp > 0:
      digit = temp%10
      temp //= 10
=======
   temp=n
   while temp > 0:
      digit = temp%10
      temp//= 10
>>>>>>> 02784d8502651a47ee9509d1b7a54fc0fd48ff76
      s += pow(digit,i)
   return s


num = 1634

 
s = sum(num)

 
if s == num:
   print('Given number is an Armstrong Number')
else:
   print('Given number is not an Armstrong Number')

