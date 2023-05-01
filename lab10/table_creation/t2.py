import psycopg2
import csv 

conn = psycopg2.connect(database="suppliers",
						user='postgres', password='Teachbeast_2005',
						host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()


sql2 = '''COPY DETAILS(employee_id,employee_name,\
employee_email,employee_salary)
FROM '/private/tmp/table_copy.csv'
DELIMITER ','
CSV HEADER'''

cursor.execute(sql2)

sql3 = '''select * from details;'''
cursor.execute(sql3)
print(cursor.fetchall())

conn.commit()
conn.close()

