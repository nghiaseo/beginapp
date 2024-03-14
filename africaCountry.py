import list
import os
import random
import msvcrt
import csv

class Player:
    def __init__(self):
        self.life = 3

    def wrong(self):
        self.life -= 1
def get_country():
    countries = []
    with open('./resource/Countries.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  
            if row['name'] not in countries and row['continent'] == 'af':              
                countries.append(row['name'].lower())
    return countries

def main():
    countries = get_country()
    guessed = []
    player = Player()
    while player.life > 0:
        os.system('cls')
        print('Life:',player.life)
        print('Guessed:',", ".join(guessed),'\n',(len(countries) - len(guessed)),'countries left')
        
        guess = input('Enter a country name in Africa : ')
        if guess.lower() in countries and guess.lower() not in guessed:
            guessed.append(guess)
            print('Correct guess')
            msvcrt.getch()
            if len(guessed) == len(countries):
                print('You win')
                msvcrt.getch()
                break
        elif guess.lower() in guessed:
            print('You already guessed that country')
            msvcrt.getch()
        else:
            print('Incorrect guess')
            player.wrong()
            msvcrt.getch()
        if player.life == 0:
            print('You lose')
            msvcrt.getch()
            break
    

    
        