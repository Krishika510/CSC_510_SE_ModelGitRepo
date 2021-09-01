
# Testing

--- 

In this section we test the code of our project. 

### What are we testing? 
___
In our project we implemented 4 functionalities

    + Generating N-th number in Fibonacci Series
    + Generating the factorial of a number
    + Checking if a number is Prime or not
    + Generating the N-th Prime number
    


### How do we test?

---

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
