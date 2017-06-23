import requests
import pdb

def grand_exchange_query(query_type=None,itemID = None):
    base_url = "http://services.runescape.com/m=itemdb_oldschool"
    type_dict = {
            'detailed' : '/api/catalogue/detail.json?item=itemID',
            'time_data': '/api/graph/itemID.json',
            }
    
    query_url = type_dict[query_type]
    if 'itemID' in query_url and itemID is None:
        raise AttributeError('When `query_type` = ' + query_type + ' `itemID` must be defined')
    
    if itemID is not str:
        itemID=str(itemID)
        
    query_url = query_url.replace('itemID',itemID)
    full_url = base_url + query_url
    
    r = requests.get(full_url)
    json_data = r.json()
    
    if query_type is 'detailed':
        json_data = json_data['item']

    return json_data
    
my_data = grand_exchange_query('detailed',3002)
