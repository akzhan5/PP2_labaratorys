#diff between global and local var
x = "awesome"
def myfunc():
  x = 'haha' #local 
  print("Python is " + x)

myfunc()
print(x) #globally unchanged


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
 
myfunc() #func call - local x is used

print("Python is " + x) #globally unchanged

print()

#global - keyword
x= 'awesome'
def myfunc():
  global x #now var belongs to the global scope, globallu changed in the fucntion 
  x = "fantastic"

myfunc() #local x fantstic used

print("Python is " + x) #fantstic used, since global x was used to make it global



x = "awesome"
#use of global for variables 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


