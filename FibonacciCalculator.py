#File: FibonacciCalculator.py
#   This program outputs n fibonacci numbers.
#by: Noah Porcelain

n = int(input("How many fibonacci numbers do you want? "))

def fib(n):
    a = 0
    b = 1
    
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fib(n)
