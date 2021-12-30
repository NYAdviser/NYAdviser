#File: FactorialCalculator.py
#   Program to compute the factorial of a number
#   Illustrates a for loop with an accumulator
#by: Noah Porcelain

def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()
