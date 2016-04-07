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
        valid_numbers = True
        for i in range (1, len(listy)):       
            if is_number(listy[i]):
                pass
            else:
                valid_numbers = False
        return valid_numbers



while True:
    print "Enter your operation and numbers: Ex: + 2 3 or q to quit"
    input = raw_input(">> ")
    nums = []

    tokens = input.split(" ")
    #User enters q and breaks out of while loop   
    if tokens[0] == 'q':
        break

    #Construct list of numbers from string input
    if test_me(tokens):
        for i in range (1, len(tokens)):
            num_to_add = float(tokens[i])
            nums.append(num_to_add)
    else:
        print "Entry was not valid!"

    #Cases to run, adding a try catch to grab too large calculations
    try:
        if tokens[0] == '+':
            print "{:.2f}".format(reduce(add, nums))
        elif tokens[0] == '-':
            print "{:.2f}".format(reduce(subtract, nums))
        elif tokens[0] == '*':
            print "{:.2f}".format(reduce(multiply, nums))
        elif tokens[0] == '/':
            print "{:.2f}".format(reduce(divide, nums))
        elif tokens[0] == 'square':
            if len(nums) > 1:
                print "You can only square one number."
            else:
                print square(nums[0])
        elif tokens[0] == 'cube':
            if len(nums) > 1:
                print "You can only cube one number."
            else:
                print cube(nums[0])
        elif tokens[0] == 'pow':
            print "{:.2f}".format(reduce(power, nums))
        elif tokens[0] == 'mod':
            print "{:.2f}".format(reduce(mod, nums))
    except OverflowError:
        print "Your calculation was too large. TOO BAD SO SAD."