import os 

print(os.getcwd()) #returns the present working directory in the form of a string

#change directory os.chdir()

# list directories - os.listdir()
#os.mkdir() - make a new directory

path1= '/Users/akzhansabibolda/Documents'

files = []
dirs = []

for i in os.listdir(path1): 
    if os.path.isfile(i): 
        files.append(i)
    elif os.path.isdir(i): 
        dirs.append(i)

print('Files:')
for l in files: 
    print(l, end = ", ")

print()

print('Directories: ', )
for m in dirs: 
    print(m, end = ", ")

print()

print('Files and Directories:')
for i in os.listdir(path1): 
    print(i, end = ', ')

