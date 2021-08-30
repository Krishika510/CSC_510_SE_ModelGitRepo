import os
import sys
from MathFun.MathFun.MathFun import *


def test_fibonacci():
    assert fibonacci(-8) == -1
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_factorial():
    assert factorial(-1) == -1
    assert factorial(20) == -1
    assert factorial(4) == 24

def test_isPrime():
    assert isPrime(-1) == False
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(10) == False
    assert isPrime(11) == True

def test_prime():
    assert prime(-1) == -1
    assert prime(1) == 2
    assert prime(5) == 11
    assert prime(101) == -1

