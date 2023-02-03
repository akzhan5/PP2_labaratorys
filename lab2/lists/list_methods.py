l1 = [1,2,3,6]

#append() - adds an el at the end of the list 
l1.append(5)
print(l1)

#clear() - removes all the elem from the list 
l1.clear()
print(l1)

#copy() - returns a copy of the list
l2 = [1,2,3]
l3 = l2.copy()
l2.remove(3)
print(l3, ' ', l2)

#count(value) - ret the number of elements with the spec value 
l2 = [1,2,2,2,3,3,4]
print(l2.count(2), ' ', l2.count(3))

#extend() - adds a list to the current list
l2.extend(l3) #extends l2 with l3
print(l2)

#index(value) - returns the index of the 1st elem with the specified value
print(l2.index(2))

#insert(pos, v) - add el to the spec pos
#append() - adds to the end
l3.insert(2, 'a')
print(l3)

#pop(pos) - removes the el at the spec pos 
l3.pop() #no pos - removes the last one
print(l3)
l3.pop(1)
print(l3)

#remove(val) - removes the item with the specified value
l3.remove('a')
print(l3)

#reverse() - reverses the order of the list
l2.reverse()
print(l2)

#sort() - sorts the list
l2.sort()
print(*l2)