# dictionary is container of key-value pair
# it is an unordered collection data type
# key in dictionary must be unique

# creating a dictionary
d = {1:'Python',2:'Omkar',3:'Manisha',4:'Pooja'}

# accessing values in dictionary
print(d[2])
print(d[4])
# print(d[9])   #keyerror

# updating a value in dictionary
print(d)
d[4] = 'pooja saste'
print(d)

# deleting a item
del d[1]
print(d)

roll = d[3]
print(roll)

for i in d:
    print(i)  # prints keys by default

for i,j in d.items():
    print(i,"-",j)

d1 = {'python':'class'}
print(d1['python'])

# methods

# clear()
# dictionary_name.clear()

d2 = {'python':'class', 'color':'pink'}
print(d2)
# d2.clear()
# print(d2)     # {}

# copy()
# dictionary_name.copy()

c = d2.copy()
print(c)

# fromkeys
# return the dictionary with specified key and value
# dict.fromkeys(key,value)
# optional parameter - value

t = ('python','class','hello')
v = 9,3,2
print(type(d))
dt = dict.fromkeys(t,v)
print(dt)

dt1 = dict.fromkeys(t)
print(dt1)  # default value None

dt['python'] = 89 # update a value
print(dt)

# get()
# get(keys,value)
print(dt.get('class',90))
print(dt['class'])

x = dt.get('python')
print(x)
print(dt.get('world',78))
# print(dt['world'])  # keyerror
# print(dt)

# items()
d2 = {'python':'class', 'color':'pink'}
x = d2.items()
print(x)
print(type(x))

for k,v in x:
    print(k,v)

d2['color'] = 'red'
print(d2)
# print(d2.items())
print('x :',x)

for i in d2:
    print(i)

# keys()
# dictionary_name.keys()
# as a list

x = d2.keys()
print(x) # list form

d2['python'] = 'orange'
print(x)
print(d2)

# pop()
# dictionary_name.pop(key, default_value)
# defailt_value - optional

x = d2.pop('python',6)
print(d2)
print(x)

print(d2.pop('class',90))

# popitem()
# dictionary_name.popitem()

d2 = {'python':'class','color':'pink'}
print(d2.popitem())
print(d2)

v = d2.popitem()
print(v)
print(d2)

# setdeault()
# dictionary_name.setdefault(key,value)
# value - optional
# value - bydefault None

d2 = {'python':'class', 'color':'pink'}
b = d2.setdefault('python')
print(b)

b = d2.setdefault('python',89)
print(b)

b1 = d2.setdefault('dfdasa')
print(b1)

b1 = d2.setdefault('week',90)
print(b1)
print(d2)

# update()
# dictionay_name.update(iterator)

d3 = {90:'roll_no','year':2000}
d2.update(d3)
print(d2)

# values
# dictionary_name.values()

val = d2.values()
print(val)

d2['color'] = 'purple'
print(val)