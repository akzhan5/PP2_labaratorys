import psycopg2 
from config import config 

def score(string, score, level): 
    conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Teachbeast_2005")

    cur = conn.cursor() #object of cursor class 

    for_key_ex = '''CREATE TABLE score_and_level 
    (id SERIAL, 
    username TEXT,
    score INT, 
    level INT, 
    CONSTRAINT fk_user 
        FOREIGN KEY (username)
            REFERENCES USERNAME(username) 
            ON DELETE CASCADE
    ); 
    ''' #on del cascade auto deletes col in the child table if the par table pr key was deleted

    insrt3 = '''INSERT INTO USERSCORE_AND_LEVEL(username, score, level) 
    VALUES(%s, %s, %s)'''

    insrt4 = '''INSERT INTO user_score(username, score, level) 
    VALUES(%s, %s, %s) 
    ON CONFLICT (username) DO UPDATE SET score = EXCLUDED.score, level = EXCLUDED.level; '''

    del_col = '''ALTER TABLE username DROP COLUMN IF EXISTS id'''

    cur.execute(insrt4, (string, score, level) )
    conn.commit()