import re 

def change(mObj): 
    return mObj.group("g1") + " " + mObj.group("g2")

string = "WhatIsYourNameGirl"

pattern = "(?P<g1>.)(?P<g2>[A-Z])"

print(re.sub(pattern, change, string))



