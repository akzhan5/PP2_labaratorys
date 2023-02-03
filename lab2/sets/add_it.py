#add() 

thisset = {"apple", "banana", "cherry"}
thisset.add('orange')
print(thisset, '\n')

#add sets 
tropical = {'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset, '\n')

#add any iterable object 
mylist = ['kiwi', 'orange']
thisset.update(mylist)

print(thisset, '\n')

