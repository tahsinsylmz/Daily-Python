
'''

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return("You dindn't write a value.")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result : {formated_f_name} {formated_l_name}"

formated_string = format_name(input("What is your first name?"), input("What is your last name?"))
print(formated_string)

'''
from day10CalculatorArt import logo
import os

def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            def clear_screen():
                os.system('cls' if os.name == 'nt' else 'clear')

            clear_screen()
            calculator()

calculator()



# continuity = "y"
#
# def loop(n1):
#     operation = input("+\n-\n*\n/\nPick an operation: ")
#     n2 = int(input("What's the next nuber?: "))
#     result = operations[operation](n1, n2)
#     print(str(n1) + " " + operation + " " + str(n2) + " = " + str(result))
#     n1 = result
#     continuity = input("Type 'y' to continue calculating with " + str(result) + ", or type 'n' to start a new calculation: ")
#     return continuity
#
#
#
#
# while continuity == "y":
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(logo)
#     n1 = int(input("\nWhat's the firs number?: "))
#     while continuity != "n":
#         loop(n1)


'''
Console clear function:

            def clear_screen():
                os.system('cls' if os.name == 'nt' else 'clear')

            clear_screen()
'''




