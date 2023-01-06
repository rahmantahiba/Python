"""

Yet another math test but more on inequalities

"""

def greater_than(a,b):
   return a > b

def test_greater_than():
    assert greater_than(4,2) == True

def less_than(c,d):
    return c < d

def test_less_than():
    assert less_than(6,2) == False

def greater_than_equal(e,f):
    return e >= f

def test_greater_than_equal():
    assert greater_than_equal(2,2) == True

def less_than_equal(g,h):
    return g <= h

def test_less_than_equal():
    assert less_than_equal(12,11) == False

def equal(j,k):
    return j == k

def test_equal():
    assert equal(4,4) == True

def not_equal(l,m):
    return l != m

def test_not_equal():
    assert not_equal(16,17) == True