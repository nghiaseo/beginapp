import list
import os
import generateIP
import extractUrl
import myUpperCase
import eggcode
import cardWar
import goals
import africaCountry

list_changllenge = [
    "Generate IP Address",
    "Extract URL",
    "Upper Case",
    "Egg Code",
    "Cards War",
    "Goals scored by each team in World Cup",
    "Africa Countries",
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
        case _:
            print("Invalid key")
