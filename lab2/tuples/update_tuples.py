#tuple - unchangeable , workaround: 
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1]='kiwi'
x = tuple(y)
print(x, '\n')

#add items
#1. convert into a list
thistuple = ("apple", "banana", "cherry")
y= list(thistuple)
y.append('orange')
thistuple = tuple(y)
print(thistuple, '\n')

#2. add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ('orange', )
thistuple+=y
print(thistuple, '\n')

#remove items 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove('apple')
y.pop(0)
thistuple = tuple(y)
print(thistuple, '\n')

#delete tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)




