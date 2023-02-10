class BankAccount: 
    def __init__(self, o, b):
        self.owner = o
        self.balance = b
    
    def deposit(self): #just putting money into a bank account
        amount = float(input('Enter the amount to be deposited: '))
        self.balance+=amount
        print('You deposited: ', amount)
        
    def withdrawn(self): 
        amount = float(input('Enter the amount to be withdrawn: '))
        if self.balance >= amount: 
            self.balance-=amount
            print('You withdrew: ', amount)
        else: 
            print('You do not have enough money on balance')
        
my = BankAccount('Akzhan', 1000)

my.deposit()
my.withdrawn()
my.deposit()
my.withdrawn()
my.withdrawn()


