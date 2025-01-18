import pytest

def sqaure(n):
    return n**2
def cube(n):
    return n**3
def fif_pow(n):
    return n**5

def test_sqaure():
    assert sqaure(2)==4 , "Test failed,Sqaure of 2 is 4"
    assert sqaure(5)==25, "Test Failed"

def test_cube():
    assert cube(3)==27,"Test Failed"

def test_fif_pow():
    assert fif_pow(2)==32,"Test Failed: Fifth power of 2 is 32"

def test_invalid_input():
    with pytest.raises(TypeError):
        sqaure("string")