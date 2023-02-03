#loop through items 
thislist = ["apple", "banana", "cherry"]
for x in thislist: 
    print(x)

print()
#loop throgh the index
for i in range(len(thislist)): 
    print(thislist[i])

print()
#while loop 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist): 
    print(thislist[i])
    i+=1

print()
#using list comprehension 
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 
print()
[print(thislist[i]) for i in range(len(thislist))]
print()
[print(thislist[i]) for i in range(len(thislist)) if i==0]
