from hello.exceptions import HelloWorldException


def get_indices(es):
    if not es or not es.ping():
        raise HelloWorldException('Provide valid es connection')

    return list(es.indices.get_alias().keys())
