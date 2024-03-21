def test_add():

    from src.calculator import add
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0
    assert add(1, -1) == 0
    assert add(1, 0) == 1
    assert add(0, 1) == 1
    assert add(0, -1) == -1
    assert add(-1, 0) == -1

def test_multiply():
    from src.calculator import multiply
    assert multiply(1, 2) == 2
    assert multiply(0, 0) == 0
    assert multiply(-1, -1) == 1
    assert multiply(-1, 1) == -1
    assert multiply(1, -1) == -1
    assert multiply(1, 0) == 0
    assert multiply(0, 1) == 0
    assert multiply(0, -1) == 0
    assert multiply(-1, 0) == 0
    assert multiply(1224, 2) == 2448
