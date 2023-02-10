# conversion
def toString(List):
   return ''.join(List)
    
# find all permutations
def permuteFunc(a, l, r):
   if l == r:
      print (toString(a))
   else:
      for i in range(l, r + 1):
         a[l], a[i] = a[i], a[l]
         permuteFunc(a, l + 1, r)
         a[l], a[i] = a[i], a[l] # backtracking
          
# main
str=input('Enter a string: ')
n = len(str)
a = list(str)
print("The possible permutations are:",end="\n")
permuteFunc(a, 0, n-1)
