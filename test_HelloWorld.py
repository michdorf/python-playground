import pytest
import HelloWorld

def f(number):
    return number+1

def test_f():
    assert f(2) == 3

def test_allan():
    assert HelloWorld.ALLAN == "et navn"