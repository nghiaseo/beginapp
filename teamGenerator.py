import list
import os
import random
import msvcrt
import csv

class Pupil:
    def __init__(self, name):        
        first_name = name.split(",")[0]
        last_name = name.split(",")[1]        
        self.name = f'{first_name} {last_name}'
        self.team = None

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

def get_pupils_from_file():
    pupils = []
    with open('./resource/class.txt', 'r') as file:
        for line in file:
            pupils.append(Pupil(line.strip()))
    return pupils

def generate_teams(pupils=[]):
    os.system('cls')
    teams=[]

    number_of_team = input('How many teams do you want to generate (1 < number of teams < 7):')
    while not number_of_team.isdigit() and (int(number_of_team) < 1 or int(number_of_team) > 7):
        os.system('cls')
        number_of_team = input('Please enter a valid number :')

    number_of_team = int(number_of_team)
    number_of_members = len(pupils) // number_of_team
    for i in range(number_of_team):
        team = Team(f'Team {i+1}')
        for _ in range(number_of_members):
            member = random.choice(pupils)
            team.add_member(member)
            pupils.remove(member)
        teams.append(team)

    for team in teams:
        if len(pupils) > 0:
            member = random.choice(pupils)
            team.add_member(member)
            pupils.remove(member)

    return teams

def pick_random_pupil(pupils):
    return random.choice(pupils)

def get_record_of_give_present(pupils):
    list_of_give_present = pupils.copy()
    list_of_receive_present = pupils.copy()
    record_of_give_present = []
    for pupil in list_of_give_present:
        valid_receivers = list_of_receive_present.copy()

        #find the pupil in the valid_receivers list and remove it
        for receiver in valid_receivers:
            if receiver.name == pupil.name:
                valid_receivers.remove(receiver)
        receive_present = random.choice(valid_receivers)        
        record_of_give_present.append((pupil.name+' give a gift to '+ receive_present.name))
        list_of_receive_present.remove(receive_present)
    return record_of_give_present

def main():
    os.system('cls')
    pupils = get_pupils_from_file()        
    teams = []
    not_picked = pupils.copy()
    while True:
        os.system('cls')        
        print('1. Generate teams')
        print('2. Pick pupil',(f' ({len(not_picked)} left)' if len(not_picked) > 0 else ''))
        print('3. Secret Santa')
        print('0. Exit')
        key = input('Enter your choice : ')
        match key:
            case '0':
                break
            case '1':
                teams = generate_teams(pupils)
                for team in teams:
                    print(team.name)
                    for member in team.members:
                        print(member.name)
                    print('-----------------')    
                msvcrt.getch()
            case '2':
                if len(not_picked) == 0:
                    print('All pupils have been picked')
                    msvcrt.getch()
                    continue
                else:
                    picked_pulil= pick_random_pupil(not_picked)
                    not_picked.remove(picked_pulil)            
                    print("Pupil picked is :", picked_pulil.name)    
                    msvcrt.getch()
            case '3':
                record_of_give_present = get_record_of_give_present(pupils)
                for record in record_of_give_present:
                    print(record)
                msvcrt.getch()
                pass
            case _:
                print('Invalid key')
                msvcrt.getch()

    