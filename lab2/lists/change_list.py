#change item by index
thislist = ["apple", "banana", "cherry"]
thislist[1]= 'mango'
print(thislist)
print()

#change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2] = ["blackcurrant", "watermelon"] #replaces banana with two items
thislist[3:5] = ["blackcurrant", "watermelon"]
print(thislist)
print()

'''insert more items than specified index, 
they will be inserted and the remained ones will move accordingly'''
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #2 inserted, to the 1st index, cherry moved

#the length of the list will change if the number of items inserted does not match the number of items replaced

#less items = replace the range whole, others move accordingly
thislist[1:3] = ['watermelon']
print(thislist)
print()

#insert(pos, item)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,'mango') #without replacing any item 
print(thislist)