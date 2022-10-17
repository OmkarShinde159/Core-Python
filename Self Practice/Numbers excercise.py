'''
# WAP to reverse an integer in python

def revNum(x):
    rev = 0
    for i in range(len(str(x))): 
        rem = x  % 10   
        rev = rev *10 + rem
        #print(rev)
        x = x//10
    return rev
    
print(revNum(123))
print(revNum(120321))

# using above function check  num is palindrome or not
def isPalindromeNum(x):
    if x == revNum(x):
        return True
    else:
        return False

print(isPalindromeNum(12321))
print(isPalindromeNum(120))


# WAP to check if num is armstrong or not

def isArmstrong(x):
    a = x
    n = 0
    p = len(str(x))
    for i in range(p):
        rem = x % 10
        n = n + rem**p
        x = x//10
    if a == n:
        return True
    else:
        return False
    
print(isArmstrong(150))
print(isArmstrong(355))
print(isArmstrong(153))
print(isArmstrong(370))
print(isArmstrong(371))
print(isArmstrong(12345))

def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                break
            else:
                return True
    else:
        return False

print(isPrime(13))
print(isPrime(1))
print(isPrime(-13))
'''
# WAF to print fibonacci series upto user input number

def fiboSeries(num):
    x = 0
    y = 1
    z = 0
    while z <= num:
        print(x)
        z = x+y
        x = y
        y = z

fiboSeries(5)


def fiboRecr(num):
    

fiboRecr(5)

    





