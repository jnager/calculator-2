"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Enter into the loop of operators.  Q will break you out of the loop.

while True:
    print "Enter your operation and numbers: Ex: + 2 3 or q to quit"
    input = raw_input(">> ")
    tokens = input.split(" ")
    #User enters q and breaks out of while loop   
    if tokens[0] == 'q':
        break
    #turning inputs into floats based on number of tokens
    num1 = float(tokens[1])
    if len(tokens) > 2:
        num2 = float(tokens[2])
    #cases to run
    if tokens[0] == '+':
        print add(num1, num2)
    elif tokens[0] == '-':
        print subtract(num1, num2)
    elif tokens[0] == '*':
        print multiply(num1, num2)
    elif tokens[0] == '/':
        print divide(num1, num2)
    elif tokens[0] == 'square':
        print square(num1)
    elif tokens[0] == 'cube':
        print cube(num1)
    elif tokens[0] == 'pow':
        print power(num1, num2)
    elif tokens[0] == 'mod':
        print mod(num1, num2)