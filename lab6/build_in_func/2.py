s = input()

upper = 0 
lower = 0


for i in s:
    if i.isupper(): 
        upper+=1
    elif i.islower(): 
        lower+=1

print('Number of upper case letters: ', upper) 
print('Numeber of lower case letters: ', lower) 