import re

string = input() 

pattern = "[a-z]_[a-z]"

matches = re.findall(pattern, string)

for i in matches: 
    print(i)

    
