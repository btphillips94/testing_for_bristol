from fib import *

def test_fib_0():
    calculated_value = fib(0)
    expected_value = 1
    assert calculated_value == expected_value

def test_fib_1():
    calculated_value = fib(1)
    expected_value = 1
    assert calculated_value == expected_value
	
# def test_fib_3():	
    # calculated_value = fib(3)
    # expected_value = 5
    # assert calculated_value == expected_value