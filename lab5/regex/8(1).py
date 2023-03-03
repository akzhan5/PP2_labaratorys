import re 

def change(mObj): 
    return mObj.group("g1") + " " + mObj.group("g2") + mObj.group("g3")


string = "HowAreyouDoingAkzhan"

pattern = "(?P<g1>.)(?P<g2>[A-Z])(?P<g3>.)"

print(re.sub(pattern, change, string))

split = re.split("\s+", re.sub(pattern, change, string))

for i in split: 
    print(i)