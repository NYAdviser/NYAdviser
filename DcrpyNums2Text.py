#numbers2text_dcrypt.py
#   Decrypts the numbers to text
#by: Noah Porcelain

def main():

    inputString = input("Enter encrypted Unicode chracters: ")

    message = []

    for i in inputString.split():

        codeNum = int(i)
        codeNum = codeNum - 5
        message.append(chr(codeNum))
        message_out = "".join(message)

    print("\nThe decoded message is: ", message_out)

main()
