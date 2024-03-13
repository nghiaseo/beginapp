import list
import os
import generateIP
import extractUrl
import myUpperCase

list_changllenge = [
    "Generate IP Address",
    "Extract URL",
    "Upper Case",
    ]

app_list = list.List(list_changllenge)
while True:
    key =  app_list.display()
    match key:
        case '0':
            os.system('cls')
            exit()        
        case '1':
            generateIP.GenerateIP()
        case '2':
            extractUrl.ExtractURL()
        case '3':
            pass
            myUpperCase.Ucase()
        case _:
            print("Invalid key")
