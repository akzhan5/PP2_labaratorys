import psycopg2 

def delete_data(cur): 
    #delete st 
    name = input()
    dele = '''DELETE FROM phonebook WHERE phone_number = '{0} {1}' '''

    #execution 
    cur.execute(dele.format(name.split()))