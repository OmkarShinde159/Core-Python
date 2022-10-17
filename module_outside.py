# module seatch path
# built in path
# current directory
# PYTHONPATH - shell variable of python
# default path

# steps to set path
# select path location from properties
# sys module

import sys
x = sys.path
print(x)
print(type(sys.path))
x.append("C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python")
print(sys.path)


# importing module from diff directory
import module_outer
print(module_outer.x)
