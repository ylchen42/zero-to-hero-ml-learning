import pytest
from micrograd.micrograd import Value

def test_value_add():
    a = Value(2.0)
    b = Value(3.0)
    c = a + b
    assert c.data == 5.0

def test_value_mul():
    a = Value(2.0)
    b = Value(3.0)
    c = a * b
    assert c.data == 6.0

def test_value_mul_zero():
    a = Value(2.0)
    b = Value(0.0)
    c = a * b
    assert c.data == 0.0
