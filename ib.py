import sys
class Customer:
    bankname='State Bank Of India'

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('The balance after deposit:',self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient Funds.. cant perform this operation')
            sys.exit()
        self.balance=self.balance-amount
        print('the balance after withdraw:',self.balance)

print('Welcome to',Customer.bankname)
name=input('Enter your Name:')
c=Customer(name)
while True:
    print('d-Deposit \nw-withdraw \ne-Exit')
    option=input('chosse your option:').lower()
    if option=='d' or option=='D':
        amount=float(input('Enter amount to deposit:'))
        c.deposit(amount)

    elif option=='w':
        amount=float(input('Enter amount to withdraw:'))
        c.withdraw(amount)

    elif option=='e':
        print('Thanks for visit bank')
        sys.exit()
    else:
        print('Invalid option.. Please choose valid option')
        
