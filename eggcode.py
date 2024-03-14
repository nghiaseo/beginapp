import msvcrt
import os
import myUpperCase
import csv

upper = myUpperCase.upper_case
validCodes = ['0','1','2','3']

def eggCode():    
    os.system('cls')
    print("Egg code")    
    valid = False
    while valid == False:
        egg_code = input('Enter your egg code or Enter to exit : ').replace(" ", "")      

        if len(egg_code) == 0:
            break
        elif len(egg_code) < 7 or egg_code[0] not in validCodes:
            print("Invalid egg code")
        else:
            os.system('cls')
            extracEggCode(upper(egg_code))
            valid = True    
    msvcrt.getch()

def extractCountry(code):    
    with open('./resource/Countries.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if code == row['ISO alpha 2']:
                return row['name']
    return 'Unknown Country'

def extractMethod(code):    
    match code:
        case '0':
            return "Organic"
        case '1':
            return "Free Range"            
        case '2':
            return "Barn"            
        case '3':
            return "Cage"
        case _:
            print("Invalid egg code")    



def extracEggCode(code):
    egg_code = {}
    egg_code['method'] = extractMethod(code[0])
    print('Farming method :',egg_code['method'])
    egg_code['country'] = extractCountry(code[1:3])    
    print('Country of Origin :',egg_code['country'])
    egg_code['farm'] = code[3:len(code)]
    print('Farm ID :',egg_code['farm'])



    

