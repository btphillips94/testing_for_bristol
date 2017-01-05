from sinc2d import *

def test_one():
    x = 0
    y = 0
    calc_val = sinc2d(x,y)
    exp_val = 1
    assert calc_val == exp_val
	
def test_two():
    x = 0
    y = 2
    calc_val = sinc2d(x,y)
    exp_val = np.sin(2)/2
    assert calc_val == exp_val
	
def test_three():
    x = 2
    y = 0
    calc_val = sinc2d(x,y)
    exp_val = np.sin(2)/2
    assert calc_val == exp_val
	
def test_four():
    x = 2
    y = 2
    calc_val = sinc2d(x,y)
    exp_val = (np.sin(2)/2) * (np.sin(2) / 2)
    assert calc_val == exp_val