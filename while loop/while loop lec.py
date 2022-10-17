'''

# decrement------------------------------------------

num = 5
while 0<num:
    print("Hello World Decrement 1")
    num -= 1

num = 5
while 1<=num:
    print(num)
    num -= 1

    
num = 5
while num>0:
    print("Hello World Decrement 2")
    num -= 1

num = 5
while num>=1:
    print(num)
    num -= 1

# increment--------------------------------------------
    
num = 0
while num<5:
    print("Hello World increment 1")
    num += 1

num = 1
while num<=5:
    print(num)
    num += 1
    
num = 0
while 5>num:
    print("Hello World increment 2")
    num += 1

num = 1
while 5>=num:
    print(num)
    num += 1


# count ---------------------------------------------------

count = 1
count_end = 60
while (count <= count_end):
    print("The count is",count)
    count += 1
count -= 1
print("Count completed", count,"times")


count = 1
count_end = int(input("Enter ending count:"))

while (count <= count_end):
    print("The count is",count)
    count += 1
count -= 1
print("Count completed", count,"times")

# multiple inputs ---------------------------------------------

num = 3
while num >0:
    input("Enter Number: ")
    num -= 1


num = 3
while num >0:
    i = input("Enter Number: ")
    num -= 1
print(i)  #the value of i updated in every input



# create a table of 2 to n -------------------------------------------

num = 2
num1 = 1
print("Multiplication table of",num)
while num1 < 11:
    print(num,"*",num1,"=",num*num1)
    num1 += 1



num = int(input("Enter the number to print its multiplication table : "))
num1 = 1
print("Multiplication table of",num)
while num1 < 11:
    print(num,"*",num1,"=",num*num1)
    num1 += 1

'''
'''
# find factorial -------------------------------------------

fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
while num >= 1:# 5 4 3 2 1 false
    fact = fact * num
    num -= 1
print("Factorial is : ",fact)

num1 = int(input("Enter Number to find its factorial: "))
fact = 1
i = 1
while i <= num1:
    fact = fact * i
    i += 1
print("Factorial is: ",fact)


fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
if num <= 0:
    print("cant find factorial, enter number greater than 0")
else:
    while num >= 1:# 5 4 3 2 1 false
        fact = fact * num
        num -= 1
    print("Factorial is : ",fact)



fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
if num > 0:
    while num >= 1:# 5 4 3 2 1 false
        fact = fact * num
        num -= 1
    print("Factorial is : ",fact) 
else:  
    print("cant find factorial, enter number greater than 0")



# create a table of 2 to 100 only , if not print num is out of range-------------------------------------------


num = int(input("Enter the number to print its multiplication table : "))

# method 1
if num >1 and num<=100:
    num1 = 1
    print("Multiplication table of",num)
    while num1 < 11:
        print(num,"*",num1,"=",num*num1)
        num1 += 1

else:
    if num <= 0 or num > 100:
        print("Number is out of range")

# method 2
if num>0:
    if num <101:
        i = 1
        while i <= 10:
            print(num,"*",i,"=",num*i)
            i = i+1
    else:
        print("out of range")

else:
    print("Negative Number")

    
'''
'''
# accept only positive number and give its factorial.and if user enter negative number
# display we cannot find factorial or negative number, and if user enter number
# greater than 100 print out of range, and if user enter 0 display enter numbered is zero
#------------------------------------------

fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
if num > 0 and num <= 100:
    while num >= 1:# 5 4 3 2 1 false
        fact = fact * num
        num -= 1
    print("Factorial is : ",fact) 
elif num < 0:  
    print("cant find factorial, enter number greater than 0")
elif num > 100:
    print("num is out of range")
else:
    print("Number is zero")

'''
'''

# accept number from the user and then display number from 1 to users entered number

num = int(input("Enter num: "))
i = 1
while i <= num: #logic 1
    print(i)
    i += 1


num = int(input("Enter num: "))
i = 1
while num >= i: # logic 2
    print(i)
    i += 1

'''
'''

# if users enter number is positive then accept upto 50
# and then print numbers from 1 to users entered umber
# if user number is beound 50 then print out of range
# if number is negative print number is negative

num = int(input("Enter num: "))

if num > 0 and num <= 50:
    i = 1
    while num >= i: 
        print(i)
        i += 1
elif num > 50:
    print("Out of range")
elif num == 0:
    print("number is zero")
else:
    print("Number is negative")
    


# accept negative from -1 to -50 and
# display users entered number to -1 and
# if number is positive and no is less than -50 then print out of range

num = int(input("Enter num: "))

if num > -50 and num < -1:  
    while num <= -1:
        print(num)
        num += 1

elif num > 0:
    print("num is positive")

elif num == 0:
    print("number is zero")

else:
    print("out of range")



# accept positive numbers from 1 to 50
#display even numbers from user entered numbers in decrement order
#if number is negative or zero or out of range print message

num = int(input("Enter number: "))

if num > 0 and num <= 50:
    if num % 2 == 0:
        n = num
    else:
        n = num-1
        
    i = 1   
    while n > i:
        print(n)
        n -= 2
        
elif num < 0:
    print("num is negative")

elif num == 0:
    print("number is zero")

else:
    print("out of range")
        
    


# case 2: limit is positive numbers from 1 to 50
# display even numbers from 0 to 50

num = int(input("Enter number case 2: "))

if num > 0 and num <= 50:
    i = 1
    while num >= i:
        if i % 2 == 0:
            print(i, "is even number")
            i += 1
        else:
            print(i, "is odd number")
            i += 1


#WAP to add number from 1 to users enter number


num = int(input("Enter number: "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print("the sum is",sum)

'''
'''
# nested while loop pttern
# 6*6
col = 1
while col <= 6:
    row = 1
    while row <= 6:
        print("*",end=" ")
        row += 1
    print()
    col += 1

#4*4
col = 1
while col <= 4:
    row = 1
    while row <= 4:
        print("*", end =" ")
        row += 1
    print()
    col += 1
'''
'''
# user input column
num = int(input("Enter the num: "))
col = 1
while col <= num:
    row = 1
    while row <= num:
        print("*", end = " ")
        row += 1
    print()
    col += 1

# right angle triangle
# user input column
num = int(input("Enter the num: "))
col = 1
while col <= num:
    row = 1
    while row <= col:
        print("*", end = " ")
        row += 1
    print()
    col += 1


# WAP to find the odd numbers from 501 to 551
num = int(input("Enter the num: "))
i = 501
if num >= 501 and num <= 551:
    while i <= num:
        if (num-1) % 2 == 0:
            print(i)
        else:
            print(i)
        i += 2
'''
'''

# WAP to find the odd numbers from 501 to 551       
i = 501
while i <= 551:
    print(i, end=" ")
    i += 2
print()

i = 501
num = 551
while i <= num:
    print(num, end = " ")
    num -=2

# WAP to print the right angle triangle in reverse order
#   1 2 3 4 5 6 << columns
# 1 * * * * * *
# 2 * * * * *
# 3 * * * *
# 4 * * *
# 5 * *
# 6 *

# when row is 1 we need 6 columns here 
# no of columns = no of stars in a row in this pattern

col = 6
while col >= 1:
    row = 1
    while row<= col:
        print("*", end=" ")
        row += 1
    print()
    col -= 1
    
col = int(input("Enter the no of columns: "))
while col>=1:
    row = 1
    while row <= col:
        print("*", end=" ")
        row += 1
    print()
    col -= 1



# wap to find cube of all numbers from 10 to 20
a = 10
b = 20
while a<=b:
    print("cube of",a,"is", a**3)
    a += 1
    
# WAP to find square of all numbers from 20 to 31
a = 20
b = 31
while b>=a:
    print("Square of",a,"is",a*2)
    a += 1
    
'''
'''
#   1 2 3 4 5 6
# 1 * * * * * *
# 2   * * * * *
# 3     * * * *
# 4       * * *
# 5         * *
# 6           *


n = int(input())
row = 1
while row <= n:
    c = 1
    while c < row:
        print(" ",end=" ")
        c += 1

    c1 = 0
    while c1 <= n-row
    n-row:
        print("*", end = " ")
        c1 += 1
        
    print()
    row +=1
'''
'''
#  1 2 3 4 5 6 7 8 9 10 11
#1 *   *   *   *   *   *
#2   *   *   *   *   * 
#3     *   *   *   *
#4       *   *   *
#5         *   *
#6           *

n = 6
row = 1
while row <= n:
    spc = 1
    while spc<row:
        print(" ",end=" ")
        c += 1

    c1 = 0
    while c1 <= n-row:
        print("*  ",end=" ")
        c1 += 1
    print()
    row += 1

#  1 2 3 4 5 6
#1 *
#2 * *
#3 * * *
#4 * * * *
#5 * * * * * 
#6 * * * * * *
#5 * * * * *
#4 * * * *
#3 * * * 
#2 * *
#1 *

n = 6
r = 1
while r <= n:
    n1 = 1
    while n1 <= r:
        print("*", end= " ")
        n1 += 1
    print()
    r+=1
    
c = 6
r1 = 1
while c > 1:
    n2 = 1
    while n2 < c:
        print("*", end=" ")
        n2 += 1
    print()
    c -= 1
   
'''
'''
# number pattern1
print("Number Pattern 1")
i = 1
while i<=5:
    j=1
    while j<=5:
        print(i,end=" ")
        j+=1
    print()
    i+=1
    
# number pattern2
print("Number Pattern 2")
    
i=5
while i>=1:
    j=5
    while j>=1:
        print(j, end=" ")
        j-=1
    print()
    i-=1
    
# number pattern3
print("Number Pattern 3")

i=1
while i<=5:
    j=1
    while j<=i:
        print(j, end=" ")
        j+=1
    print()
    i+=1


# number pattern4
print("Number Pattern 4")
i=1
while i<=5:
    j = 1
    k = 5
    while j<=i:
        print(k,end=" ")
        k-=1
        j+=1
    print()
    i+=1


# number pattern5
print("Number Pattern 5")

i=6
while i>=1:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i-=1


# number pattern6
'''
111111
22222
3333
44
55
6

'''
print("Number Pattern 6")
i=1
while i<=6:
    j=6
    while i<=j:
        print(i,end=" ")
        j-=1
    print()
    i+=1

# number pattern7
print("Number Pattern 7")
i=6
while i>=1:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print()
    i-=1


# number pattern8
print("Number Pattern 8")  

1
2 3
4 5 6
7 8 9 10
'''
'''
i = 1
while i<=10:
    while i<2:
        print(i)
        i+=1
    while i<4:
        print(i,end=" ") 
        i+=1
    print()
    while i<7:
        print(i,end=" ")
        i+=1
    print()
    while i<11:
        print(i,end=" ")
        i+=1
    print()
'''        
'''
i=1
n=4
k=1
while i<=n:
    j=1
    while j<=i:
        print(k,end=" ")
        j+=1
        k+=1
    print()
    i+=1

# number pattern9
print("Number Pattern 9")
'''
'''
'''
i=1
n=6
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1






























