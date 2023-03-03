#generator is a function that
def squares(n):
    for i in range(n): 
        yield i**2

numb = int(input()) 
for x in squares(numb): 
    print(x)