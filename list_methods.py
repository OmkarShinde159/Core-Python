l = [12,23,34,56]

# insrt at the start
l[0:0]=[89,78]
print(l)

# l[0] = [89,78] # added as a nested list
# print(l)

#insert at the end
l[6:]=[1,2,3]
print(l)

# l[6:] = 88  # typeerror can only assign iterable
# print(l)

l[len(l):] = [9,0]
print(l)

# deleting the items
l[0:2] = []
print(l)

l[2:3] = []
print(l)

# del keyword
del l[7]
print(l)

# del l
# print(l) # l is not defined because deleted


# multipledelete
del l[3:5]
print(l)

# reverse
print(l[::-1])

# concatenation
# addition operator +
# int + int normal addition
# str + str
# list + list

print('str'+'str1')
print(9+0)

l2 = ['python','class',90]
con = l+l2
print(con)

con1 = con + l2
print(con1)

# list methods or list functions

# append()
# clear()
# extend()
# copy()
# insert()
# insert(indexing_value, value)
# pop()
# pop(indexing_value)
# remove()
# remove(value)
# sort()
# reverse()

# list_name.function_name()
# list_name.function_name(parameter)

print(l)
l.append(5)
l.append('class')
print(l)

con1.clear()
print(con1)

# l.clear()
print(l)
l.extend((45,65,'python'))
print(l)
l.extend({'add','set'})
print(l)
l.extend(['add','list'])
print(l)

x = l.copy()
print(x)

print(id(l))
print(id(x))
print(x is l)

l.insert(4,90.99)
print(l)

l.pop(5)
print(l)

l.remove('add')
print(l)

l.remove('set')
print(l)

l1 = [45,90,890,76,3]
l1.sort()
print(l1)

l2 = (8,9,0)
print(sorted(l2))

# tuple
# count()
# index()
c = l1.index(890)
print(l1)
print(c)

print(l1.index(76))

# count(value)
print(l1.count(90))
print(l1.remove(90))
print(l1.count(90))

# WAP 
# take each item from user and insert into list

def add_items(n):
    new = []
    for i in range(n):
        st = input("Enter item: ")
        new.append(st)
    print(new)

n = int(input("Enter list size: "))
add_items(n)