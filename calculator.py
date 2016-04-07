"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Enter into the loop of operators.  Q will break you out of the loop.

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
def test_me(listy):
    # Checking to see if entire string past 1st space is valid (only numbers)
        valid_iterable = True

        for i in range (1, len(listy)-1):
            
            if is_number(listy[i]):
                pass
            else:
                valid_iterable = False
    
        return valid_iterable



while True:
    print "Enter your operation and numbers: Ex: + 2 3 or q to quit"
    input = raw_input(">> ")
    nums = []

    tokens = input.split(" ")
    #User enters q and breaks out of while loop   
    if tokens[0] == 'q':
        break
    #turning inputs into floats based on number of tokens
    


    #Construct list of numbers from string input
    if test_me(tokens):
        for i in range (1, len(tokens)-1):
            nums.append(float(tokens[i]))
    else:
        print "Entry was not valid!"

    print nums
"""
    #Cases to run
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
"""