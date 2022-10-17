# random module

# random module is a built in module
# which is used to generate random numbers
# these are psuedo random numbers because these are not truly random

import random

# 1. random()
# returns a random float number between 0 and 1
# random.random()
r = random.random()
print(r)
print(random.random())

# 2. randint
# returns a random integer number between specified range
# randint(starting_value, ending_value)
n = random.randint(5,10)
print(n)

for i in range(1,11):
    print(random.randint(100,200))

# print(random.randint(-2,-10,1) 

# 3. randrange()
# returns the random number from the given range
# randrange(start,stop,step)
# stop is mandatory parameter

p = random.randrange(12)
print(p)
print(random.randrange(4,90,8))
print(random.randrange(8,5,-1))

# choice()
# returns a random element from the given sequence
# choice(sequence)
l = [1,5,7,8,9,3,"gsg","fad","fafadsf"]
c = random.choice(l)
print(c)

s = "Python program"
print(random.choice(s))

###
# shuffle()
# recognize or shuffle the order of the items/elements present in the given sequence
# shuffle(sequence, function)
# function is optional
# this function should return the number between 0.0 abd 1.0
# if not specified, the function random() will be used

l = ["A","J","K","Q","2","5","8"]
print(l)

while True:
    print("1.Do you want to start again \n2.exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        random.shuffle(l)
        print(l)
    elif ch==2:
        print("Thank you")
        break
    else:
        print("please enter valid choice")

def random1():
    return 0.8900
random.shuffle(l,random.random)
print(l)




# sample()
# sample(sequence,k)
# where k = number of elements to generate upto length of seq
# returns a list of random elements from sequence
import random as r

data = ['name','age','phone','addr']
l = r.sample(data,k=2)
print(l)

print(r.sample("Python",k=4))

# uniform()
# return a random float number between specified range
# uniform(start_value, end_value)

print(r.uniform(1,5))
print(r.uniform(1.33,5.88))

# triangular()
# triangular(start,stop,mid_point)
# default start,stop,mid = 0,1,0.5
print(r.triangular())
print(r.triangular(12))
print(r.triangular(12,25))
print(r.triangular(12,25,18))