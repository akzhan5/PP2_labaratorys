import os 

path1 = '/Users/akzhansabibolda/Documents'

#existence of a path - os.path.exists()
if os.path.exists(path1): 
    print('Such path exists') 
else: 
    print('Such path does not exist')

#readiability of a path - os.access(path, R_OK) = bool
if os.access(path1, os.R_OK): 
    print("Readible path")
else: 
    print("Not readible path")

#writeability 
if os.access(path1, os.W_OK): 
    print("Writeable path")
else: 
    print("Not writeable")

#executeablity 
if os.access(path1, os.X_OK): 
    print("Executable path")
else: 
    print("Not executable")

