#File: NumFactorialCalculator.py
#  This program returns the number factorial.
#by: Noah Porcelain

n = int(input("What number factorial do you want? "))

def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact = fact * i
        
    return fact

print(factorial(n))
