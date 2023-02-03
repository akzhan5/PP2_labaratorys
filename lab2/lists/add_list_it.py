#append() - add item to the end 
thislist = ["apple", "banana", "cherry"]
thislist.append('melon')
print(thislist)

print()

#insert(pos, item)
thislist.insert(1, 'mango') 
print(thislist)

print()

#l1.extend(l2) - extends l1 with l2
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
tropical.extend(thislist)
print(tropical)
print(thislist, '\n')

#extend() - adds any iterable obj(lists, tuples, dict)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange") #tuple (..)
dict = {1:'a', 2:'b'}
thislist.extend(thistuple)
thislist.extend(dict.values()) 
print(thislist)


