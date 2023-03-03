import re 

string = input()

pattern = "[A-Z]{1}[a-z]+"

matches = re.findall(pattern, string)

for i in matches: 
    print(i)

    