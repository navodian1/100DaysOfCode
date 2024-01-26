import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():

        number1 = float(input("enter first number: "))
        for symbol in operations_dict:
            print(symbol)
        continue_flag = True
        while continue_flag:
            op_symbol = input("Pic a symbol to perform calculation: ")
            number2 = float(input("Enter next number: "))
            calculator_function = operations_dict[op_symbol]
            output = calculator_function(number1,number2)
            print(f"{number1}{op_symbol}{number2} = {output}")
            should_continue = input(f"enter 'Y' if you want to continue calculation with {output} else 'n' to start a new "
                                    f"calculation, 'x' to exit ").lower()
            if should_continue == 'y':
                number1 = output
            elif should_continue == 'n':
                continue_flag = False
                os.system('cls' if os.name == 'nt' else 'clear')
                calculator()
            else:
                continue_flag = False
                print("thank you for using calculator")
calculator()