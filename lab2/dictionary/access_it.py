#refer by the key 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict['model'], '\n')

#get() 
x = thisdict.get('model')
print(x, '\n')

#get keys
x = thisdict.keys()
print(x, '\n')

#adding new item - changes key list
car = {
    'brand': 'Ford', 
    'model': 'Mustang', 
    'year': 1964
}
print(car.keys())
car['colour'] = 'red'
print(car.keys(), '\n')

#get values
x=  thisdict.values()
print(x, '\n')

#adding a new value changes the values list
car = {
    'brand': 'Ford', 
    'model': 'Mustang', 
    'year': 1964
}
print(car.values())
car['year'] = 2020
print(car.values(),'\n')


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x, '\n') #after the change

#get items 
# items() - return each item in a dictionary as a tuples
x = thisdict.items()
print(x,'\n')

#change - updates items list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#make a chnage in the original dictionary - overrides the 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car['year'] = 2020
print(x, '\n') #after the change

#check if key exists 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if 'model' in thisdict: 
    print('Yes, "model" is one of the keys')
if 'Ford' in thisdict.values(): 
    print('Hehe')