import os 

with open('file.txt', 'w') as file: 
    file.write('Keke')

path1 = os.path.dirname('file.txt')

if os.path.exists('file.txt'): 
    os.remove('file.txt')



