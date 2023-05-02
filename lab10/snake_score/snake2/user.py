import psycopg2 
from config import config 

def user_inp(string): 
    conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Teachbeast_2005")

    cur = conn.cursor() #object of cursor class 

    for_key_ex = '''CREATE TABLE score_and_level 
    (id SERIAL, 
    username TEXT ,
    score INT, 
    level INT, 
    CONSTRAINT fk_user 
        FOREIGN KEY (username)
            REFERENCES USERNAME(username) 
            ON DELETE CASCADE
    ); 
    ''' #on del cascade auto deletes col in the child table if the par table pr key was deleted

    insrt = '''INSERT INTO USERNAME(username) 
    VALUES(%s)
    ON CONFLICT (username) DO UPDATE SELECT score, level FROM user_score; '''

    insrt2 = '''INSERT INTO USERSCORE_AND_LEVEL(username)
    VALUES(%s)'''

    in_it = '''SELECT username, score, level FROM user_score WHERE username = %s''' 


    cte_score = '''WITH cte AS (
   INSERT INTO "username"(username)
   VALUES (%s)
   ON CONFLICT (username) DO NOTHING
   RETURNING username
)
SELECT NULL AS result
WHERE EXISTS (SELECT 1 FROM cte)  
UNION ALL        
SELECT score
FROM "user_score" 
WHERE username= %s 
AND NOT EXISTS (SELECT 1 FROM cte);  '''

    cte_level = '''WITH cte AS (
   INSERT INTO "username"(username)
   VALUES (%s)
   ON CONFLICT (username) DO NOTHING
   RETURNING username
)
SELECT NULL AS result
WHERE EXISTS (SELECT 1 FROM cte)  
UNION ALL        
SELECT level
FROM "user_score" 
WHERE username= %s 
AND NOT EXISTS (SELECT 1 FROM cte);  '''


    del_col = '''ALTER TABLE username DROP COLUMN IF EXISTS id'''
    
    cur.execute(cte_level, (string, string, ))
    conn.commit()
    return cur.fetchone()
