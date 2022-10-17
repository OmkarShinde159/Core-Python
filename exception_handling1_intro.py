# packages
# packages is nothing but a directory/ folder of python that contains
# an additional file whis is __init__.py
# which distinguishes a package from a directory
# __init__.py
# built in packages - numpy, pandas, matplotlib etc
# user defined packages

# Exception handling
# Unwanted or enexpected event that interupts the normal execution
# flow of our program is called as Exception
# Exception is a run time error


# Types of exception
# 1. Built in exception (SyntaxError & LogicalError)
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # ValueError
    # IndexError
    # ZeroDivisionError

# 2. User defined exception

# All built in exceptions are represented as classes in python
# The base class for all builtins exception is BaseException class
# check Exception hierarchy

# Need of exception handling
# suddenly termination of a program
# because of data loss

# exception handling
# the mechanism of handling unexpected error/exception in a program 
# is called as exception handling
# we use exception handling so that the normal execution flow of our
# program can be maintained

# block - try, except, else, finally
# similar to if elif else principle

# syntax

# try: contains code which may cause exception
# except: is used to handle an exception that is raised in try block
'''
try:
    body of try Block
except:
    body of except block
'''
# NameError
p = 89
try:
    print(p)
except:
    print("P is not defined")

print("Program run after exception handling")


# IndexError
l = [1,2,3,4,5]
try:
    i = 0
    while True:
        print(l[i])
        i += 1
except:
    print("Index out of range")



# TypeError
try:
    x = int(input("Enter integer: "))
    y = int(input("Enter integer: "))
    print(x/y)
except:
    print("Entered value is not integer")


x = "Python"
y = 34
try:
    z = x/y
    print(z)
except:
    print("Cannot devide str and int")

# we can define multiple or more than except blocks for a single try block
# so handle different different types of exceptions
    
try:   
    x = int(input("Enter integer: "))
    y = int(input("Enter integer: "))
    print(x/y)
except ValueError:
    print("Enteref value should be integer type")
except ZeroDivisionError:
    print("Divison by zero is not possible")

    