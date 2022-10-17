# built in modules

# math module

import math

#constants
# pi
# eulers,s number

# ceil()
# floor()
# pow()
# factorial()
# exp()

print(math.e)
print(math.sin(45))

# functions:

# ceil()
# syntax: ceil(num)
# rounds a number up to the nearest integer
# 3.6 -> 4
print(math.ceil(3.6))
print(math.ceil(3.1))
print(math.ceil(-3.6))
print(math.ceil(-3.9))

# floor()
# syntax: floor(num)
# rounds a number down to the nearest integer
# 3.6 -> 3
print(math.floor(3.6))
print(math.floor(3.1))
print(math.floor(-3.6))
print(math.floor(-3.9))

# factorial()
# syntax: factorial (num)
# returns the factorial value ( 4 : 4*3*2*1)
# only for positive values
print(math.factorial(4))
print(math.factorial(5))



# fabs()
# float + absolute 
# returns absolute value of a given number in float data type
print(math.fabs(4.5))
print(math.fabs(-5.8))
print(math.fabs(9))
print("absolute value:",abs(9))


# exp()
# returns power of e i.e e^y
# exp(num)
y = 9
print(math.exp(y))
print(math.e**y)
print(math.exp(3.3))

# pow()
# pow(base,exp)
# return the value of base to the power of exp
# typecast values in float first and then calculate power
print(math.pow(2,4))
print(math.pow(9,2))
print(math.pow(9.1,2))
print(math.pow(9.1,0))

# fmod()
# fmod(num,deno)
# float + modulus
# returns a remainder after deviding 2 numbers
print(math.fmod(12,3.5))
# print(math.fmod(12,0))   #error
print(math.fmod(12,5))

# fsum()
# float + sum
# return the sum of all items in given iterable
# iterable can be tuple, set,list,array etc
# fsum(iterable)
l = [2,3,4,5]
print(math.fsum(l))

# prod()
# returns the product of the element from given iterable
# prod(iterable, starting_value)
print(math.prod(l))

# sqrt()
# returns the square root of a number
# sqrt(num)
# return float value
print(math.sqrt(8))
print(math.sqrt(27))

# isqrt()
# returns the square root of a number
# isqrt(num)
# return the rounded value (downword)
print(math.isqrt(8))
print(math.isqrt(27))


