import os
import sys
# sys.path.append("../Mathfun")
# import MathFun
def fibonacci(i):
	"""
	This function finds the ith number in the Fibonaci series, -1 otherwise.
	"""
	if i <= 0:
		return -1
	if i <= 2:
		return 1

	prev = 1
	curr = 1

	for k in range(i-2):
		temp = curr
		curr += prev
		prev = temp

	return curr


def factorial(i):
	"""
	This function return i! if i is in [1, 10], -1 otherwise.
	"""

	if i <=0 or i >10:
		return -1

	curr = 1
	for k in range(2, i+1):
		curr *= k

	return curr

def isPrime(i):
	"""
	This function returns if i is a prime number or not.
	"""
	if i <= 1:
		return False

	for k in range(2, int(i**0.5)+1):
		if i%k == 0:
			return False
	return True

def prime(i):
	"""
	This function return the ith prime number if i is in [1, 100], -1 otherwise.
	"""

	if i <=0 or i >100:
		return -1


	primesSoFar = 0
	num = 2

	while primesSoFar < i:
		if isPrime(num):
			primesSoFar+=1
		num+=1

	return num-1

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

