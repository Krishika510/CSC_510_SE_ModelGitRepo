import os
import sys
import sys
sys.path.insert(0, '/MathFun/MathFun')

import MathFun

def test_fibonacci():
    assert fibonacci(-8) == -1
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_factorial():
    assert factorial(-1) == -1,"Negative numbers should yield -1 for all, they do not have a factorial"
	assert factorial(-2) == -1,"Negative numbers should yield -1 for all, they do not have a factorial"
	assert factorial(0) == 1,"Factorial of 0 or 1 should be 1, the output is something else"
	assert factorial(1) == 1,"Factorial of 0 or 1 should be 1, the output is something else"
	assert factorial(2) == 2,"Factorial of 2 is 2, the output is something else"
    assert factorial(20) == -1,"Anything above 10 is -1, we have a restricted range"
    assert factorial(4) == 24,"Factorial of 4 is 24, the output is something else"

def test_isPrime():
    assert isPrime(-1) == False,"-1 is neither prime nor composite"
	assert isPrime(0) == False,"0 is neither prime nor composite "
    assert isPrime(1) == False,"1 is neither prime, nor composite"
    assert isPrime(2) == True,"2 is neither prime, nor composite"
    assert isPrime(10) == False,"10 is a composite number, the output is wrong"
    assert isPrime(11) == True,"11 is a prime number, the output is wrong"
    assert isPrime(13) == True,"13 is a prime number, the output is wrong"

def test_prime():
    assert prime(-1) == -1
    assert prime(1) == 2
    assert prime(5) == 11
    assert prime(101) == -1

