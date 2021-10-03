import pytest

from hello.db import get_es_connection
from hello.exceptions import HelloWorldException
from hello.indices import get_indices
from testing.utils import (create_test_index, get_test_index_name,
                           remove_test_index)


def test_no_connection():
    with pytest.raises(HelloWorldException):
        get_indices(None)


def test_get_indices():
    es = get_es_connection()
    create_test_index(es, 'foo', {})
    create_test_index(es, 'bar', {})

    indices = get_indices(es)
    assert get_test_index_name('foo') in indices
    assert get_test_index_name('bar') in indices

    remove_test_index(es, 'bar')
    remove_test_index(es, 'foo')
