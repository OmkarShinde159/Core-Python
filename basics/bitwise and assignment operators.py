a = 9
b = 4

a &= b          # bitwise and assignment
print("and:", a)

a |= b          # bitwise or assignment
print("Or: ", a) 

a = -10
print(~a) 

print(~4)
print(~-4)

x = 72 
y = 2
x >>= y
print("right ", x)  # bitwise right assignment

x = -96
right = x>>4
print(right)

x = 12
y = 3
x<<= y
print("left: ",x)  # bitwise left assignment

x = 16
left = x<<3
print(left)

x = 12
y = 3
x ^= y
print("xor : ",x) # bitwise xor assignment


a1 = 10
b1 = -4
# bitwise and
print("a1 & b1", a1 & b1)

# bitwise or  
print("a1 | b1", a1 | b1)

# bitwise not  
print("~a1", ~a1)
print("~b", ~b1)

# bitwise xor  
print("a1 ^ b1", a1 ^ b1)

# right shift
a = 10 
b = -10 
print("a>>1",a>>1)
print("b>>1",b>>1)

# left shift
a = 5 
b = -10 
print("a<<1",a<<1)
print("b<<1",b<<1)


# Assignment opeators

a = 16 
b = 23

# plus Assignment 
a += b
print("plus Assignment: ", a)

# minus Assignment 
a -= b      # a = 39
print("minus Assignment: ",a)

# multiplication Assignment 
a *= b      # a = 16
print("multiplication Assignment: ",a)

# division Assignment 
a /= b      # a = 368
print("division Assignment: ",a)

# remainder Assignment 
b %= a      # a = 16
print("remainder Assignment: ",b)

# floor division Assignment 
b //= a      # a = 16
print("remainder Assignment: ",b)

# power Assignment 
a = 5 
b = 2 
a **= b    
print("power Assignment: ",a)
