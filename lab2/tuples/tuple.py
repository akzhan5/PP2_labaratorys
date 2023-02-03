#tuple is ordered, unchangeable 
thistuple1 = ('apple', 'banana', 'cherry')
print(thistuple1, '\n')

#tuple items - ordered, unchangeable, allow duplicate values(defined order and that order will not change)

#allow duplicates
thistuple2 = ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple2, '\n')

#tuple length 
print(len(thistuple1), '\n')

#create tuple with one item using comma after it
#Not a tuple - no comma, then str
thistuple = ('apple')
print(type(thistuple))
#Tuple: 
thistuple=('apple',)
print(type(thistuple), '\n')

#tuple items - any data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#tuple can contain different data types: int,str, bool any in one
tuple1 = ("abc", 34, True, 40, "male")

#type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple), '\n')

#tuple() constr
thistuple = tuple(('apple', 'banana', 'cherry'))
print(thistuple)

