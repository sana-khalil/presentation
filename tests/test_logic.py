from presentation.logic import add_numbers


def test_add_numbers():
    actual = add_numbers(3, 5)
    expected = 8
    assert actual == expected
