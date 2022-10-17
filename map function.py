# map function

# map()

# map(func, iterator/sequence)
# msp(func, seq1, seq2)

l = [2,4,6,7,8,9]

# using user defined function in map
def add(n):
    return n+n

map_obj = map(add,l)
print(map_obj)

m = list(map_obj)
print(m)

# using lambda function in map
tup1 = (2,3,4,5,6,7,7)
m_obj = map(lambda n : n+n, tup1)
#similar to
# for i in m_obj:
#       print(i)

t = tuple(m_obj)
print(t)

# map usinf two sequence or iterator with lambda

l1 = [1,5,9]
l2 = [3,5,7]
t1 = (2,5,8)
obj  = map(lambda x,y,z : x+y+z, l1,l2,t1)
print(list(obj))

s1 = {1,4,7}
t2 = (2,5,8)
l3 = [3,6,9]
obj  = map(lambda x,y,z : x+y+z, s1,t2,l3)
print(set(obj))

# with string
# len(data)
str_list = ['python','program','hello','world','mon','l']

# using for loop
print(len(str_list[5]))

for i in str_list:
    print(len(i))

# using map function with user defined
def length(s):
    return len(s)

lg = map(length, str_list)
print("map", list(lg))

# map using with lambda
lg = map(lambda x: len(x), str_list)
print("lambda", list(lg))

# map with bilt in len() function
lg = map(len, str_list)
print('built-in', list(lg))

# WAP to convert str into int
l = ['8','7','6','9','0']

cnv_int = map(int , l)
print(list(cnv_int))












    

















