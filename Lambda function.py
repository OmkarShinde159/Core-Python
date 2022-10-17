# lambda function
# it is a type of function
# lambda function has no name thats why it called annonymous function and also called as single line
# executed function
# it is used for small execution only
# a lambda function can take any number of arguments but can only have one expression

# syntax"
# f = Lambda arguments : expression
# f(argument_value)

s = 'Python'
l = lambda s: print(s)
l(s)

a = lambda p : p
p = a(5)
print(p)
# or
print(a(5))

# assign zero variable
w = lambda : print('hello world')
w()

# addition without lambda
def add(a,b):
    return a+b
print(add(5,6))
# addition with lambda

add = lambda a,b : a+b
print(add(5,7))

# square of a number
# sq is a function variable which is used to call the function
sq = lambda a : a**2
print(sq(5))

# use value in variable
b = 8
sub = lambda a: a-b
print(sub(5))
# print(a) >> returns memory location instead of error


# create a table using lambda
tab = lambda n : n*i

for i in range(1,11):
    print(tab(5))


table = lambda a,b : a*b
n = int(input("Enter number: "))
for i in range(1,11):
    t = table(n,i)
    print(t)


# single line execution
(lambda x : print(x))(21)

(lambda x,y : print(x**2))(21,2)

(lambda x,y=9 : print(x*y))(10)

(lambda x,y : print(x*y))(10,20)

ret = (lambda x: x)(21)
print(ret)
# this variable only stores the return value of function
# ret(6)    >> error

# using variable length arguments

list1 = [2,6,7,8]
list2 = [90,78,78,6]


add = lambda *args : sum(args)
print(add(*list1))
print(add(*list1,*list2))

# WAP to display last digit of given number using lambda function

n = lambda x : x%10
print(n(123))


