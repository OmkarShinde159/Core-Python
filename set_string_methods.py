'''
set()
set is an unordered collection of items
every elements must be unique
set us mutable
element of set is immutable
i.e list,dict,set cannot use inside the set

str, int, bool,tup can use in set
'''
'''
# creating set
x = set([1,3,(4,7),3]) 
print(x)

s = {2,3,"python",(1,2),False}
print(s)

# accessing a set
# for loop
for i in s:
    print(i)

print(False in s)

# set methods
# add()
# Set_name.add(value)
print(s)
s.add(True)
print(s)

s.add(3)
print(s)

# clear()
# set_name.clear()
# s.clear()
# print(s)

# copy()
# set_name.copy()

copy_set = s.copy()
print(copy_set)

x = s.pop()
print(x)
print(s)

# remove()
# set_name.remove(value)
# raise an error when value is not in set
s = {1,2,3,4,5,6}
print(s)
print(s.remove(5))
print(s)

# discard()
# set_name.discard(value)
# does not returns an error when values are not in set
s.discard(3)
print(s)

print(s.discard(2))
print(s)

# update()
set1 = {1,2}
set2 = {3,4}
set2.update(set1)
print(set2)
'''
# issubset()
# True or False
# set_name.issubset(set)
x = {'a','v','b','c'}
z = {'a','b','c','d','v','u'}
t = x.issubset(z)
print(t)

x = {'a','v','b','c'}
z = {'a','c','d','v','u'}
t = x.issubset(z)
print(t)

# issuperset()
# set.issuperset(set)
x = {'a','v','b','c'}
z = {'a','c','d','v','u'}
t = x.issuperset(z)
print(t)

x = {'a','c','d','v','u'}
z = {'a','c','d','v','u'}
t = x.issuperset(z)
print(t)

x = {'a','c','d'}
z = {'a','c','d','v','u'}
t = z.issuperset(x)
print(t)

# intersection()
# return set
# same
# set.intersection(set)
# set.intersection(set1,set2,setn)
# returns common elememts between sets
s1 = {'a','b','c','n'}
s2 = {'p','n','c','a'}
set1 = s1.intersection(s2)
print(set1)

s3 = {'f','g','c','a'}
set2 = s1.intersection(s2,s3)
print(set2)

# difference()
# set.difference(set)
# set
set1 = s1.difference(s2)
print(set1)

set2 = s2.difference(s1)
print(set2)


# union()
# set.union(set)
# set.union(set1,set2,...setn)
s2 = {'p','n','c','a'}
s3 = {'f','g','c','a'}

s = s2.union(s3)
print(s)

s4 = {'o',8,9,'a'}
print(s2.union(s3,s4))
print(s4.union(s2,s3))

# intersection_update()
# set.intersection_update(set)
# set.intersection_update(set1,set2,setn)

s = {'a','b','c','p','l'}
s2 = {'g','m','a','p','l'}
print(s)
s.intersection_update(s2)
print(s) 

s3 = {'c','d','e','l','p'}
s.intersection_update(s2,s3)
print(s)

# difference_update()
# set.difference_update(set)
s = {'a','b','c','p','l'}
s2 = {'g','m','a','p','l'}
s3 = {'c','d','e','l','p'}

s.difference_update(s2)
print(s)
s.difference_update(s2,s3)
print(s)

# set method starts with is returns True or False
# symmetric_difference()
# v = set.symmetric_difference(set)
s = {'a','b','c','p','l'}
s2 = {'g','m','a','p','l'}
s6 = s.symmetric_difference(s2)
print(s6)

# set.symmetric_difference_update(set)
x = {'a','b','c'}
y = {'g','m','a'}
x.symmetric_difference_update(y)
print(x)

# isdisjoint()
# True or False
# set.isdisjoint(set)
x = {'a','b','c'}
y = {'g','m','p'}
print(x.isdisjoint(y))

x = {'a','b','c'}
y = {'g','m','a'}
print(x.isdisjoint(y))


# string
# creating a string
# by single quotes
s = 'python'
print(s)

s1 = "programming"
print(s1)

s2 = '''language'''
print(s2)

s3 = """ python language"""
print(s3)

# multiline
s4 = ''' Python
    programming 
            language'''
print(s4)


# accessing a string
s = 'python'
print(s[:])
print(s[1:5])
print(s[5:1:-1])
# reverese string 
print(s[::-1])

# string is immutable does not allow item assigning
# s[-1] = 9
# s[1:7] = 78

del s
# print(s)

# loop
p = 'prograMMing 55world'
for s in p:
    print(s)

print(p*-1)

# string methods

# capitalize()
print(p.capitalize())
print(p.upper())
print(p.title())

# count()
# string_name.count(value,start,stop)
# value - required
# returns count of particular value in string
s = 'PythonPrpgramming'
c = s.count('P')
print(c)

print(s.count('P',0,8))
print(s.count('P',0,5))

# endswith()
# string_name.endswith(value)
# True or False
print(s.endswith('g'))
print(s.endswith('ing'))
print(s.endswith('jnkj'))
print(s.endswith('n',0,6))

# startswith()
# starting_name.startwith(value,start,stop)
st = s.startswith('P')
print(st)
print(s.startswith('n',5,9))

# find()
# return indexing value.
# if not present return -1
# starting_name.find(value,start,stop)
print(s.find('p'))
print(s.find('ing'))
print(s.find('P',4,9))
print(s.find('na'))

# index()
# return indexing value.
# if not present return -1
# starting_name.find(value,start,stop)
print(s.index('p'))
print(s.index('ing'))
print(s.index('P',4,9))
# print(s.index('na'))

# isalnum()
# alphanumeric characters (a-z,A-Z,0-9)
# *&#$@
# string_name.isalnum()

s = 'Python'
print(s.isalnum())
print('Python55'.isalnum())

# isalpha()
# string_name.isalpha()
print('Python55'.isalpha())

# isdigit()
# dyting_name.isdigit()
print('Python55'.isdigit())

# islower()
# string_name.islower()
print('Python55'.islower())

# isupper()
# string_name.isupper()
print('PYTHON55'.isupper())

# isspace()
s = " 1  "
print(s.isspace())
s = "   "
print(s.isspace())

# string literals
# \n and \t
print("1.Add\n2.Mul\n3.Div")
print("1.Add\t2.Mul\t3.Div")
print("\t1.Add/t\t\n\t2.Mul\n\t3.Div")

# center()
# string_name.center(Length,character)
s = 'Python'
print(s.center(11,'-'))

# expandtabs()
# string_name.expandtabs(tab_size)
s = 'Hello\tWorld'
print(s)
print(s.expandtabs(10))

# isascii()
print('AscII'.isascii())

# isidentifier()
# string_name.isidentifier()

print('Identity'.isidentifier())
print('1Identity'.isidentifier())
print('1 Identity'.isidentifier())

# isprintable()
print('Python'.isprintable())
print('Python\tABC'.isprintable())

# istitle()

p = 'Hello python class'
print(p.istitle())

p = 'Hello Python Class'
print(p.istitle())















