from sub_project.my_module import add


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_float_numbers():
    assert add(2.5, 3.5) == 6.0
