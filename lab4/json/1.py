import json 
from tabulate import tabulate

#opening json file 
f = open("data.json")
#returns json object as a dict 
data = json.load(f)

print ("Interface status")
print('================================================================================') 

col_names = ['DN', 'Description', 'Speed', 'MTU']
datas = []
rows = []

for i in data['imdata']: 
    rows.append(i["l1PhysIf"]["attributes"]["dn"])
    rows.append(i["l1PhysIf"]["attributes"]["descr"])
    rows.append(i["l1PhysIf"]["attributes"]["speed"])
    rows.append(i["l1PhysIf"]["attributes"]["mtu"])
    datas.append(rows)
    rows = []

print(tabulate(datas, headers = col_names))

#to make a table use tabulate!









