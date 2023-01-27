#assign a value to variable

x= 'Hello Wordl'
x =20 #int
x= 20.5 #float
x = 1j #complex number
x = ['apple', 'banana', 'orange'] #list - mutable , may contain diff data types
x= ('apple', 'banana', 'orange') #tuple - immutable just like list
x = range(7) #range 
print(type(x))

x = {'name': 'John', 'age': 36} #dict: key-value pairs

x = {'apple', 'bana', 'orange'} # set - mutable, unique elements

x = frozenset({3,2,3,4,3}) #immutable, unique elements
print(*x)

x = True #bool

x = b'Hello' #bytes
print(type(x)) 
print(x)

x = bytearray(5)
print(type(x))
print(x)

x= memoryview(bytes(5)) #memoryview
print(type(x))
print(*x)

x= None #NoneType
print(x)



