import psycopg2 
from config import config
from upload_from_csv import upload_from_csv
from insert_from_console import insert_console
from show_table import show_table
from update_data import change_in_table 
from query import query_data
from delete import delete_data
#make a connection with the database in postgresql 
params = config() 
conn = psycopg2.connect(**params)

#conn.autocommit = True #commands have immediate effect 

#make a cursor that will execute operations 
cur = conn.cursor() 

#creation of the table called phonebook
create_tb = '''CREATE TABLE IF NOT EXISTS PHONEBOOK
 (id INT NOT NULL, full_name VARCHAR(100), phone_number INT NOT NULL);'''
cur.execute(create_tb) 

#upload data from csv 
upload_from_csv(cur) 

#insert data from the input 
insert_console(cur)

#update data in the table 
change_in_table(cur); 

#delete data from table by username 
delete_data(cur)

#querying data 
query_data(cur) 

#show info from the table  
dt = show_table(cur) 
for i in dt: 
   print(i)

#close the connection with the database
conn.commit()
conn.close()