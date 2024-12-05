'''Generate the Fibonacci series up to n terms using a recursive function.
'''
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

n = int(input("Enter the number of terms: "))
print(fibonacci(n))
