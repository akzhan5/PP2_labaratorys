mylist = ['apple', 'banana', 'cherry']
print(mylist)
print(*mylist)

''' Lists - ordered, changeable, duplicates, 
indexed from 0'''
print()
#duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#len(list) - length 
print(len(thislist))

#lists can have any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 5, 3]
list3 = [True, False, False]
print(list2)

#lists can have diff data types
l1 = ['abc', 1, 1.0, 1j, True]
print(*l1)

print()

#type()
print(type(l1))
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print()

#list() constructor
l2 = list(('banana', 'apple', 'orange'))
print(l2)


