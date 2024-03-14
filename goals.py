import list
import os
import random
import msvcrt
import csv
import time

list_task = [
    "Details of random 2 countries",
    "Guess which of the two countries scored the most goals",
    "List the total number of goals scored for each country",    
    "Which country scored the most goals?",
    "Which player scored the most goals?"
]

def sort_by_goals(record):    
    return int(record['TotalGoals'])

def sort_by_player_goals(record):    
    return int(record['Goals'])

def list_total_goals_for_country(list_record):
    countries = []
    for record in list_record:
        if record['Country'] not in countries:
            countries.append(record['Country'])
    #list total goals for each country
    total_goals_by_country = []
    for country in countries:
        total_goals = 0
        for record in list_record:
            if record['Country'] == country:
                total_goals += int(record['Goals'])
        total_goals_by_country.append({'Country':country,'TotalGoals':total_goals})
    return total_goals_by_country

class Goals:
    def __init__(self):
        self.list_record = []
        task_list = list.List(list_task)        
        with open('./resource/goals.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=';',fieldnames=['Name','Country','Goals'])
            for row in reader:                
                record = {}
                record['Name'] = row['Name']
                record['Country'] = row['Country']
                record['Goals'] = row['Goals']
                self.list_record.append(record)              
        while True:
            key =  task_list.display()
            self.excute_task(key)
            if key == '0':
                break


    def excute_task(self,key):
        match key:
            case '0':
                os.system('cls')                
            case '1':
                os.system('cls')                
                print("Details of random 2 countries")
                index1 = random.randint(0, len(self.list_record)-1)
                index2 = random.randint(0, len(self.list_record)-1)
                while index1 == index2 and self.list_record[index1]['Country'] == self.list_record[index2]['Country']:
                    index2 = random.randint(0, len(self.list_record)-1)
                print('Country :', self.list_record[index1]['Country'])
                print('Player :', self.list_record[index1]['Name'])
                print('Goals :', self.list_record[index1]['Goals'],'\n')
                print('Country :', self.list_record[index2]['Country'])
                print('Player :', self.list_record[index2]['Name'])
                print('Goals :', self.list_record[index2]['Goals'],'\n')
                
                print("Press any key to continue...")
                msvcrt.getch()                
            case '2':
                os.system('cls')                
                print("Guess which of the two countries scored the most goals")
                guess1 = input('Enter the name of 1st country : ')
                guess2 = input('Enter the name of 2nd country : ')
                
                #list total goals for each country
                total_goals_by_country = list_total_goals_for_country(self.list_record)

                total_goals_by_country.sort(key=sort_by_goals,reverse=True)

                if(total_goals_by_country[0]):
                    print('Which country scored the most goals?')
                    print('1.',total_goals_by_country[0]['Country'],'with',total_goals_by_country[0]['TotalGoals'],'goals')
                if(total_goals_by_country[1]):
                    print('Second most goals scored by')
                    print('2.',total_goals_by_country[1]['Country'],'with',total_goals_by_country[1]['TotalGoals'],'goals')
                
                if guess1.upper() in [total_goals_by_country[0]['Country'].upper(),total_goals_by_country[1]['Country'].upper()] and guess2.upper() in [total_goals_by_country[0]['Country'].upper(),total_goals_by_country[1]['Country'].upper()]:
                    print('You guessed correctly')
                elif guess1.upper() in [total_goals_by_country[0]['Country'].upper(),total_goals_by_country[1]['Country'].upper()] or guess2.upper() in [total_goals_by_country[0]['Country'].upper(),total_goals_by_country[1]['Country'].upper()]:
                    print('You guessed 1 correctly')
                else:
                    print('You guessed incorrectly')

                print("Press any key to continue...")
                msvcrt.getch()        
            case '3':
                os.system('cls')                
                print("List the total number of goals scored for each country")   
                msvcrt.getch()                                   

                #list total goals for each country
                list_total_goals_by_country1 = list_total_goals_for_country(self.list_record)
                os.system('cls')            
                
                for record in list_total_goals_by_country1:
                    print(record['Country'],':',record['TotalGoals'])
                    time.sleep(0.1)


                print("Press any key to continue...")
                msvcrt.getch()                    
            case '4':
                os.system('cls')                                
                 #list total goals for each country
                total_goals_by_country = list_total_goals_for_country(self.list_record)

                total_goals_by_country.sort(key=sort_by_goals,reverse=True)

                if(total_goals_by_country[0]):
                    print('Which country scored the most goals?')
                    print(total_goals_by_country[0]['Country'],'with',total_goals_by_country[0]['TotalGoals'],'goals')

                print("Press any key to continue...")
                msvcrt.getch()
            case '5':
                os.system('cls')                
                print("Which player scored the most goals?")
                self.list_record.sort(key=sort_by_player_goals,reverse=True)
                print(self.list_record[0]['Name'],'from',self.list_record[0]['Country'],'with',self.list_record[0]['Goals'],'goals')
                print("Press any key to continue...")
                msvcrt.getch()
            case _:
                os.system('cls')                
                print("Invalid key")