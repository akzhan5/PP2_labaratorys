import datetime

tod = datetime.datetime.now()
yes = datetime.datetime(int(tod.year), int(tod.month), int(tod.day)-1)
tom = datetime.datetime(int(tod.year), int(tod.month), int(tod.day)+1)


print(yes.strftime("%x"))
print(tod.strftime("%x"))
print(tom.strftime("%x"))





