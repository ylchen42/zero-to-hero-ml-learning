import pytest
from micrograd.micrograd import Value

def test_value_add():
    a = Value(2.0)
    b = Value(3.0)
    c = a + b
    assert c.data == 5.0
    assert c._children == {a, b}
    assert c._op == "+"

def test_value_mul():
    a = Value(2.0)
    b = Value(3.0)
    c = a * b
    assert c.data == 6.0
    assert c._children == {a, b}
    assert c._op == "*"

def test_value_mul_zero():
    a = Value(2.0)
    b = Value(0.0)
    c = a * b
    assert c.data == 0.0
    assert c._children == {a, b}
    assert c._op == "*"

def test_value_add_same_value():
    a = Value(2.0)
    b = a + a
    assert b.data == 4.0
    assert b._children == {a}
    assert b._op == "+"

def test_value_mul_same_value():
    a = Value(2.0)
    b = a * a
    assert b.data == 4.0
    assert b._children == {a}
    assert b._op == "*"
