import list
import os
import generateIP
import extractUrl
import myUpperCase
import eggcode
import cardWar
import goals
import africaCountry
import teamGenerator
import spaceMission
import letour
import atm
import orderingSystem
import cinemaBooking

list_changllenge = [
    "Generate IP Address",
    "Extract URL",
    "Upper Case",
    "Egg Code",
    "Cards War",
    "Goals scored by each team in World Cup",
    "Africa Countries",
    "Team Generator",
    "Space Mission",
    "Le Tour de France",
    "ATM Machine",
    "Ordering System",
    "Cinema Booking System",
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
            myUpperCase.Ucase()
        case '4':
            eggcode.eggCode()
        case '5':
            cardWar.Game()
        case '6':
            goals.Goals()
        case '7':
            africaCountry.main()
        case '8':
            teamGenerator.main()
        case '9':
            spaceMission.main()
        case '10':
            letour.main()
        case '11':
            atm.ATM()
        case '12':
            orderingSystem.main()
        case '13':
            cinemaBooking.main()
        case _:
            print("Invalid key")
