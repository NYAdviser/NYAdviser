#File: Sum;AvgCalc.py
#   This program will print out the sum and average of these numbers
# I pledge my honor that I have abided by the Stevens Honor System
#by: Noah Porcelain

def main():
    print("This program will compute the the sum and average")
    print()
    
    n = int(input("How many numbers will be entered? "))
    count = 0
    sum = 0

    for i in range(n):
        count+=1
        num = float(input("Enter the numer: "))
        print(num)
        sum+= num

    avgNum = sum/count
    print("The sum of these numbers is", round(sum,2), "and the average of these numbers is", round(avgNum, 2))

main()
        
    
