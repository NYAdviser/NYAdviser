#File: 5-day_moving_avg.py
#   A simple program to calculate the 5-day simple moving average
# by: Noah Porcelain

def main():
    print("This program calculates the 5-day simple moving aveage")
    print("of a security")

    Day1 = eval(input("Enter the price on day 1: "))
    Day2 = eval(input("Enter the price on day 2: "))
    Day3 = eval(input("Enter the price on day 3: "))
    Day4 = eval(input("Enter the price on day 4: ")) 
    Day5 = eval(input("Enter the price on day 5: "))
   
    for i in range (5):
          movingavg = (Day1 + Day2 + Day3 + Day4 + Day5) / 5

    print("The 5-day simple moving average of the security is:", movingavg)

main()
