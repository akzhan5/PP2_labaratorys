import re 

def change(mObject):
    return mObject.group("g1") + "_" + mObject.group("g2").lower()


#group() - returns tht part of the string where there were a match
#.span() - returns a tuple containing the start-, and end positions of the match


text = 'mySuperVar'
pattern1 = "(?P<g1>[a-z])(?P<g2>[A-Z])" #grouping 



print(re.sub(pattern1, change, text))

#sub (pattern, repl, text)

