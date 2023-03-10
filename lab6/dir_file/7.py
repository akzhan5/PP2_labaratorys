import os 

with open('in.txt', 'r') as f: 
    with open('out.txt', 'w') as f1: 
        for i in f: 
            f1.write(i)

