'''
x = 15.0
y = 15/2
z = 8 

var = x > y 
print(var)

var = z < y 
print(var)

var = x == z 
print(var)

var = x != 15 
print(var)

var = x >= z
print(var)

var = y <= z
print(var)

var = 6.3199 == (6.3199*2)/2
print(var)

print("--------string comparison result---------")

x = "Python"
y = "Developer"

print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

print("--------logical operator result---------")

x = 5 > 2
y = 4 < 6
print("and: ", x and y)

x = 5 > 5
y = 4 < 6
print("or :", x or y)

x = 5 > 0 # True
y = False

print(x)
print(y)
print(not( x and y)) 
print(not( x or y))


print("--------identity operator result---------")
a = 10
b = 10
c = 20
print(id(a))  # a and b have same memory location
print(id(b))
print(id(c)) 
print(a is b)
print(a is c)
print(b is c)
print(a is not b)
print(a is not c)
print(b is not c)

print("--------membership operator result---------")
p = "Python"
print("y" in p)
print("s" in p)

'''
print("-------operator precedence---------")
a = 20
b = 10
c = 15
d = 5 
e = 0 

e = ((a+b)*c)/d 
print(e)

e = (a+b)*c/d 
print(e)

e = (b*c)/(c//d) 
print(e)

e = a+(a*b)+c/d 
print(e)

x = (7+3)/(8*2)*(7-2)+78-9/2
print(x)
