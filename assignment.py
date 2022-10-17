# Functions
# Q.1.a)

def factorial(num):
    fact = 1
    for i in range (1,num+1):
         fact = fact*i
    print(fact)
    
# test case
factorial(3)
#factorial(5)
#factorial(6)

# Functions
# Q.1.b)

def factorial2(num):
    while num>0:
        fact = factorial(num)
        num-=1    

factorial2(4)
#factorial2(5)


# Q.2
#Guess by Birthday

def guess_me(birthdate):
    date = 1
    count = 1
    while date <= 31:
        a = int(input("Guess the date from day 1: "))
        if a == birthdate:
            break
        count +=1
        date += 1
    print(count)
    
# test case
guess_me(22)


def guess_me2(birthdate):
    li = [x for x in range(1,32)]
    count = 1
    date = 1
    
    while date <= 31:
        a = int(input("Guess the date: "))
        if a == birthdate:
            break
        elif a > birthdate:
            print("Enter the date less than,",a)
        else:
            print("Enter the date greater than,",a)
            
    count +=1
    date +=1
    print(count+1)
   
# test case
guess_me2(22)













