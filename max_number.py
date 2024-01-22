# Find Maximum of two numbers in Python
"""
solution 1: using inbuilt max function
num1 = 20
num2 = 41
maximum = max(num1, num2)
print(maximum)
------------------------------------------------
Solution 2: using ternary operator
num1,num2=20,41
print(num1 if num1>=num2 else num2)

we can also use sort function to find max in list value, however time complexity may impact, better to avoid
"""
# solution 3

def max_value(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


input1 = float(input("enter first number to compare:"))
input2 = float(input("enter second number to compare:"))
maximum = max_value(input1,input2)
print(f"value of {maximum} is maximum among your input {input1} and {input2}")
