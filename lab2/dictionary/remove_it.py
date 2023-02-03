#pop() - removes the item with the spec key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop('year')
print(thisdict, '\n')

#popitem() - removes the last inserted item 
thisdict.popitem()
print(thisdict, '\n')

#del - removes the item with the key name, del dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict['model']
print(thisdict)

del thisdict #comp delete 

#clear() - empties the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
