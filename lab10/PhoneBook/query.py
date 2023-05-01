import psycopg2 

def query_data(cur): 
    #selection 
    #get the person with the surname starting with A 
    f1 = '''SELECT * FROM phonebook WHERE LEFT(full_name, 1) = 'A' ''' 
    f2 = '''SELECT full_name, phone_number FROM phonebook WHERE LEFT(full_name, 3) = 'Kim' '''
    f3 = '''select * from phonebook where full_name in ('Sabibolda Akzhan', 'SABI BOL' )'''

    #execution 
    cur.execute('''select * from phonebook''') 

    #querying 
    row = cur.fetchall() 
    for i in row: 
        print(i)        