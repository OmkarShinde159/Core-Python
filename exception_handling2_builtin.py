# we can define multiple or more than one except blocks for a single try block
# we use multiple except block to handle different types of exceptions
'''
try:
    n = int(input("Enter number: "))
    n1 = int(input("Enter number: "))

    div = n/n1
    print(f"Division of {n} and {n1} is: {div}")
except ValueError:
    print("Entered value should be integer type")
except ZeroDivisionError:
    print("Division is not possible as we dividing number by zero")
'''
'''
l = [1,2,3,5,"p","u"]
try:
    i = 0
    while i <= len(l):
        print(l[i])
        i += 1
except IndexError:
    print("List Index out of range")


l = [1,2,3,5,"p","u"]
new_l = []
try:
    i = 0
    while i < len(l):
        new_l.append(int(l[i]))
        i += 1
except IndexError:
    print("List Index out of range") 
except ValueError:
    print("Cannot able to convert string into integer")

print(new_l)

'''
# can use alias to print the built in error message 
'''
try:
    BODY
except Exception_class_name as object:
    print(object)
'''

l = [1,2,3,5,"p","u"]
try:
    i = 0
    while i<=len(l):
        print(int(l[i]))
        i+=1
except ValueError as i:
    print(i)

a,b = 2,0
try:
    div = a/b
    print(div)
except ZeroDivisionError as d:
    print(d)

# one except block handling specific types of exceptions
# (multiple types of exceptions)
# try:
#     statements
# except (Exception_class1, exception_class2, exception_class3):
#     statements

try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    d = num1/num2
    print(d)
except (NameError, ZeroDivisionError, ValueError) as obj:
    print("Exception occure\n", "Built in msg: ",obj)


# loop with else execution
for i in range(1,10):
    if i==5:
        break
    print(i)
else:
    print("python")

# else block
# this block will get executed  when no exception is raised in the try block
# else block must be present after all except blocks

def div():
    try:
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        d = num1/num2
    except ZeroDivisionError as z:
        print(z)
    except ValueError as v:
        print(v)
    else:
        print("Division is: ", d)


try:
    num = int(input("Enter Number: "))
except ValueError:
    print("Please enter correct number")
else:
    print("Square is: ", num**2)
    

### finally block:
# this block will get executed irrespective of wheather there is an exception
# in the try block or not

try:
    n = int(input("Enter number: "))
    n1 = int(input("Enter number: "))

    div = n/n1
except ZeroDivisionError as z:
    print(z)
else:
    print("Divison is: ", div)
finally:
    print("In the finally block")

'''
# cannot handle erros occures due to not following coding rules
try:
    if True:
    print("Hii")
except IndentationError as s:
    print(s)
'''






