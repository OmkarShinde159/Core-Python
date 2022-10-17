# calling lambda function inside lambda function

# take a choice from user and perform arithmatic opertions using lambda function

print('1 : addition')
print('2 : subtraction')
print('3 : multiplication')
print('4 : division')
print('5 : percentage')

n = int(input("Enter choice: "))

if n>=1 and n<=4:
        n1 = int(input("Enter num:"))
        n2 = int(input("Enter num:"))
else:
    obt = int(input("Enter obt:"))
    tot= int(input("Enter tot:"))
        

add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b
per = lambda a,b : (obt/tot)*100
        
op = lambda n : add(n1,n2) if n==1 else (sub(n1,n2) if n==2 else (mul(n1,n2) if n==3 else (div(n1,n2) if n==4 else (per(obt,tot) if n==5 else "Invalid input"))))

print(op(n))

# filter()
# syntax: filter (function, sequence data)

def greater(i):
    if i>5:
        return i
list1 = [1,2,3,4,5,6,7,8,9]
fil = filter(greater,list1)
print(fil)
print(type(fil))
# can access using for loop
#for i in fil:
#    print(i)
l = list(fil)
print(l)
fil = filter(lambda x: True if x>5 else False, list1)
print('using lambda:',list(fil))


# filter num divisible by 3
t = (1,2,3,4,5,6,7,8,9)
def fun(n):
    if n%3==0:
        return n
div3 = filter(fun,t)
print(list(div3))

div3 = filter(lambda x: True if x%3==0 else False, t)
print('using lambda: ', list(div3))


# filter even numbers
t1 = (1,2,3,4,5,6,7,8,9)
def fun1(n):
    if n%2==0:
        return n
div4 = filter(fun1,t1)
print(list(div4))

even = filter(lambda x: True if x%2==0 else False, t1)
print('using lambda:', list(even))


# filter all the values in the list which is equal to or greater than 18
list2 = [2,15,13,18,19,25,36,32,0]
def fun2(i):
    if i>=18:
        return i
div5 = filter(fun2, list2)
print(list(div5))

grt = filter(lambda x : True if x>=18 else False, list2)
print('using lambda:', list(grt))


# filter the first class percentage
perc = [61,65,68,79,55,42,35,89]
def fun3(p):
    if p >=60:
        return p
div6 = filter(fun3, perc)
print(list(div6))

per = filter(lambda x: True if x>60 else False, perc)
print("using  lambda", list(per))


# filter the vowels from string list
string = ['a','e','r','y','i','k']
def vov(s):
    if s in "aeiouAEIOU":
        return s
div7 = filter(vov,string)
print(list(div7))


# using lambda function

vov = filter(lambda x: True if x in 'aeiouAEIOU' else False, string)
print('using lambda', list(vov))


# filter all string from length of string of length 5
strings = ['pooja','manisha','omkar','learning','python']
len5 = filter(lambda x: True if len(x)==5 else False, strings)
print('using lambda:', list(len5))


# filter the numbers between range 10-20
nums = [10,11,15,28,36,14,25,13,17,17,17,19,21]
filnums = filter(lambda x : True if x in range(10,21) else False, nums)
print('using lambda:', set(filnums))














