import psycopg2 
from config import config 

params = config() 
conn = psycopg2.connect(**params) 
cur = conn.cursor() 

insrt4 = '''INSERT INTO user_score(username, score, level) 
    VALUES(%s, %s, %s) 
    ON CONFLICT (username) DO UPDATE SET score = EXCLUDED.score, level = EXCLUDED.level; '''

upd = '''UPDATE phonebook 
            SET  phone_number = %s 
            WHERE full_name = %s''' 
    

proc = '''
create or replace procedure insert(
username TEXT,
phone BIGINT
)
language plpgsql 
as $$
begin 

insert into phonebook (full_name, phone_number) 
select username, phone 
where not exists (select 1 from phonebook where full_name = username);

update phonebook 
set phone_number = phone 
where full_name = username;
end; $$'''

#cur.execute(proc) 

call = '''call insert(%s, %s)'''
name, phone = input().split(', ') 

cur.execute(call, (name, int(phone), ))

conn.commit()