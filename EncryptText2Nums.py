#File: EnryptText2Nums.py
#   Encrypts text to numbers
#by: Noah Porcelain

def main():

    message = input("Enter message to encode: ")
    print("\nHere is the encrypted message: ")
        
    for i in message:
        x = ord(i)
        print("", x + 5, end = "")

    print() #black line befroe prompt

main()
