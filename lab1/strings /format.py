#format() - combine strings and numbers. 

'''age = 36 
txt = "My name is John, I am " + age
print(txt) #TypeError'''
age = 36
txt = 'My name is Akzhan, I am {}' 
print(txt.format(age)) #format - takes an arg and puts it into {} placeholder

#format() - takes unlimited number of arguments, and puts them into corresponding placeholders 

q = 3
i = 'cake'
p = 49.95

myorder = 'I want {} pieces of item {} for such price {}'
print(myorder.format(q,i,p))

#use indexes to arrange args using format
myorder = 'I want {1} pieces of item {0} for {2}'
print(myorder.format(i, q, p))








