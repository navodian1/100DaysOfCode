# this is a leetcode:412. Fizz Buzz exercise:
"""Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true."""
# solution1:
# ______________________
"""
n = 15
list1 = []
for i in range(1, n + 1):
    list1.append(
        "FizzBuzz" if i % 15 == 0 else
        "Buzz" if i % 5 == 0 else
        "Fizz" if i % 3 == 0 else
        str(i)
    )

print(list1)
"""
# solution 2
# _________________________________________
n = 15
ans = []
for i in range(1, n+1):
    if i % 15 == 0:
        ans.append("FizzBuzz")
    elif i % 3 == 0:
        ans.append("Fizz")
    elif i % 5 == 0:
        ans.append("Buzz")
    else:
        ans.append('i')
print(ans)
