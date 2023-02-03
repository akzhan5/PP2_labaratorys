#boolean values
print(10>9)
print(10==9)
print(8>9)

#condition in an if st python returns true or false
a = 200
b = 33
if b>a: 
    print('b is greater than a')
else: print('a is greater than b')

print()

#evaluate values and variables - true or false in return 
print(bool('Hello')) #true 
print(bool(1)) # 1 - true 
print(bool(0)) # 0 - false

#evaluate 2 variables 
x ='Hello'
y =15
print(bool(x))
print(bool(y))
print()

#Most values are True 
''' strings are true, empty string - false 
number is true, 0 -false 
list, tuple, set, dict - true, empty ones- false'''

print(bool('abc'))
print(bool([1,2,3])) 
print(bool((1,2,3)))
print(bool({1,2,4,4}))

print()

#Some values are false
print(bool(False))
print(bool(0))
print(bool(''))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))

'''class with a methid that returns 0, bool(obj) will be False'''
class myclass(): 
    def __len__(self):  #def len (self) - returns True..
        return 0

myobj = myclass()
print(bool(myobj))
print()

#functions can return a bool
def myfunc(): 
    return True

print(bool(myfunc))

#execute code based on a bool of a function
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


def IsPositive(x): 
    if x >0: 
        return True
    else: return False
x= int(input())
if IsPositive(x): 
    print('Yas')
else: 
    print('No')

#built-in func: isinstance() - if object is of a certain data type

x= 200
print(isinstance(x, int)) #x is an int, so prints True
print(isinstance(x, float)) # x is an int, so False

