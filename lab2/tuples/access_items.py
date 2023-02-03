#refer to index
mytuple = ("apple", "banana", "cherry")
print(mytuple[0], '\n')

#negative indexing - start from the end
thistuple = ('apple', 'banana', 'cherry')
print(thistuple[-1], '\n') #cherry

#range of indexes - start and end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5], '\n') #cherry, orange, kiwi

#leave out the start- auto from 0
print(thistuple[:5], '\n')

#leave out the end - auto till end
print(thistuple[3:], '\n')

#range of negative indexes 
print(thistuple[-4:-1], '\n') #from -4: (orange kiwi melon) -1:mango not in

#check if item exists: 
thistuple = ('apple', 'banana', 'cherry')
if 'apple' in thistuple:
    print("Yes, 'apple' is in the tuple") 




