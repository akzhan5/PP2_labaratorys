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

        #create a new database conenction by calling connect(parameters)
        #important data is hidden by params 
        conn = psycopg2.connect(**params) #to create a new database connection the connection parameters are given as argument to the function 

        #by using the connection obj, 
        # you can create a new cursor to execute any SQL statements 
        cur = conn.cursor() 

        #execute a statement 
        cur.execute("""SELECT * FROM accounts""")

        #display the PostgreSQL database server version 
        #fetchone - read result set by calling the fetchone() method of the cursor obj 
        #table = cur.fetchall() 
        #for tb in table: 
            #print(tb) 

        #fetching 1st row from the table 
        res = cur.fetchall() 
        print(res)

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
