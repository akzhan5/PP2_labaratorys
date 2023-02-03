fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []
 
#without list copmprehension
for x in fruits: 
    if 'a' in x: 
        newlist.append(x)
 
print(newlist)
newlist=[]

#with list comprehension: 
newlist = [x for x in  fruits if 'a' in x]
print(newlist, '\n')

#newlist = [expression FOR item IN iterable IF condition==True]

newlist2 = [x for x in fruits if x != 'apple']
print(newlist2,'\n')

#with no conditional 
newlist3 = [x for x in fruits]
print(newlist3, '\n')

#iterable - any: list, tuple, set etc
newlist4 = [x for x in range(10)]
print(newlist4, '\n')

newlist5 = [x for x in range(10) if x>5]
print(newlist5, '\n')
newlist5 = [x for x in range(20) if x<15]

#expression - current item on the iteration, manipulate it and then add to the new list
newlist6 = [x.upper() for x in fruits]
print(newlist6, '\n')

#set the outcome: set all the iterms to one 
newlist7 = ['Hello' for x in fruits ]
print(newlist7, '\n')

#expression with condition to man the outcome
newlist8 = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist8)
#if exp is not banana add it to the list, eif it is banana add orange
 

