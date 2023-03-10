import os 

path1 = '/Users/akzhansabibolda/Documents'

if os.path.exists(path1): 
    print('Filename of the path: ', '\n', os.path.basename(path1))
    print('Directory portion of the path: ', '\n', os.path.dirname(path1))
else: 
    print('This path does not exist')