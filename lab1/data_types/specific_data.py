#specify data type with constructor 

x= str('Hello Wordl')
x =int(20) #int
x= float(20.5) #float
x = complex(1j) #complex number
x = list(['apple', 'banana', 'orange']) #list - mutable , may contain diff data types
x= tuple(('apple', 'banana', 'orange')) #tuple - immutable just like list
x = range(7) #range 
print(type(x))

x = dict({'name': 'John', 'age': 36}) #dict: key-value pairs

x = set({'apple', 'bana', 'orange'}) # set - mutable, unique elements

x = frozenset({3,2,3,4,3}) #immutable, unique elements
print(*x)

x = bool(True) #bool

x = bytes('Hello') #bytes
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



