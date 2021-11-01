"""Configure elasticsearch connection"""

import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections

ELASTICSEARCH_USER = os.getenv('ELASTICSEARCH_USER', 'elastic')
ELASTICSEARCH_PASSWORD = os.getenv('ELASTICSEARCH_PASSWORD', 'xxx')
ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')
ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT', '9200')

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
