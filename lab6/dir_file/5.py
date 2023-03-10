import os

with open ('newfile.txt', 'w') as file:
    file.write('This is the new file')

lis = ['Hi girl', 22 , 'Akzhan', True] 

with open ('newfile.txt', 'w') as file: 
    for i in lis: 
        file.write(str(i)+ '\n')

