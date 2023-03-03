import re 

string = input() 

pattern = "a.+b"

x = re.search(pattern, string) 

if x: 
    print("String matches")
else: 
    print("String does not match")

    
