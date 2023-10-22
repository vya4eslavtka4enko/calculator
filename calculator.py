from logo import logo
import os
# arithmetic
def add(number1,number2):
    return number1+number2
def subtract(number1,number2):
    return number1-number2
def multiply(number1,number2):
    return number1*number2
def divide(number1,number2):
    return number1/number2

print(logo)

operations = {
    "+": add,
    "-": subtract,
    '*': multiply,
    '/': divide
}


num1=int(input("what's the first number "))
should_continue=True
# os.system('clear')
while should_continue == True:
     operation_symbol=input('Pick an operation ')
     calculation_function = operations[operation_symbol]
     num2=int(input("what's the second number "))
     result = calculation_function(num1,num2)
     print(f"{num1}   {operation_symbol}  {num2}  =  {result}")
     if input(f"type to continue calculating with {result} or type 'n' to exit") =='y':
         num1=result
     else:
         should_continue = False