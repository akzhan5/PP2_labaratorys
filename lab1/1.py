#comment 
''' multiline comment 
happens here '''

if 6//2==2: 
    print('YES')
else:
    print('NO')

x= 5
myVariableName = 'Akzhan' #Camel case - 1st little, other ones big
my_var_name = 'Akzhan' #Pascal case - all the ones are little, with case letter

x, y, z = 5,4,7 #not really important
print(x)
print(y) 
print(z)
print(x,y,z)

fruits = ['ak', 'keke', 'l']
x,y,z = fruits #parcing elements of the list to var
print(x, y)
print(z)

def my_func():
    global x
    print('My function ' + str(x))

def my_func2(): 
    print('Python is ' + str )