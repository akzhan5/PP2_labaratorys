#index number list[i]
thislist = ["apple", "banana", "cherry"]
print(thislist[0])
print()

#negative indexing: starts from the end of the list
print(thislist[-1])
print(thislist[-3])
print()

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(*thislist[2:5]) #2 included, 5 not included #index start = 0

#leavong out start, from the start auto 
print(thislist[:4])

#leaving out the end- goes till the end
print(thislist[1:])
print()

#Range of negative indexes
#specify negative indexes if you want to start the search from the end of the list 
print(thislist[-4:-2])
print()

#Check item - in 
if 'apple' in thislist: 
    print('yes, \'apple\' is in the list' )





