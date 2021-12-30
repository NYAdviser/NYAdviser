#File: TimeCalculator.py
#   This program converts the number of days into years, weeks, and days
#by: Noah Porcelain

import math

def main():
    print("This program converts the number of days into years, weeks, and days")
    print()

    days = int(input("How many days? "))

    Years = days // 365
    w = days % 365

    Weeks = w // 7
    d = w % 7

    Days = d % 7

    print("The number of years: ", Years)
    print("The number of weeks: ", Weeks)
    print("The number of days: ", Days)

main()
