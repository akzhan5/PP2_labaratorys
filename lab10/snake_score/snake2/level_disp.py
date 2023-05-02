import psycopg2 
import pygame
from config import config 

def level_disp(string): 
    conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Teachbeast_2005")

    cur = conn.cursor() #object of cursor class 

    in_it = '''SELECT username, score, level FROM user_score WHERE username = %s''' 
    cur.execute(in_it, (string, ))
    q = cur.fetchone()
    score = q[1] 
    level = q[2] 

    return [score, level]

print(level_disp('Akka'))