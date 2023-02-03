#set = unchangeable, unordered, unindexed. can remove and add new items
thisset= {'apple', 'banana', 'cherry'}
print(thisset, '\n') #not sure in which order items will appear

#no duplicates
thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset, '\n')

#get the length of a set 
print(len(thisset), '\n')

#set items can be any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#set may contain diff data types
set1 = {"abc", 34, True, 40, "male"}

#type()
print(type(thisset), '\n')

#set() const
thisset = set(('apple', 'banana', 'cherry'))
print(thisset)

