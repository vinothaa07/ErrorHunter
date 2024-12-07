'''Write a program to reverse a given list without using built-in functions'''
def reverse_list(lst):
    return[lst[i] for i in range(-1,-len(lst)-1,-1)]

print(reverse_list([1,2,3,4,5]))