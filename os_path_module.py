# os module
    # submodule - path

# 1. basename()
# use to return basename of a file
# basename(path)

import os

x = os.path.basename('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python')
print(x)

# 2. dirname()
# return the directory name from given path
# os.path.dirname(path)

x = os.path.dirname('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python')
print(x)

# 3. isabs()
# isabs(path)
# chech wheather given path is absolute or not
# if path is absolute - True 
# else False

t = os.path.isabs('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python')
print(t)


# 4. isdir()
# isdir(path)
# check wheather the given path is existing directory or not

w = os.path.isdir('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python1')
print(w)


# isfile()
f = os.path.isfile('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new_rename.py')
print(f)

# normcase()
# normcase(path)
# in Windows returns path is lowercase
# and converts forward slash into backslash
# in unix,linux,MacOS system it returns the pathname as it is

n = os.path.normcase('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python')
print(n)
# c:\users\omkar\desktop\python_programs\python

# normpath(path)
# normalize the path
m = os.path.normpath("C:\\Users/\\Omkar\\Desktop\\Python_Programs\\Python")
print(m)


# exists()
# return boolean value
# check wheather the given file or dir exists in operating systems directory
# exists(path)
v = os.path.exists("C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python")
print(v)
v = os.path.exists("C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python_not")
print(v)
v = os.path.exists("C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new_rename.py")
print(v)


# getsize()
# return the size of the specified file_name in bytes
size = os.path.getsize("module_outer.py")
print(size," Bytes")

# join()
# return the string of pathname with forward slash
# is used to join more paths
# join(path, *path)

p = "C:\\Users\\Omkar"
np = os.path.join(p,"Desktop","Python_programs","Python","new_rename.py")
print(np)

print(os.path.join(os.getcwd(),"Python_new"))

