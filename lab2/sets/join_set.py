# union() method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3, '\n')

#update() - inserts items of set2 into set1 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1, '\n')

#keep only the duplicates
#intersection_update() - keeps itesm that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x, '\n')

#intersection() - returns the new set with el that are present in both sets
z = x.intersection(y)
print(z, '\n')

#keep all but not the duplicates

#symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x, '\n')

#returns a set - symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=  x.symmetric_difference(y)
print(z)





