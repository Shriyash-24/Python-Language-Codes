def func():
    """
    This is a docstring
    We can write what the function is supposed to do.
    :return: None
    """
    return None
func() # ~ Does nothing.

print(help(func)) # help() can give details about any function.

def divide(num1, num2):
    """
    num1: A number to be divided ( numerator )
    num2: A number to be divided ( denominator )
    :return: float (if num2 is non-zero) OR str (if num2 is 0)
    """
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        result = num1 / num2
        return result
print(help(divide)) # Prints docstring
help(divide) # Prints docstring ~ No need for print

# Docstring should be first thing in function definition.
# help() can also be used for built-in functions.