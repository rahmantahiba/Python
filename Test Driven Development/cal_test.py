"""

Calculation Check Tests 

"""

def another_sum(a,b):
    return a + b

def test_another_sum():
    assert another_sum(3,2) == 5

def another_sub(c,d):
   return c -d 

def test_another_sub():
    assert another_sub(0,0) == 0 #Test will fail if the assert is false 

def another_multiply(e,f):
    return e * f

def test_another_multiply():
    assert another_multiply(4,4) == 16

def another_division(g,h):
    return g/h

def test_another_division():
    assert another_division(4,2) != 0
