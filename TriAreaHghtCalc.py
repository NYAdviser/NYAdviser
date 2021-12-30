#File: TriAreaHghtCalc.py
#   This program determines the area and height (h) of the triangle
#by: Noah Porcelain

import math

def main():
    print("This program determines the area and heigh (h) of the triangle")
    print()

    s = float(input("Enter the length of the side in meters: "))
    b = float(input("Enter the length of the base in meters: "))
    a = float(input("Enter the angle θ in degrees: "))

    x = math.sin(math.radians(a))

    area = (s * b * x)/2
    height = 2*area/b

    print("The area is", round(area, 4) , "and the height is", round(height, 4))

main()
