from sonicdf import SonicDF
from nose.tools import *

def test_typecheck_int():
    s = SonicDF()
    assert s.checkType(3,int) == True

def test_typecheck_not_float():
    s = SonicDF()
    assert s.checkType(3,float) == False

def test_type_array():
    s = SonicDF()
    assert s.checkType([3,4], [int, int]) == True

def test_type_array_single():
    s = SonicDF()
    assert s.checkType([3,4], [int]) == True

def test_type_mixed_array():
    s = SonicDF()
    assert s.checkType([3,'helo'], [int, str]) == True

def test_type_mixed_array_fail():
    s = SonicDF()
    assert s.checkType([3,'helo'], [int, int]) == False

@raises(Exception)
def test_type_raises_exception():
    s = SonicDF()
    s.checkType([3,'helo', 4.0], [int, int])
