from logo import logo
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
num2=int(input("what's the second number "))

for sumbol in operations:
    print(sumbol)
operation_symbol=input('Pick an operation frome the line above  ')
calculation_function = operations[operation_symbol]

result = calculation_function(num1,num2)
    


print(f"{num1}   {operation_symbol}  {num2}  =  {result}")