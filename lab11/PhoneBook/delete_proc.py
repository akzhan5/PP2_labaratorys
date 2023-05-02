import psycopg2 
from config import config 

params = config() 
conn = psycopg2.connect(**params) 

cur = conn.cursor() 

proc ='''
create or replace procedure delete_proc(
username TEXT )
language plpgsql 
as $$
begin 
delete from phonebook where full_name = username;
end; $$'''

proc2 = '''
create or replace procedure delete_phone(
phone BIGINT )
language plpgsql 
as $$
begin 
delete from phonebook where phone_number = phone;
end; $$'''

cur.execute(proc2)
call1 = '''call delete_proc(%s)'''
#name = input() 
phone = int(input())
call2 = '''call delete_phone(%s)'''
#cur.execute(call, (name,) )
cur.execute(call2, (phone, ))

conn.commit()