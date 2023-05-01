import psycopg2 
from config import config 

def upload_from_csv(cur): 
#delete all the previous info from the table 
    dele = '''DELETE FROM phonebook'''
    cur.execute(dele)

#upload data from book.csv file again 
    with open('book.csv', 'r') as f: 
        next(f) #skip the header row 
        cur.copy_from(f, 'phonebook', sep = ',')