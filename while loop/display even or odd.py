# accept positive numbers from 1 to 50
#display even numbers from user entered numbers to 1
#if number is negative or zero or out of range print message
#------------------------------------------------------------------------


# case 1: limit is positive numbers from 1 to 50
# display even numbers from 50 to 0
'''
num = int(input("Enter number case 1: "))

if num > 0 and num <= 50:
    if num % 2 == 0:
        n = num
    else:
        n = num-1
        
    i = 1   
    while n > i:
        print(n)
        n -= 2


#------------------------------------------------------------------------

# case 2: limit is positive numbers from 1 to 50
# display even numbers from 0 to 50

num = int(input("Enter number case 2: "))

if num > 0 and num <= 50:
    i = 2
    while num >= i:
        print(i)
        i += 2
#------------------------------------------------------------------------

# case 3: limit is positive numbers from 1 to 50
# display odd numbers from 50 to 0

num = int(input("Enter number case 3: "))

if num > 0 and num <= 50:
    if num % 2 == 0:
        n1 = num-1
    else:
        n1 = num

    i = 0
    while n1 > i:
        print(n1)
        n1 -= 2
#------------------------------------------------------------------------        

# case 4: limit is positive numbers from 1 to 50
# display odd numbers from 1 to 50

num = int(input("Enter number case 4: "))

if num > 0 and num <= 50:
    i = 1
    while num >= i:
        print(i)
        i += 2
#------------------------------------------------------------------------

# case 5: limit is positive numbers from 1 to 50
# display even and odd numbers from 1 to 50

num = int(input("Enter number case 5: "))

if num > 0 and num <= 50:
    print("Even Numbers are: ")
    i = 2
    while num >= i:
        print(i)
        i += 2

    print("Odd numbers are: ")
    i = 1
    while num >= i:
        print(i)
        i += 2
#------------------------------------------------------------------------

'''
'''

# case 6: limit is positive numbers from 1 to 50
# display even and odd numbers from 50 to 0

num = int(input("Enter number case 6: "))
if num > 0 and num <= 50:
    if num % 2 == 0:
        n = num-1
        
        print("----Even Numbers----")
        i = 2
        while num >= i:
            print(num)
            num -= 2
        print("----Odd Numbers----")
        i = 1
        while n >= i:
            print(n)
            n -= 2
    else:
        n1 = num -1
        print("----Even Numbers----")
        i = 2
        while n1 >= i:
            print(n1)
            n1 -= 2
        print("----Odd Numbers----")
        i = 1
        while num >= i:
            print(num)
            num -= 2
       
elif num < 0:
    print("num is negative")

elif num == 0:
    print("number is zero")

else:
    print("out of range")

#-------------------------------------------------------------------------
# accept negative numbers from -1 to -50
#display even numbers from user entered numbers to -1
#if number is negative or zero or out of range print message

num = int(input("Enter number case 7: "))
if num <= -1 and num >= -50:
    if num % 2 == 0:
        n = num+1
        
        print("----Even Numbers----")
        i = -2
        while num <= i:
            print(num)
            num += 2
        print("----Odd Numbers----")
        i = -1
        while n <= i:
            print(n)
            n += 2
    else:
        n1 = num +1
        print("----Even Numbers----")
        i = -2
        while n1 <= i:
            print(n1)
            n1 += 2
        print("----Odd Numbers----")
        i = -1
        while num <= i:
            print(num)
            num += 2
       
elif num > 0:
    print("num is positive")

elif num == 0:
    print("number is zero")

else:
    print("out of range")
    
'''
'''

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

'''
# WAP to add number from 1 to users enter number


num = int(input("Enter number case 2: "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print("the sum is",sum)
   
    
    



















