import psycopg2 
from config import config 

def show_table(cur): 
    #show the table in the console
    show = '''SELECT * FROM phonebook ORDER BY full_name ASC;''' 
    cur.execute(show) 
    data = []
    for i in cur.fetchall(): 
        data.append(i)
    return data
