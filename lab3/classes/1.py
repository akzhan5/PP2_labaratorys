class StringOp: 
    def __init__(self): 
        self.string=''

    def getString(self): 
        self.string = input()

    def printString(self): 
        print(self.string.upper())


k = StringOp()
k.getString()
k.printString()

