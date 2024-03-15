import list
import os
import random
import msvcrt
import csv

def convert_from_light_years_to_km(distance_in_light_years: float) -> float:
    return distance_in_light_years * 9.461e+12

def convert_from_km_to_light_years(distance_in_km: float) -> float:
    return distance_in_km / 9.461e+12

def year_to_seconds(year: float) -> float:
    return year * 365 * 24 * 60 * 60

def main():
    os.system('cls')
    duration =year_to_seconds(convert_from_km_to_light_years(5e+8))
    print('It will take',duration,'seconds to travel from Rosetta to Earth')
    alpha_centauri = convert_from_light_years_to_km(4.24)
    print('Alpha Centauri is',alpha_centauri,'km away from Earth')
    barnards_star = convert_from_light_years_to_km(5.96)
    print('Barnard\'s Star is',barnards_star,'km away from Earth')
    luhman_16 = convert_from_light_years_to_km(6.59)
    print('Luhman 16 is',luhman_16,'km away from Earth')
    wise_0855 = convert_from_light_years_to_km(7.2)
    print('WISE 0855-0714 is',wise_0855,'km away from Earth')    
    wolf_359 = convert_from_light_years_to_km(7.78)
    print('Wolf 359 is',wolf_359,'km away from Earth')
    msvcrt.getch()