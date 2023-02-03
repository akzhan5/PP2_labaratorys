#cant copy, just a reference
list1 = [3,1,2,4]
list2 = list1
list1.sort()
print(list2, '\n')

#copy() - make a copy of the list
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy() #copies
thislist.append('keke')
print(mylist, '\n')

#list(thislist) - another way of copying
thislist2 = ['apple', 'banana', 'cherry']
mylist2 = list(thislist2)
print(mylist2, '\n')
