import re

string = input() 

x = re.search("ab*", string)

if x: 
    print("String matches")
else: 
    print("String does not match")

    