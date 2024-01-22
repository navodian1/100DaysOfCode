# numbers can be added by different ways in python depends on what you prefer

"""
# using + operator is very common method
num1 = 15        # you can take input from user using num1=float(input("enter first number"))
num2 = 20
addition = num1 + num2
print(f"sum of {num1} and {num2} is {addition}")
"""


# _____________________________________________________________
# with the help of the defined function
def addition(num1, num2):
    return num1 + num2


first_num = int(input("enter first number:"))
second_num = int(input("enter another number:"))
result = addition(first_num, second_num)
print(f"addition of your first value:{first_num} and second value:{second_num} is {result}")

"""
in above program it is considered that user will enter integer as input, 
you can also use float type conversion during input and try exception block to enhance validation

"""