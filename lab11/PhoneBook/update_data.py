import psycopg2 
import string 
from show_table import show_table

def change_in_table(cur): 
#make a cursor that will execute operations 

    #change the data from the console 
    #update user phone based on the phone
    upd1 = '''UPDATE phonebook 
            SET  phone_number = %s 
            WHERE full_name = %s''' 
    
    upd2 = '''UPDATE phonebook 
            SET full_name = %s
            WHERE phone_number = %s'''
    
    dt = show_table(cur)

    print('Do you want to change the name or the phone?')
    ans = input() 
    if ans == 'phone': 
        name, phone = input().split(sep = ', ')
        for l in dt: 
            if name in l:
                cur.execute(upd1, (phone, name))
                break 

    if ans == 'name': 
        name, phone = input().split(sep = ', ')
        for l in dt: 
            if int(phone) in l:
                cur.execute(upd2, (name, phone))
                break 


    