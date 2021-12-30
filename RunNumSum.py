#File: RunNumSum.py
#   This program returns the sum of all numbers from 1 to n
#by: Noah Porcelain

def main():
    print("This program returns the sum of all numbers from 1 to n")

    n = int(input("Enter a number: "))

    sum = 0

    for i in range (n+1):
            sum += i

    print("The sum of all the numbers from 1 to n is", sum)

main()
