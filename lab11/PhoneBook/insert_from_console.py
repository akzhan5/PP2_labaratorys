import psycopg2 
from show_table import show_table
def insert_console(cur): 
#insert data from the console 
    name, phone = input().split(sep = ', ')
    cur.execute('INSERT INTO phonebook VALUES (%s, %s)', (name, int(phone)))
