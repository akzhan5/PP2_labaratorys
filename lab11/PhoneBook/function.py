import psycopg2 
from config import config 

params = config() 
conn = psycopg2.connect(**params) 
cur = conn.cursor() 

func = '''
CREATE FUNCTION find_user(number bigint) 
    returns TEXT[] 
    language plpgsql 
as 
$$
DECLARE
    result TEXT[];
BEGIN
   SELECT ARRAY(SELECT full_name FROM phonebook WHERE phone_number = number)
    into result;

    return result;
END;
$$;
 '''


func2 = '''
CREATE FUNCTION find_phone(username TEXT) 
    RETURNS BIGINT[]
    language plpgsql 
AS
$$
DECLARE
    result BIGINT[];
BEGIN
   SELECT ARRAY(SELECT phone_number FROM phonebook WHERE full_name = username)
   INTO result;
   return result;
END;
$$;
 '''

call = '''SELECT "find_phone"(%s)'''

#cur.execute(func2)

cur.execute(call, ('Sabibolda Akzhan', ))
for i in list(cur.fetchone()): 
    for j in i:
        print(j)

conn.commit()

