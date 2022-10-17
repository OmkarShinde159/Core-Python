# WAP to display last digit of given number using lambda function
n = lambda x : x%10
print(n(123))

# lambda arg : body of if if condition else body of else

# WAP to check if num is divisible by 5 or not using lambda
n = lambda x: print('divisible by 5') if x%5==0 else print("not divisible by 5")
print(n(16))



# WAP to find greatest number among 3 numbers using lambda function

#g = lambda x,y,z : print(x,"is greater" ) if x>y and x>z else (print(y,"is greater") if y>x and y>z else print(z,'is greater) else print(z,"is greater")
#g(1,2,3)


# WAP to pass percentage of lambda function and print pass or fail
per = lambda x : print('pass') if x>35 else print('fail')
per(40)

# lambda arg: body of if if cond else (body of if if cond else (body of if if cond else body of else))

greater = lambda a,b,c:("a is greater" if a>c else"c is greater") if a>b else ("b is greater" if b>c else "c is greater")
print(greater(12,3,2))
print(greater(12,13,11))
print(greater(12,12,33))


# WAP to display you are eligible for college if age is greater than 18 and per is greater than 65
# else  display you are not eligible and
# if age is less than 18 display you are not qualifies
# using lambda function 

elegible = lambda a,p: ('eligible' if p>65 else 'not eligible') if a>18 else ('not qualified' if a<18 else "not qualified") 
print(elegible(22,66))


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

l = lambda x,y: add(x,y)
print(l(12,3))

s = lambda x,y: print(sub(x,y))
s(12,3)
print(s(12,3))

l = lambda x,y: print('addition of',x,'and',y,'is',add(x,y))
l(12,3)

s = lambda x,y: print('subtraction of',x,'and',y,'is',sub(x,y))
s(12,3)
#print(s(12,3))

l = lambda x,y: ('addition of',x,'and',y,'is:',add(x,y))
print(l(12,3))

s = lambda x,y: ('subtraction of',x,'and',y,'is:',sub(x,y))
print(s(12,3))

def add1(a,b,c):
    return a+b+c

add = lambda: add1(12,13,12)
print(add())



# lambda function inside user defined function

def fun(n):
    return lambda a: a+n
x = fun(12)
print(x(3))

'''
def fun1(a,b):
    return lambda a,b: 'a is greater' if a>b else 'b is greater'
max = fun1(a,b)
print(max(12,14))
'''

min = lambda a : a
def fun11():
    print(min(12))
fun11()

def fun12():
    return min(13)
print(fun12())

def fun13(l):
    return min(l)
print(fun13(4))

min1 = lambda x,y : 'x is less' if x<y else 'y is less'

def min_fun(a,b):
    return min1(a,b)
print(min_fun(12,23))
print(min_fun(23,12))
























