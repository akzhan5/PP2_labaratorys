import datetime 

tod = datetime.datetime.now() 
d = tod.day
m = tod.month
y = tod.year()
days_ago = datetime.datetime(y, m, d-5)

print("Today's date is ", tod.strftime("%x"))
print("5 days ago was ", days_ago.strftime("%x"))

