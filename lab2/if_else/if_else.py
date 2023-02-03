#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#indentation error
'''
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
'''

#elif
a =33
b= 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else: 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#if, else: 
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short-hand IF: 
if a>b: print('a is greater than b')

#Short-Hand If/Else: 
a = 2
b = 330
print("A") if a>b else print('B')
print('Hey') if a==b else print('J')

#ternary op: 
a = 330
b = 330
# 3 cond
print('A') if a>b else print('=') if a==b else print('B')
#rewritten as 
if a>b: 
    print('A')
else:
    if a==b: 
        print('=')
    else: 
        print('B')

print()

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print()

#or 
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print()

#not: 
a = 33
b = 200
if not a>b: 
    print('a is NOT greater than B')

print()

#nested if
x = 41
if x>10: 
    print('Above 10')
    if x>20: 
        print(' and Above 20')
    else: 
        print(' but not above 20')
else: 
    print('Not above 10')

print()

#pass st 
a= 33
b = 200
if b>a: 
    pass #if with no cont to avoid error