from elasticsearch import Elasticsearch
import json, requests
def mirror_to_elastic(db_name, table_name, data):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    
    r = requests.get('http://localhost:9200') 
    if r.status_code == 200:
        es.index(index='{}'.format(db_name), doc_type='{}'.format(table_name), body=data)

    
