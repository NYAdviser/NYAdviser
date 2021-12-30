#File: RootsQuadEquat.py
#   This program computes the real roots of a quadratic equation
#   Illistrates use of the math library
#by: Noah Porcelain
import math

def main():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        discRoot = math.sqrt(b**2 - 4 * a * c)
        
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        
        print("\nThe solutions are:", root1, root2)
        
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No Real Roots")
            
        else:
            print("Invalid coefficient given")
            
    except:
        print("\nSomething went wrong, sorry!")
        
main()
