import re

string = "myCamelCase?"

pattern = "[A-Z]"

matches = re.split(pattern, string)

for i in matches: 
    print(i) 


