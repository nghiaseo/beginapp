import msvcrt
import os

class ATM:
    def __init__(self,banknote_20=30,banknote_10=40):        
        self.balance = banknote_20 * 20 + banknote_10 * 10
        self.capacity = self.balance
        self.banknote_20 = banknote_20
        self.banknote_10 = banknote_10
        self.action()

    def withdraw(self,amount):
        max_amount = 200
        min_amount = 10
        
        #check amount is multiple of 10
        if amount % 10 != 0:
            return 'Amount should be multiple of 10'
        #check amount is between 10 and 200
        if amount < min_amount or amount > max_amount:
            return 'Amount should be between 10 and 200'
        #check amount is less than balance
        if amount > self.balance:
            return 'ATM balance is less than amount'
        #check amount is less than capacity
        if amount > self.capacity:
            return 'Your amount is more than ATM capacity'
        
        #check enough banknotes available to withdraw
        banknote_20_needed = amount // 20
        if banknote_20_needed > self.banknote_20:
            banknote_20_needed = self.banknote_20
        banknote_10_needed = (amount - banknote_20_needed * 20) // 10
        if banknote_10_needed > self.banknote_10:
            banknote_10_needed = self.banknote_10
        if banknote_20_needed * 20 + banknote_10_needed * 10 < amount:
            return 'ATM does not have enough banknotes'
        else:
            self.banknote_20 -= banknote_20_needed
            self.banknote_10 -= banknote_10_needed
            self.balance -= banknote_20_needed * 20 + banknote_10_needed * 10
            return f'You have withdrawn {banknote_20_needed * 20 + banknote_10_needed * 10}'
        
    def action(self):
        while True:
            os.system('cls')
            print('ATM balance:',self.balance)
            print('ATM capacity:',self.capacity)
            print('Banknote 20:',self.banknote_20)
            print('Banknote 10:',self.banknote_10)
            amount = input('Enter amount to withdraw or type exit :')
            if amount == 'exit':
                break
            else:
                if amount.isdigit():
                    print(self.withdraw(int(amount)))
                else:
                    print('Invalid amount')
            msvcrt.getch()
        
        
    

    
