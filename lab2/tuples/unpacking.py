#packing 
fruits = ("apple", "banana", "cherry")

#extract values back into variables - unpacking
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red, '\n')


#numb of var must match the leb of tuple, if not use * to collect the rest as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) # * - collects the rest as a list)
print(type(red), '\n')

#matches el to the list till the left number of el 
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic) #list: mango, papaya, pineapple
print(red)
