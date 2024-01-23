# we can get sum of array through various methods. simplest is to use sum function
"""arr = [4, 6, 2, 5]
sumArr = sum(arr)
print(sumArr)
-----------------------
However if we want to solve it using user defined function following solution will work

"""


def _sum(arr):
    sumArr = 0
    for i in arr:
        i = int(i)     # need to typecase because input function generate string list
        sumArr += i
    return sumArr


inputArr = input("enter numbers separated by comma").split(',')
print(_sum(inputArr))
