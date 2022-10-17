# a=(input("Please enter no.: "))
# b=len(a)
# c=int(a[0])**b
# d=int(a[1])**b
# e=int(a[2])**b
# f=c+d+e
# h=int(a)

# if f==h:
#     print("Arm no.")

# else:
#     print("Not arm no.")

# print( float(True))

# x = 2570
# print(id(x))
# y = 2570
# print(id(y))

# print(x is y)

'''
# mutable
# list
x = [1,"harsh",1.5,True, 5,True]
x[4:]=5,6,7
print(x[0:2])
print(x)

# tuple
x = (1,"harsh",1.5,[1,2,3],True,True)
print(x[0:3])
# x[1] = False
print(x)
print(x)
x[3][1:] = 5,6,7
print(x)


x = {11,"harsh",1.5, True}
print(x)
print(id(x))

x.add(5)
print(x)
print(id(x))

x = {1:11,2:"harsh",3:1.5, 4:True}
print(x[2])
print(x)

t = ('python','class','hello')
v = 9,3,2
dt = dict.fromkeys(t,v)
print(dt)

t = ('python')*3
print(t)
print(type(t))
t = ['python']*3
print(t)

# t = {'python'}*3
# print(t)

x = "Harry"
print(x,"he is a good boy")
'''
t = ['python','class','hello']
for x in t:
    print(x)

# for i in range(6,1,-2):
#     print(i)

x = 1
while x < 10:
    if x==5:
        x+=1
        continue   
    x+=1
    print(x)
    
      
   

    
for i in range(0,5):
    for j in range(0,5):
        print("*", end=" ")
    print()














