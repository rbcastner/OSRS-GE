import json
import pandas 

with open('/Users/nicholasramos/pythonstuff/test.txt') as data_file:    
   data = json.load(data_file)

item_number=[] 
my_dict=[]
store_list=[]
name_list=[]

for item in data:
    item_number.append(item)
    
for k in data: 
    my_dict.append(data[k])

for store in my_dict: 
    store_dict = store
    store_list.append(store_dict['store'])

for name in my_dict: 
    name_dict = name 
    name_list.append(name_dict['name'])

name_to_id = dict(zip(name_list, item_number))
id_to_name = dict(zip(item_number, name_list))

print (name_to_id['Cannonball'])
print (id_to_name['2'])