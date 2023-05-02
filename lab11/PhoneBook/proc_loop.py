import psycopg2 
from config import config 

params = config() 
conn = psycopg2.connect(**params) 
cur = conn.cursor() 

type = '''create type my_item as (
    field_1        text,
    field_2        bigint,
);'''

cur.execute(type)

proc = '''
create or replace procedure many_insert(
users text[])
language plpgsql 
as $$
declare 
var record;
begin 
for var in select users
    loop
    insert into phonebook (full_name) 
    select var 
    where not exists (select 1 from phonebook where full_name = username);
    end loop;
end; $$'''

names = ['Son Lok', 'Pan Sam', 'Roy Charles'] 

call = '''call many_insert(%s)'''

cur.execute(proc) 
    