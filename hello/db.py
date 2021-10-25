"""Configure elasticsearch connection"""

import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections

ES_USER = os.getenv('ES_USER', 'elastic')
ES_PASSWD = os.getenv('ES_PASSWD', 'xxx')
ES_HOST = os.getenv('ES_HOST', 'localhost')
ES_PORT = os.getenv('ES_PORT', '9200')

_es = None


def get_es_connection():
    global _es

    if not _es:
        _es = Elasticsearch(
            hosts='elasticsearch:9200',
            http_auth=(ES_USER, ES_PASSWD)
        )
        # _es = Elasticsearch('elasticsearch:9200',)
        #     #http_auth=(ES_USER, ES_PASSWD)
        # connections.add_connection('default', _es)

    return _es
