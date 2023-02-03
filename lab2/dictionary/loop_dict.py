thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#print key names
for i in thisdict: 
    print(i)
print()
#print values: 
#values() meth
for i in thisdict.values(): 
    print(i)

for i in thisdict: 
    print(thisdict[i])
print()

#keys meth
for i in thisdict.keys(): 
    print(i)

#loop through both key and values: items()

for k,v in thisdict.items(): 
    print(str(k) + ' is a ' + str(v) )


