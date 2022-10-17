
# lambda dunction returning one value
l = lambda x : x+10
print(l(2))

# lambda function returning multiple values
# consider normal function
def fun():
    return 12,3,5.6,'python'
print(fun())        # return values in tuple form

# using lambda function syntax , lambda arguments : (expression values)
# Note : did not need to use return keyword in lambda function
# as lambda returns value by itself

l1 = lambda : (12,3,5.6,'python')
print(l1)   
print(l1())
x = l1()        # store function in a variable
print(x)
# note: if we did not use parenthesis it returns Typeerror:tuple object is not callable

# multiple values using multiple expression in single line
add = lambda a,b : a+b
print(add(12,3))
a = add(12,4)
print(a)
# similarly
sub = lambda a,b : a-b
print(sub(12,3))
s = sub(12,4)
print(s)
# we can perform this two functions in a single lambda function for same arguments
ad_sb = lambda a,b : (a+b,a-b)      # using concept of returning multiple values
a,b = ad_sb(30,10)
print(a)
print(b)
print(ad_sb(30,20))

# WAP to perform all arithmatic operations on two values
a_s = lambda x,y : (x+y, x-y, x*y, x/y, x**y, x%y)

a,b,c,d,e,f = a_s(12,2)
print(a)
print(b)
print(c)
print()
print(e)
print(f)

# conditional statement using lambda function
# lambda arguments : body of if if statement else body of else

# example
x = 5
print( x*x if x>=10 else x*x*x )
# Note: above statement is only valid for if else statement | bot for if statement

# using same with lambda
sq = lambda x : x*x if x>=10 else x*x*x
print(sq(6))

# using print() in expression
sq = lambda x : print(x*x) if x>=10 else print( x*x*x)
print(sq(4)) # Note : also returns  None 
sq(7)

# WAP to check if entered number is even or odd using lambda
n = lambda x : 'Even' if x%2==0 else 'Odd'
print(n(5))
print(n(6))

# WAP to check the greatest among two numbers
grt = lambda x,y :(x,'is greatest') if x>y else (y,'is greatest')
print(grt(5,10))                                             

# WAP to check if the number is positive or negative using lambda
chk = lambda x: ('positive') if x>0 else ('negative')
print(chk(-5))

# WAP to display square if number is off else display cube using lambda
sq = lambda x:(x**2) if x%2!=0 else (x**3)
print(sq(3))
print(sq(2))

# is you dont want to use else part you can write None or False in else body
squ = lambda x: x*x if x>0 else None
print(squ(4))
print(squ(-3))

# WAP to find greatest among three numbers using lambda
grt = lambda x,y,z : ('x is greater' if x>z else 'z is greater') if x>y else ('y is greater' if y>z else 'z is greater')
print(grt(1,2,3))
print(grt(1,3,2))
print(grt(3,2,1))


# WAP to display you are eligible for college if age is >18 and per>65
# else display you are not elegible
# if age<18 display you are not qualified

check = lambda age,per : ('Elegible for college' if per>65 else 'Not elegible') if age>18 else 'Not fit in criteria'
print(check(19,66))
print(check(19,64))
print(check(17,66))








