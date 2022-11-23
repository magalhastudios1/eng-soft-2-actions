import calculator

def test_addition():
    assert calculator.addition(2, 3) == 5

def test_subtraction():
    assert calculator.subtraction(2, 3) == -1

def test_multiplication():
    assert calculator.multiplication(2, 3) == 6

def test_division():
    assert calculator.division(2, 3) == 0