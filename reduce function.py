# reduce function

# returns only single value
# syntax: reduce(func, sequence)
# defined inside the module called as functools

# 1st way
# import functools
# functools.reduce(func, seq)

# 2nd
# from functools import reduce
# reduce(func, seq)
# reduce(func, seq, initial_value/starting_value)

list2 =[1,2,3,4,5,6]

# addition using for loop
sum=0
for i in list2:
    sum = sum+i
print(sum)

# using reduce and user defined function
def sum_add(n1,n2):
    return n1+n2

import functools
red = functools.reduce(sum_add, list2)
print(red)

from functools import reduce
r = reduce(sum_add, list2)
print(r)

# using lambda with reduce
red1 = reduce(lambda x,z : x*z, list2)
print(red1)
print(type(red1))

# with optional or third parameter
red2 = reduce(lambda x,y : x+y, list2, 9)
print(red2)

# WAP to find min number from list using list
min_num = reduce(lambda x,y : x if x<y else y, list2)
print("using lambda:", min_num)

#without using lambda
min_num = reduce(min, list2)
print(min_num)

# WAP to find max number from list using list
max_num = reduce(lambda x,y : x if x >y else y, list2)
print("using lambda", max_num)

max_num = reduce(max, list2)
print(max_num)











