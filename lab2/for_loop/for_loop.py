#for 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print()

#looping through a string
for x in 'banana': 
    print(x)

print()

#break 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x=='banana': 
    break #stops the loop
print()

#break befire the print 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'banana': 
        break
    print(x) #apple only

print()

#continue 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x =='banana': 
        continue #goes to the next iteration
    print(x) #banana wont be printed out

print()

#range(): 
for x in range(10): 
    print(x) #0-9
print()
#start prm
for x in range(1,4): 
    print(x)
print()

#increment the seq
for x in range(1,30,3): #incr is 3
    print(x)

print()

#else : 
for x in range(6): 
    print(x)
else: 
    print('Finally finished!')

print()

#break, else 
for x in range(6): 
    print(x)
    if x==3: break 
else: 'Not done anyway'

print()

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: 
    for y in fruits: 
        print(x,y)

print()

#pass st - avoi get error with empty for loop
for x in range(1,5): 
    pass

