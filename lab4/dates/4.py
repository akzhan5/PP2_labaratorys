from datetime import datetime

d1 = input()
d2 = input()

d1 = datetime.strptime(d1, "%Y %m %d")
d2 = datetime.strptime(d2, "%Y %m %d")

if d1>d2: 
    differ = d1 - d2 
else: 
    differ = d2 - d1 

print("the difference between 2 dates in seconds is ", differ.total_seconds())















