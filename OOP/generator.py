# generator
# generator is a special function which stores the value in a function
# insted of returns an iterator object in a sequence
# generator object becomes empty after extracting values


# iterator
# iterable
# next(), next(iterator, default_return_value)


def gen_fun():
    yield 25
    yield 35 
    yield 45

print(gen_fun())
print(list(gen_fun()))

for i in gen_fun():
    print(i)

print(gen_fun())
x = gen_fun()
print(next(x))
print(next(x))
print(next(x))
print(next(x,100)) # generator become empty here and return default end value




def gen_fun1():
    print("using retun")
    return 25
    return 35
    return 45

print(gen_fun1())
# print(list(gen_fun1()))

# for i in gen_fun1():
#     print(i)

def hello_user(name):
    yield "Hello "+name

h = hello_user("Manisha")
print(tuple(h))

def gen_fun2(a,b):
    yield "Omkar",a
    yield "Number",b
    return 25
    yield "not execute"

f =gen_fun2("shinde",15)
print(list(f))
print(f)

def gen_num(n):
    for i in range(1,n+1):
        yield i

print(list(gen_num(10)))

def fibo_series(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        yield c
        a = b
        b = c
        c = a+b
        
print(list(fibo_series(15)))

n1 = (fibo_series(10))
print(next(n1))
print(next(n1))
print(next(n1))
print(next(n1))
print()
for i in n1:
    print(i)
print(list(n1))

# n1 becomes empty after extracting all values

# iter() function
# convert iterable into iterator
# iter(iterable)
# list iterator object

l = [1,2,3,4,65]
print(l)
iter1 = iter(l)
n = iter1
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n,15))
print(next(n,20))  # end value

