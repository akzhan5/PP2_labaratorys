thisdict = {
    'brand': 'Ford', 
    'model': 'Mustang',
    'year': 1964
}
print(thisdict, '\n')

#dictionary items - ordered, changeable, does not allow duplicates(keys)
print(thisdict['brand'])

#ordered - items have a defined order, it will not change, can refer by a key

#dupl not allowed
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang', 
    'year': 1964, 
    'year': 2020 #overrides 1964
}
print(thisdict, '\n') #dupl overrides the existing

#dict length 
print(len(thisdict), '\n')

#dict items - data types: 
#str,bool, int, list

thisdict = { 
    'brand': 'Ford',
    'electric': False, 
    'year': 1964,
    'colors': ['red', 'white', 'blue']
}
print(thisdict, '\n')

#tupe() 
print(type(thisdict), '\n')

#dict() - const 
thisdict = dict(name = 'John', age = 36, country = 'Norway')
print(thisdict)






