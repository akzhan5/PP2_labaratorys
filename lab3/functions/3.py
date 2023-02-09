def solve(numheads, numlegs): 
    '''c + r = numheads 
    2*c + 4*r = numlegs
    2*r = numlegs - 2*numheads'''
    r = int((numlegs - 2*numheads)/2)
    c = int(numheads - r)
    print('The number of rabbits: ', r)
    print('The number of chickens: ', c)

solve(35, 94)

