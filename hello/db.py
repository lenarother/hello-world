"""Configure elasticsearch connection"""

import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections

ELASTICSEARCH_USER = os.getenv('ES_USER', 'elastic')
ELASTICSEARCH_PASSWORD = os.getenv('ES_PASSWD', 'xxx')
ELASTICSEARCH_HOST = os.getenv('ES_HOST', 'elasticsearch')
ELASTICSEARCH_PORT = os.getenv('ES_PORT', '9200')

_es = None


def get_es_connection():
    global _es

    if not _es:
        _es = Elasticsearch(
            hosts=f'{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}',
            http_auth=(ELASTICSEARCH_USER, ELASTICSEARCH_PASSWORD)
        )
        if _es.ping():
            connections.add_connection('default', _es)

    return _es
