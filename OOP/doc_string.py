# string
# docstring
# rawstring

# ''' or """"
# square
# we cannot acces comments whereas
# we can access docstrings
# written inside the function
def fun(n):
    '''square'''
    return n*n
print(fun(4))

# __doc__(access)
# function_name.__doc__
print(fun.__doc__)

# multiline docstring
def add(a,b):
    '''
    2 parameters:
        for addition
    '''
    return a+b
print(add(12,2))
print(add.__doc__)



# raw string
# r"string"
# generrally used in file handling to specify path as it is
# removes the functionality of a character inside the string
# and print the string as it is 

print('Pythin\nProgramming')
p = "C: \\Desktop"
print(p)

print(r'Pythin\nProgramming')
p1 = r'C: \\Desktop'
print(p1)


