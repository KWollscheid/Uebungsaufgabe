a = "foo"
b = "bar"


def concatenation(a, b):
    return str(a)+str(b)


def test_concatenation():
    assert concatenation(a, b) == "foobar"
