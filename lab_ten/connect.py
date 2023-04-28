#the function connect() function connects to the suppliers database 
#and prints out the PostgreSQL database version 
import psycopg2 
from config import config

def connect(): 
    # connect to the PostgreSQL database server 
    conn = None 

    try: 
        #read connection parameters from the database.ini file
        params = config()

        #connect to the PostgreSQL server 
        print('Connecting to the PostgreSQL database..') 
        #create a new database conenction by calling connect(parameters)
        conn = psycopg2.connect(**params) #to create a new database connection the connection parameters are given as argument to the function 

        #by using the connection obj, 
        # you can create a new cursor to execute any SQL statements 
        cur = conn.cursor() 

        #execute a statement 
        print('PostgreSQL database version: ') 
        cur.execute('SELECT version()') 

        #display the PostgreSQL database server version 
        #fetchone - read result set by calling the fetchone() method of the cursor obj 
        db_version = cur.fetchone() 
        print(db_version) 

        #close the communication with the PostgreSQL 
        cur.close() 
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
    finally: #exception or not does not matter, runs in any case
        #connection should close
        if conn is not None: 
            conn.close() 
            print("Database connection closed") 


connect()
