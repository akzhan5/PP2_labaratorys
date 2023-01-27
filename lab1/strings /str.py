print('Hello')
print("Hello")

#assign string to a variable 
a = "Hello"
print(a)

a = ''' Thank God for loving parents, 
opportunity to study at university, 
independetly express my thoughts, 
access to books, and psychology, 
for air to breath, and food to eat, 
to hear others, and express thoughts myself, 
Honestly, I am so blessed '''

print(a)

a = """ Thank God for loving parents, 
opportunity to study at university, 
independetly express my thoughts, 
access to books, and psychology, 
for air to breath, and food to eat, 
to hear others, and express thoughts myself, 
Honestly, I am so blessed """

print(a)

#strings are arrays
a = "Hello, World"
print(a[0:len(a)])

#looping through a string
for x in "banana": 
    print(x)

#string length 
print(len(a))

#check string in
txt = 'The best things in life are free'
print('free' in txt)

if 'free' in txt: 
    print("Yes, 'free' is present") 

#check if NOT in
txt = "The best things in life are free!" 
if 'expensive' not in txt: 
    print("No, 'expensive' is NOT present.")





