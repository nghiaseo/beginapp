import msvcrt
import os

def display_menu():    
    print('1. Map')
    print('2. Book a specific seat')
    print('3. Book a seat close front')
    print('4. Book a seat close back')
    print('5. Cancel booking')
    print('6. Rest all seats')
    print('0. Exit')

def get_all_user_from_file():
    #read the file with one record per line and separate the fields by semicolon
    list=[]
    with open('./resource/user.txt', 'r') as file:
        for line in file:
            record = line.strip().split(',')
            entry = {'username':record[0],'password':record[1]}
            list.append(entry)
    return list

def authenticate_user(username,password):
    users = get_all_user_from_file()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

def login():
    os.system('cls')
    print('Login')
    username = input('Enter username : ')
    password = input('Enter password : ')
    if authenticate_user(username,password):
        return True
    else:
        return False
    


def get_map_from_file():
    #read the file with one record per line and separate the fields by semicolon
    list=[]
    with open('./resource/cinemamap.txt', 'r') as file:
        for line in file:
            record = line.strip().split(',')            
            list.append(record)
    return list

def display_map(map):    
    print('   ----Screen----','\n')
    print('  1 2 3 4 5 6 7 8')
    for ind,row in enumerate(map):
        r = []
        for seat in row:
            if seat == '0':
                r.append('O')
            else:
                r.append('X')
        print(ind+1,' '.join(r))    

def detect_consecutive_seats_of_a_seat(row,seat):
    if seat == 1:
        if map[row-1][seat] == '0' and map[row-1][seat+1] == '0':
            return True
    elif seat == 8:
        if map[row-1][seat-2] == '0' and map[row-1][seat-1] == '0':
            return True
    else:
        if map[row-1][seat-2] == '0' and map[row-1][seat-1] == '0' and map[row-1][seat] == '0':
            return True
    return False

def is_full(map):
    for row in map:
        for seat in row:
            if seat == '0':
                return False
    return True

def book_specific_seat(map):
    os.system('cls')
    display_map(map)
    row = int(input('Enter row number : '))
    seat = int(input('Enter seat number : '))

    if map[row-1][seat-1] == '0':
        map[row-1][seat-1] = '1'
        print('Seat booked successfully')
    else:
        print('Seat already booked')
    
    if not is_full(map):
        print('Do you want to book another seat? (y/n) : ')
        if input() == 'y':
           map = book_specific_seat(map)
    
    return map

def book_close_front(map):
    for row in range(1,7):
        for seat in range(1,9):
            if map[row-1][seat-1] == '0':
                map[row-1][seat-1] = '1'
                print('You have booked seat',row,seat)
                msvcrt.getch()
                return map

def book_close_back(map):
    for row in range(7,1,-1):
        for seat in range(9,1,-1):
            if map[row-1][seat-1] == '0':
                map[row-1][seat-1] = '1'
                print('You have booked seat',row,seat)
                msvcrt.getch()
                return map

def cancel_all_booking(map):
    map = get_map_from_file()
    return map

def clear_all_seats(map):
    for row in range(1,7):
        for seat in range(1,9):
            map[row-1][seat-1] = '0'
    #write the map to file
    with open('./resource/cinemamap.txt', 'w') as file:
        for row in map:
            file.write(','.join(row)+'\n')

    print('All seats are reset')
    msvcrt.getch()
    return map


def main():
    # while not login():    
    #     print('Invalid username or password')
    #     msvcrt.getch()
    
    map = get_map_from_file()    
    while True:    
        os.system('cls')        
        display_menu()
        choice = input('Enter your choice : ')
        if choice == '1':
            os.system('cls')
            display_map(map)
            msvcrt.getch()
        elif choice == '2':
            map = book_specific_seat(map)
        elif choice == '3':
            map = book_close_front(map)
        elif choice == '4':
            map = book_close_back(map)
        elif choice == '5':
            map = cancel_all_booking(map)
            print('All seats are cancelled')
            msvcrt.getch()
        elif choice == '6':
            map = clear_all_seats(map)
        elif choice == '0':
            break
        else:
            print('Invalid choice')
    pass
    