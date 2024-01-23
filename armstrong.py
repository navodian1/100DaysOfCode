# Program to Check Armstrong Number
"""
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits
approach1: using string manipulation
-----------------------------------------------------------------
def armstrong(num):
    str_num = str(num)
    n = len(str_num)
    sum_digit = 0
    for digit in str_num:
        sum_digit += int(digit) ** n
    if sum_digit == num:
        return True
    else:
        return False


input1 = int(input("enter number to check if it is armstrong number:"))
print(f"is entered number is armstrong number? ans: {armstrong(input1)}")

--------------------------------------------------------------
Time Complexity: O(log(num))
Space Complexity: O(log(num))
Auxiliary Space: O(1)


approach2: digit by digit sum
"""

import math


def armstrong(num):
    temp = num
    num_digits = 0
    sum_digit = 0

    while temp > 0:
        temp //= 10
        num_digits += 1
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_digit += math.pow(digit, num_digits)
        temp //= 10
    if sum_digit == num:
        return True
    else:
        return False


input1 = int(input("enter number to check if it is armstrong number:"))
print(f"is entered number is armstrong number? ans: {armstrong(input1)}")
