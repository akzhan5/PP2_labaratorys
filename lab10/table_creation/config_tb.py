import psycopg2 #to be ablte to work with databases 
from configparser import ConfigParser 

def config (filename = 'database1.ini', section = 'postgresql'): 
    #create a parser 
    parser = ConfigParser() #obg of class ConfigParser // turns into dictonary 
    #read config file using parser method 
    parser.read(filename) 

    # get section, default to postgresql 
    db = {} 
    if parser.has_section(section): #indicate whether section is present in the cofiguration 
        params = parser.items(section) #return a list of name value tuples for each  option in a section 
        for param in params: 
            db[param[0]] = param[1] #db[name] = value 
    else: 
        raise Exception('Section {0} not found in the {1} file'.format(section, filename)) 
    return db #returns database 