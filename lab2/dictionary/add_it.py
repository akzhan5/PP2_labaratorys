#add new key-value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict['color'] = 'white'
print(thisdict)

#update() dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({'color':'white'}) #update dict with a set of key-value pair
print(thisdict)
thisdict.update({'side': 4})

