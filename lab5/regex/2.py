import re 

string = input()

x = re.search("ab{2,3}", string)

if x: 
    print('String matches')
else: 
    print('String does not match')

