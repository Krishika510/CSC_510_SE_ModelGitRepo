# MathFun - Software Engineering HW2b
<img src="https://github.com/Krishika510/MathFun/blob/main/MathFun/GIF0209.gif" width="300px">
<img src="https://github.com/Krishika510/MathFun/blob/main/MathFun/D6fJ.gif" width="300px">
<img src="https://github.com/Krishika510/MathFun/blob/main/MathFun/Primenumber.gif" width="300px">

[![Build Status](https://app.travis-ci.com/Krishika510/MathFun.svg?branch=main)](https://app.travis-ci.com/Krishika510/MathFun)
[![DOI](https://zenodo.org/badge/400883811.svg)](https://zenodo.org/badge/latestdoi/400883811) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <br />
MathFun is about implementation of basic problems in maths.  

# Description
Aim of this repo was to follow some guidelines on how to create a "good" Github Repo. Worked on basic Math problems with test cases.

Below are the functions and their descriptions which are in MathFun:  
**1. fibonacci(i):** This function finds the ith number in the Fibonaci series, -1 otherwise.  
**2. factorial(i):** This function return i! if i is in [1, 10], -1 otherwise.  
**3. isPrime(i):** This function returns if i is a prime number or not.  
**4. prime(i):** This function return the ith prime number if i is in [1, 100], -1 otherwise.  

# Authors
- Arpitha Vijayakumar (avijaya6@ncsu.edu)
- Ishan Bhatt (ivbhatt@ncsu.edu)
- Krishika Shivnani (kmshivna@ncsu.edu)
- Apurva Sonavane (asonava@ncsu.edu)
- Unnati Nadupalli (upnadupa@ncsu.edu)


# Testing

### What are we testing? 

In our project we implemented 4 functionalities

    + Generating N-th number in Fibonacci Series
    + Generating the factorial of a number
    + Checking if a number is Prime or not
    + Generating the N-th Prime number
    


### How do we test?

We use the  [pytest](https://docs.pytest.org/en/stable/index.html) package to test our code
        
The tests for the project are in /test/test_init.py

Steps to run tests locally
        
1. Download the project into you local computer.
2. Install the requirements.txt file on your computer

    <code> $ pip install -r requirements.txt</code>

3. Run the pytest command in the project root directory

    <code>$  pytest</code>

Expected Output:

    ================================================================ test session starts =================================================================
        platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
        rootdir: C:\MathFun
        collected 4 items                                                                                                                                     

        test\test_init.py ....                                                                                                                          [100%]

    ================================================================= 4 passed in 0.07s ==================================================================


