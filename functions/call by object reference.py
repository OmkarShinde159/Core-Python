''''
def fun(lst):
    return lst
l = [5,6,7,8,9]
l1 = fun(l)
print(l1)


def con_add(n1,n2):
    return n1 + n2

x = con_add(12,23)
print(x)
x = con_add(12,23.5)
print(x)
y = con_add('python','language')
print(y)
# z = con_add('p',9)
# print(z)      error

l = [12,23,34,45]
l1 = [45,56,78]
print(con_add(l,l1))

x = 45.5
y = 9
z = 'python'
b = True

def con(a,b):
    a = str(a)
    b = str(b)
    return a+b
print(con(x,y))
print(con(x,5))
print(con(y,89))
print(con(z,x))
print(con(z,b))

def fun(a):
    return a
d = {1:'Pooja', 2:'Manisha', 3:'Omkar'}
print(fun(d))
print(type(fun))
print(type(fun(d)))

# call by object reference
def num(a):
    print(a)
    a = 78   # break connection with object refrence
    print(a)
x = 6
print(id(x))
num(x)

y = 'python'
num(y)
# print(id(a))
'''
# int
# stiring
# list = mutable

def fun(lst):
    print(lst)
    lst[2] = 5
    print(lst)

l = [1,2,3,4,5,6]
print(l)
fun(l)
print(l)


# def fun(s):
#     s[2] = 5
#     print(s)


# def func(lst):
#     print(lst)
#     lst = [5,6,7,8]
#     print(lst)
# func(l)
# print(l)

  
























