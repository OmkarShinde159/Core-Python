
# Formal arguments - parameter
# Actual arguments - argument

'''
Types of Arguments:
1. Positional argument or required positional argument
2. Keyword argument
3. default argument
4. variable length argument
5. keyword variable length argument
'''
# 1. Positional argument
'''
# Example
def fun_1(a):
    print(a)
# fun_1()         > error because no argument
fun_1(6)
# fun(6,2)    > error because extra argument

# Example
def add(a,b):
    a1 =a+b
    print(a1)
# add(56)
add(23,3)
add(3,23)

# Example
e = int(input("Enter num: "))
ex = int(input("Enter num: "))
def exp(e,ex):
    print(e**ex)        
exp(2,5)
exp (ex, e)         # no error but wrong output because of wrong positions of values
exp(e,ex)
exp(3,5)

# Example
def per(o,t):
    p = o/t*100
    print("Perentage is: ",p)

per(450,500)
per(500,450)    # no error but wrong output because of wrong positions of values
'''
# 2. Keyword argument
# name and value pair
# name=value

'''
#Example
def fun(name,age):
    print(name)
    print(age)
fun('python',5)    # returns correct output beause of correct data sequence as per parameter
fun(6,'python')   # retrurns incorrect output because of incorrect sequence order of data
# to avoid this errors because of "sequence of arguments != seq of parameters"
# keyword argument is used

#Example
def fun(name, age):
    print(name)
    print(age - 8)
fun('python',5)
fun(age = 16, name = 'python')
#fun(age = 16)
#fun(age = 16, name = 'python', r = 90)

# keyword argument name must match the formal argument name

#Example
def fun1(name,age,roll_no):
    print("Name: ", name)
    print("Age: ", age)
    print("Roll_No: ", roll_no)
fun1("python",25,7)
fun1(roll_no=10, age=20,name='sachin')
fun1(age=18,name="manisha",roll_no=6)
fun1("Omkar", roll_no=9, age=25)

# Example

def per(o,t):
    p = o/t*100
    return p
print(per(350,500))
print(per(500,350))  # incorrect percentage
print(per(t=500,o=350))


# Example
def num(n1,n2):
    return n1-n2
print(num(7,9))
print(num(n2=7,n1=9))

# Example
e1 = int(input("Enter num for power: "))
p1 = int(input("Enter the power value: "))
def exp(e,p):
    return e**p

print(exp(p=p1,e=e1))
print(exp(p1,e1))    # incorrect output
#print(exp(3))         # error


# 3.default argument

def fun3(name = 'user', age=18):
    print(name)
    print(age)
fun3()
fun3("Pooja")
fun3("Pooja",19)
fun3(21)
fun3(age = 21)

def add(num1 = 0,num2=0):
    print("addition is: ", num1+num2)
add()
add(1,2)
add(20)

#def add(num1 = 0, num2)     default argument shold ne followd by non default argument
#   print(num1 + num2)
#add(2,3)
#add(3)


def add(num2, num1 = 0):
    print(num1 + num2)
add(2,3)
#add(3)




# 4. variable length argument
# stores in form of tuple
# *formal_argument_name


def add(*num):
    total = 0
    for i in num:
       total =  total + i
    print(total)

add(1,2,3,4,5,6)
add( 15,15,25,25,50)


def p_print(*s):
    print(s[0],s[1],s[2])
    print(s)
p_print("Hello","welcome","to","goa")

def fun4(*n):
    for i in n:
        print("Hello", i)

fun4("Omkar","Pooja","Manisha")



def obt_marks(*marks):
    obt_marks = 0
    for m in marks:
        obt_marks = obt_marks + m
    return obt_marks

obt_marks(56,89,78,67,56)

def perc(*marks):
    obt = obt_marks(*marks)
    #print(obt)
    tot = len(marks)*100
    #print(tot)  
    per = obt/tot*100
    print(per)
 
perc(66,89,78,67,56,89,78,90)

'''
'''
# fun(age = 90, name = 'Python')
# name,age,roll_no,per,class

def fun1(**kwargs):
    print(kwargs)
    print("Name is: ",kwargs['name'])
    print('Roll no is: ', kwargs['roll_no'])

fun1(name='python',roll_no = 19)
fun1(name='python',roll_no = 19, age = 20, per=90)

def add1(**b):
    sum = 0
    for k in b.values():
        sum = sum + k
    print(sum)

add1(n= 1,n1=9,n2=5)

def fun3 (**kwargs):
    for i in kwargs.items():
        print(i)

fun3(name='python',roll_no=19)
fun3(name='python',roll_no=19, age=20,per=90)

def fun4(**k):
    for k1 in k:
        print("Hello",k1)

    for k2 in k.values():
        print("Percentage is: ",k2)
              
    for k3,k4 in k.items():
              print('Name is: ',k3, ', perentage is: ',k4)

fun4(Omkar=99, pooja=89,manisha=78)


def fun5(**marks):
    for a,b in marks.items():
        print("Marks of ",a, "is" ,b)
        
    obt = 0
    for m in marks.values():
        obt = obt + m
    print(obt)
        
    count = 0
    for s in marks:
        count += 1
    print(count)

    tot = count*100
    print(tot)

    per = obt/tot*100
    print("Percentage is : ", per)
        
fun5(maths=78, marathi=85,English=88,science=93, history=64)

'''
# recursive function
'''
def rec():
    x = 10
    print(x)
    rec()

rec()    # returns recursion error as it crosses 1000 limit
print("Hello world")  
'''

def num(n):
    print(n)
    if n==0:
        return
    else:
        num(n-1)

#num(6)

def factrec(n):    
    if n==1:
        return 1
    else:
        return n*factrec(n-1)
    
print(factrec(1))
print(factrec(2))
print(factrec(3))
print(factrec(4))
print(factrec(5))









