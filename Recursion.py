# recursion

def num(n):
    print(n)
    if n==0:
        return
    else:
        num(n-1)

#num(5)

# WAP to print factorial using recursion n(n-1)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1) #5*4=20

print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))

#2. WAP tp print factorial only if given number is positive if entered number is negative
# print entered number is negative we cannot find factorial of a given number.

def fact(n):
    if n>0:
        return n*fact(n-1)
    elif n==0:
        return 1
    else:
        return "cannot find factorial of a negative number"

print(fact(-1))
print(fact(0))
print(fact(5))

# 3. WAP to print fibonacci series upto passed number in function call using recursion.

# without recursion
def fibo(n):
    a = 0
    b = 1
    c = 0
    for i in range(c,n):
        print(c)
        a=b
        b=c
        c = a+b

#fibo(8)

# with recursion use (n-2)+(n-1)
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

n = 10
for i in range(10):
    print(fib(i))















