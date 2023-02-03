i =1 
while i<6: 
    print(i)
    i+=1

#note remember to increment i, or else the loop will continue forever 
print()

#break st
i =1
while i<6: 
    print (i)
    if i==3:
        break #stop the loop
    i+=1

print()


#continue - stop current iteration, and continue with the next 
i = 0
while i<6: 
    i+=1
    if i==3:
        continue #goes over 3 
    print(i)

print()

#else st
i =1
while i<6: 
    print(i)
    i+=1
else: 
    print('i is no longer less than 6')










