import os 

with open ('a.txt', 'r') as file: 
    x = len(file.readlines()) #readlines() - list of all the lines in the file
    print(x)