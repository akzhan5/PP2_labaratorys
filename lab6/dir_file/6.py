import os, string 


if not os.path.exists('letters'): 
    os.makedirs('letters')

for letter in string.ascii_uppercase: 
    with open(letter+'.txt', 'w') as file: 
        file.writelines(letter)

