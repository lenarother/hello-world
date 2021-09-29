from hello.hello_world import hello_world


def smoke_test():
    assert 1 == 1


def test_hello_world():
    assert hello_world() == 'Hello world!'
