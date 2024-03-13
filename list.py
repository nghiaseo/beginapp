import os
class Item:
    def __init__(self, key, name):
        self.name = name
        self.key = key
    

class List:
    def __init__(self,items = []):
        self.items = []
        for i in range(len(items)):
            self.items.append(Item(i+1,items[i]))
        self.items.append(Item(0,'Exit'))    
    
    def display(self):
        os.system('cls')
        print('List of Challenges')
        for i in self.items:
            print(str(i.key)+'.',i.name)
        return input('Enter number to select challenge: ')
        
        