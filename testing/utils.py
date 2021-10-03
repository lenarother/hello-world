from elasticsearch.helpers import bulk


def create_test_index(es, index, mappings, test_data=None):
    index = f'test-{index}'
    if es.indices.exists(index=index):
        es.indices.delete(index=index)
    es.indices.create(index=index, body=mappings)
    if test_data:
        bulk(es, test_data, index=index)
    es.indices.refresh(index)


def remove_test_index(es, index):
    index = f'test-{index}'
    if es.indices.exists(index=index):
        es.indices.delete(index=index)


def get_test_index_name(index):
    return f'test-{index}'
