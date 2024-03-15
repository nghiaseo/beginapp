import msvcrt
import os

def get_menu_as_list():
    #read the file with one record per line and separate the fields by semicolon
    list=[]
    with open('./resource/food-menu.txt', 'r') as file:
        for line in file:
            record = line.strip().split(';')
            entry = {'Code':record[0],'Item':record[1],'Price':record[2]}
            list.append(entry)
    return list

def main():
    os.system('cls')
    menu = get_menu_as_list()
    total = 0
    ordered = []
    while True:
        os.system('cls')
        print('Menu','\n')
        
        for item in menu:
            print(item['Code'],'\t',item['Item'],'\t',item['Price'])
        print("you ordered:",','.join(ordered))
        print('Total bill:',total)

        code = input('Enter the code of the item you want to order or type exit : ')
        if code == 'exit':
            break
        found = False
        for item in menu:
            if item['Code'] == code.upper():
                total += float(item['Price'])
                found = True
                ordered.append(item['Item'])
                break
        if not found:
            print('Invalid code')
            msvcrt.getch()        
        
    os.system('cls')
    print('Thank you for your order')
    msvcrt.getch()    