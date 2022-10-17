# local scope and global scope
# local variable and global variable
'''
The variable that we create inside the functions are called as local variable and we can use the values
of that variable only in inside the functions, this range of using a variable is called as its scope
or local scope.
'''

a = 15  # global var
def fun():
    # local scope of variable a
    a = 10      # local var
    print("In function: ",a)

fun()
# when local variable of same name as global is inside the function, function ignores the global variable

# global scope of variable a
print("Outside the function: ",a)
    
def add():
    a = 12  #local
    addition = a+3
    print(addition)
    print(a)

add()


x = 19  # global x
def sum():
    x = 9   # local x
    print(x)    # ignores global x

sum()           # fun ignore global x
print(x)        # outside fun prints global x


i = 10
def fun():
    # i= i+1    #>> return an error 
    a = i+1
    print("addition is: ", a)
fun()


i = 10      # global i
def fun():
    i = 10  # local i
    i = i+1  # use local i for addition
    print("addition is: ", i)
fun()

a = 0       # global
print(id(a))
def fun():
    global a      # use the global a value inside the fun using global keyword
    print(id(a))
    while a<=5:
        print(a)
        a = a+1     # updated global a value stored in variable and can be use in program in next codes
fun()
print("outside the function: ",a)  # updated global a


def fun1():
    global a
    print(a)   # print latest updated global a value = 6
    a = a + 1
    print(a)   # print latest updated global a value = 7
fun1()



def fun():
    global x1
    x1 = 10       # declare x1 as a global variable using global keyword
    print(x1)    # we can use this global x1 outside the functions also for other operations
fun()
print("Value of x: ",x1)
print(x1 + 9)   # use global x1 that created inside the function for addition




















