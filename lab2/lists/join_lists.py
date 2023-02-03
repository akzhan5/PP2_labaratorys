# + op: 
list1 = ['a', 'b', 'c', 'd']
list2 = [1,2,3]
list3 = list1 + list2 #join 2 lists
print(list3, '\n')

#appending from list2 to list1: 
for i in list2: 
    list1.append(i)
print(list1, '\n')

list1 = ['a', 'b', 'c', 'd']
#extend() -add el of one list to another
list1.extend(list2)
print(list1)