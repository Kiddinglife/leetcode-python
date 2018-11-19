# -*- coding: utf-8 -*-

"""
斐波纳契数列以如下被以递推的方法定义：
F(1)=1，F(2)=1, F(3)=2,F(n)=F(n-1)+F(n-2)（n>=4，n∈N*）
fib(3)
    fib(2) 
        fib(1)
            return 1
        +
        fib(0)
            return 0
        return 1
    + 
    fib(1)
        return 1
    return 2
"""


def fib_v1(n):
    if n <= 1:
        return n
    return fib_v1(n-1) + fib_v1(n-2)

# Function to calculate nth Fibonacci number 
def fib_v2(n, lookup): 
    if n == 1 or n == 0:
        lookup[n] = n
    if lookup[n] is None:
        lookup[n] = fib_v2(n-1, lookup) + fib_v2(n-2, lookup)  
    return lookup[n]

def fib_v3(n):
    lookup = [0]*(n+1)
    lookup[1] = 1
    for i in range(2, n+1):
        lookup[i] = lookup[i-1] + lookup[i-2]
    return lookup[-1]

def fib_v4(n):
    v1
    pass

def test_fib_v2():
    n = 34 
    # Declaration of lookup table 
    # Handles till n = 100  
    lookup = [None]*(101) 
    print("Fibonacci Number is ", fib_v2(n, lookup))

def test_fib_v1():
    assert(fib_v1(4) == 3)

