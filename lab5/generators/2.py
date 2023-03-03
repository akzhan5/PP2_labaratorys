def evens(n): 
    for i in range(n+1): 
        if i%2==0: 
            yield i




numb = int(input())
for x in evens(numb):
    print(x, end = ', ')

