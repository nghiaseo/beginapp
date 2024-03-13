import os
import msvcrt

class Ucase:
    def __init__(self):
        os.system('cls')                
        print("Upper Case")
        text = input("Enter text or Enter to back: ")
        if(text == ""):
            return
        print(self.upper_case(text))
        print("Press any key to continue...")
        msvcrt.getch()
        
    def upper_case(self, text):                
        upperString=''
        for i in text:
            if ord(i) >= 97 and ord(i) <= 122:
                upperString +=chr(ord(i)-32)
            else:
                upperString += i
        return str(upperString)