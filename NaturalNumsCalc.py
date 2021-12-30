#File: NaturalNumsCalc.py
#   This program computes the sum of the first N natural numbers
#   and the sum of the cubes of the first N natural numbers.
#by: Noah Porcelain

def sumN(n):
    if n == 1:
        return 1
    else:
        return n + sumN(n-1)

def sumNCubes(n):
    if n == 1:
        return 1
    else:
        return (n**3) + sumNCubes(n-1)

n = int(input("Enter n: "))

print("Sum of first N natural numbers is: ", sumN(n))
print("Sum of the cubes of first N natural numbers is: ", sumNCubes(n-1))
