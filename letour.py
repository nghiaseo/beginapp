import msvcrt
import os

def get_schedule_as_list():
    #read the file with one record per line and separate the fields by semicolon
    list=[]
    with open('./resource/letour.txt', 'r') as file:
        for line in file:
            record = line.strip().split(';')
            entry = {'Stage':record[0],'Distance':record[1],'Start':record[2],'Finish':record[3]}
            list.append(entry)
    return list

def convert_from_km_to_miles(distance_in_km: float) -> float:
    return distance_in_km * 0.621371

def main():
    os.system('cls')
    schedule = get_schedule_as_list()

    #get longest distance stage index
    longest_distance = 0
    longest_distance_index=0
    for i in range(len(schedule)):
        if float(schedule[i]['Distance']) > longest_distance:
            longest_distance = float(schedule[i]['Distance'])
            longest_distance_index = i
    print('The longest distance stage is',schedule[longest_distance_index]['Stage'],'with',schedule[longest_distance_index]['Distance'],'km')

    #get shortest distance stage index
    shortest_distance = longest_distance
    shortest_distance_index=0
    for i in range(len(schedule)):
        if float(schedule[i]['Distance']) < shortest_distance:
            shortest_distance = float(schedule[i]['Distance'])
            shortest_distance_index = i
    print('The shortest distance stage is',schedule[shortest_distance_index]['Stage'],'with',schedule[shortest_distance_index]['Distance'],'km')

    #get average distance per stage
    total_distance = 0
    for i in range(len(schedule)):
        total_distance += float(schedule[i]['Distance'])
    average_distance = total_distance / len(schedule)
    print('The average distance per stage is',average_distance,'km')

    #total distance of tour
    print('The total distance of the tour in miles is',convert_from_km_to_miles(total_distance),'miles')

    #get travel distance from start to stage 17
    total_travel_distance = 0
    for i in range(16):
        total_travel_distance += float(schedule[i]['Distance'])
    print('The travel distance from start to stage 17 is',total_travel_distance,'km')

    #get distance from stage 17 to finish
    distance_from_stage_17_to_finish = 0
    for i in range(16,len(schedule)):
        distance_from_stage_17_to_finish += float(schedule[i]['Distance'])
    print('The distance from stage 17 to finish is',distance_from_stage_17_to_finish,'km')

    msvcrt.getch()