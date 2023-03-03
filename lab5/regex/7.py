import re

#snake_case 
#camelCase 
def change(mObj): 
    return mObj.group("g1") + mObj.group("g3").upper()


snake_case = "my_snake_is_keke" 
pattern = "(?P<g1>[a-z])(?P<g2>_)(?P<g3>[_a-z])"
 

print(re.sub(pattern, change, snake_case))

