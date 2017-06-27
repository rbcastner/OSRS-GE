import json
import pandas 

with open('ge_store_data.json') as data_file:    
   data = json.load(data_file)

item_number=[] 
my_dict=[]
store_list=[]
name_list=[]

for item in data:
    item_number.append(int(item))
    
for k in data: 
    my_dict.append(data[k])

#for store in my_dict: 
#    store_dict = store
#    store_list.append(store_dict['store'])

for name in my_dict: 
    name_dict = name 
    name_list.append(name_dict['name'].lower())

dict_keys = name_list+item_number
dict_values = item_number+name_list
item_query_dict = dict(zip(dict_keys,dict_values))
