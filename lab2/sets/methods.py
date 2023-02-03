# add() 
s1 = {1,2,3}
s1.add(5)
print(s1)

#difference() - returns a set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
k = y.difference(x)
print(z, k)

#difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

