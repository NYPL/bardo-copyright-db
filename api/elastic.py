import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

class Elastic():
    def __init__(self):
        self.client = None
    
    def init_app(self, app):
        host = f'{os.environ["ES_HOST"]}:{os.environ["ES_PORT"]}'
        self.client = Elasticsearch(hosts=[host])
    
    def create_search(self, index):
        return Search(using=self.client, index=index)

    def query_regnum(self, regnum, page=0, perPage=10):
        startPos, endPos = Elastic.getFromSize(page, perPage)
        search = self.create_search('cce')
        nestedQ = Q('term', registrations__regnum=regnum)
        nestedSearch = search.query('nested', path='registrations', query=nestedQ)[startPos:endPos]
        return nestedSearch.execute()
    
    def query_rennum(self, rennum, page=0, perPage=10):
        startPos, endPos = Elastic.getFromSize(page, perPage)
        search = self.create_search('ccr')
        renewalSearch = search.query('term', rennum=rennum)[startPos:endPos]
        return renewalSearch.execute()
    
    def query_fulltext(self, queryText, page=0, perPage=10):
        startPos, endPos = Elastic.getFromSize(page, perPage)
        print(startPos, endPos)
        search = self.create_search('cce,ccr')
        renewalSearch = search.query('query_string', query=queryText)[startPos:endPos]
        return renewalSearch.execute()
    
    @staticmethod
    def getFromSize(page, perPage):
        startPos = page * perPage
        endPos = startPos + perPage
        return startPos, endPos

elastic = Elastic()