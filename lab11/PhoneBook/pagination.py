import psycopg2 
from config import config 

params = config() 
conn = psycopg2.connect(**params) 
cur = conn.cursor() 

pagi = '''CREATE OR REPLACE FUNCTION GetRowsByPageNumberAndSize(
 PageNumber INTEGER = NULL,
 PageSize INTEGER = NULL
 )
 RETURNS SETOF phonebook AS
 $BODY$
 BEGIN
  RETURN QUERY
   SELECT *
   FROM phonebook
   ORDER BY full_name
   LIMIT PageSize
   OFFSET ((PageNumber-1) * PageSize);
END;
$BODY$
LANGUAGE plpgsql;'''

#cur.execute(pagi)

call = '''SELECT "pagination"(%s, %s)'''

cur.execute(call, (2,3,))

for i in list(cur.fetchall()): 
    l = list(i) 
    print(*l)

conn.commit()