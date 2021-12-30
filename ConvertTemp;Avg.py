#convert.py
#   A program to convert Celsius temps to Fahrenheit
#   n amount of times
#   Find average temperature of n temperatures
#by: Noah Porcelain

def main():
    n = int(input("How many numbers will be entered? "))
    count = 0
    sum = 0

    for i in range(n):
        count+=1
        fahrenheit = float(input("What is the Fahrenheit temperature? "))
        celsius = 5/9*(fahrenheit-32)
        print(celsius)
        sum+=1

    avgTemp = sum/count
    print("The average temperature is", avgTemp, "degrees Celsius.")
                   
main()
                   
