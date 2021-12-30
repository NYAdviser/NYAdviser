#File: ConvertTemp;Warnings.py
#   This program will convert degrees Celsius to Fahrenheit
#   It will also print heat and cold warnings
#by: Noah Porcelain

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    
    # Warnings
    if fahrenheit > 100:
        print("Heat Alert")
    if fahrenheit < 0:
        print("Cold Alert")
        
main()
