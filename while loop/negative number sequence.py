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

'''

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
        
    
    







