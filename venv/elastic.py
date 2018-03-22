import json, requests
from datetime import datetime
from elasticsearch import Elasticsearch
class ElasticOps(Elasticsearch):
    def __init__(self):
        pass

    def authenticate(self):
        pass
        
'''
resp = requests.get("http://swapi.co/api/planets/2")
obj = ElasticOps()
obj.index(index="asd",doc_type="asdd",id=2,body=json.loads(resp.content))
'''
