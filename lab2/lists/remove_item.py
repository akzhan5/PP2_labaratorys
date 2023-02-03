#remove(value) - remove the spec value
thislist = ["apple", "banana", "cherry"]
thislist.remove('apple')
print(thislist, '\n')

#pop(index) - removes the val at specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop()#pops last one
thislist.pop(1) 
print(thislist, '\n')

#del - may remove item, or the list completely
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist, '\n')
del thislist

#l1.clear() - empties the list 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
