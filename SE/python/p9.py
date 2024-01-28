'''
Take as input two numbers a, b with following conditions:
1. Assert that the number a should be even
2. Raise user defined OutOfBounds error if the number b is less than 1 or greater than 10
3. Raise predefined "ZeroDivisionError" error for a/b
4. Display a Thank You message irrespective of the outcome of program
'''

class OutOfBoundsError(Exception):
    def __init__(self, msg):
        msg="Number 'b' is out of bounds (should be between 1 and 10)."

a = int(input("Enter an even number (a): "))
b = int(input("Enter a number between 1 and 10 (b): "))

try:
    assert a % 2 == 0, "Number 'a' should be even."
    if b < -10 or b > 10:
        raise OutOfBoundsError
    c = a / b
    print("The result of division is: ", c)
except AssertionError as e:
    raise AssertionError(e)
except ZeroDivisionError:
    raise ZeroDivisionError("Division by zero is not allowed.")
except OutOfBoundsError as e:
    print(e)
finally:
    print("Thank You")