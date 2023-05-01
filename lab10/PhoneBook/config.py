import psycopg2 
from configparser import ConfigParser

def config(filename = 'database.ini', section = 'postgresql'): 
    #create a parser 
    parser = ConfigParser() #an object of class ConfigParser() 
    #read config file 
    parser.read(filename) 

    #get section, default to postgresql, return connection parameters 
    db = {} 
    if parser.has_section(section): 
        params = parser.items(section) #parameters - items() - returns a list of tuples (name, value) for each option in a section
        for param in params: #param is a tuple consisting of (name, value) for each parameter in a section
            db[param[0]] = param[1] #db[name of option] = value of option 
    else: 
        raise Exception ('Section {0} not found in the {1} file'.format(section, filename)) 
    return db 