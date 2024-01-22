# Factorial of a Number
"""
solution1: using inbuilt function

import math


def factorial(num):
    return math.factorial(num)


input1 = 6
print(f"factorial of {input1} is {factorial(input1)}")
---------------------------------------------------------------
solution2: using ternary operator

def factorial(num):
    return 1 if (num == 1 or num == 0) else num * factorial(num - 1)


input1 = float(input("enter a number to find factorial:"))
print(f"factorial of {input1} is {factorial(input1)}")
----------------------------------------------------------------
solution3: using numpy

import numpy


input1 = int(input("enter a number to find factorial:"))
factorial = numpy.prod([i for i in range(1, input1+1)])
print(f"factorial of {input1} is {factorial}")
"""


def factorial(num1):
    result = 1
    for i in range(2, num1 + 1):
        result *= i
    return result


input1 = int(input("enter a number to find factorial:"))
print(f"factorial of {input1} is {factorial(input1)}")
