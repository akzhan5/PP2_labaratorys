from itertools import permutations

def permute(string): 
    permutes = permutations(string)
    for i in permutes:
        print(''.join(i))

s = input()
print('Permutations:')
permute(s)

