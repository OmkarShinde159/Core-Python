# string method

# join()
# seperator.join(iterator)
# iterator should be string type

l = ['a','b','c','d','e'] # iterator
s = " "                   # seperator
st = s.join(l)
print(st)

t = ('1','2','3')
s = '_'
print(s.join(t))

d = {'1':'Python','2':'java'}
s = ': >'
print(s.join(d))


# replace()
# string_name.replace('old_value','new_value',count)
# count optional

s = 'Python Programming Language'
print(s)
print(s.replace('Python','java'))  # creates new string
print(s)                           # old string
s1 = s.replace('Python','java')    # string stored in variable
print(s1)

s = 'Python Programming Language, I love Python programming'
print(s)
s2 = s.replace('Python','Java')
print(s2)
s3 = s.replace('Python','Java',1)
print(s3)
# o/p - Java Programming Language, I love Python programming



# split()
# returns list
# string.split(seperator,split_no)
# note: split no 1 = 2 parts of split
# both parameters are optional
# seperator by default consider space for split
# opposite to join 

s = 'Python Programming Language'
t = s.split()
print(t)

t2 = s.split(" ",2)
print(t2)

t3 = s.split(" ",1)
print(t3)

s1 = 'Hello*Python*Class'
print(s1.split("*",1))

# splitlines():
#\n
# string.splitlines(keeplinebreak)
# keeplinebreak - optional
# default - False

s1 = 'Python\nProgramming\nLanguage'
l = s1.splitlines()
print(l)
l1 = s1.splitlines(True)
print(l1)

# strip()
# removes the spaces or characters from start and end of the string
# by default removes spaces
# string.strip(character)

# s = input("Enter your choice: ")
s = '   1   '
print(s)
s  = s.strip()
print(s)
if s == '123':
    print("123")

s = "*******123***"
print(s)
print(s.strip("*"))

s = 'abc1234abc'
print(s)
print(s.strip('abc'))


# swapcase()
# convert characters from lower case - uppercase and uppercase - lowercase
# string.swapcase()
# ignores number

p = 'pyThoN'
s = p.swapcase()
print(s)

# zfill()
# zero fill
# add zero in the beginning if the len is greater than string length
# string.zfill(len)

h = 'dog'
z = h.zfill(12)
print(z)


#rfind()
# find return only first match indexing value whereas r find
# returns last matching indexing value of character from string
# rfind("Value",start,stop)
s = 'PythonPythonP'
print(s.rfind('P'))
print(s.rfind('P',2,10))


# rindex()
# rindex("Value",start,stop)
# if value is not in index returns a valuerror
c = s.rindex('P',0,10)
print(c)

# c = s.rindex('z',0,10)
# print(c)

# rstrip():
# removes the characters from right side of 'value'
# string.rstrip(character)
s = '  Python  '
rs = s.rstrip()
print(rs)
s = '-----Python---'
rs = s.rstrip('-')
print(rs)


# lstrip():
# removes the characters from right side of 'value'
# string.rstrip(character)
s = '  Python  '
rs = s.lstrip()
print(rs)
s = '-----Python---'
rs = s.lstrip('-')
print(rs)

# rsplit()
# splits the string from right
s = 'this is python program code'
print(s.rsplit(" ",2))

# ljust()
# string)name.ljust(len,charachter)
# optional : character
# default : space
s = 'Python'
l = s.ljust(30)
print(l)
print(len(l))  # 30
l1 = s.ljust(30,"-")
print(l1)

# rjust()
# string)name.rjust(len,charachter)
# optional : character
# default : space
s = 'Python'
l = s.rjust(30)
print(l)
print(len(l))  # 30
l1 = s.rjust(30,"-")
print(l1)

# partition
# bydefault search from left
# must returns 3 parts of string 
# returns in a tuple form
# 1 part - before the specified value
# 2 part - spcified value
# 3 part - after the specified value

s = 'hello world I love python programming'
p = s.partition('python')
print(p)
# when specified value not in string
p1 = s.partition('Class')
print(p1)

# rpartition
# search from right
# must returns 3 parts of string 
# returns in a tuple form
# 1 part - before the specified value
# 2 part - spcified value
# 3 part - after the specified value

s = 'hello world I love python programming'
p = s.rpartition('python')
print(p)
# when specified value not in string
p1 = s.rpartition('Class')
print(p1)





