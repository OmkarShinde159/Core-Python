# swap two variables


# without using third variable
a = 10
b = 40
print("Value before swapping, a:",a,",b:",b)
a,b = b,a 
print("Value after swapping, a:",a,",b:",b)

# using third variable
x = 15
y = 30
print("Value before swapping, x:",x,",y:",y)
temp = x
x = y 
y = temp
print("Value after swapping, x:",x,",y:",y)


print("-----using input function-----")

# without using third variable
a = input("Enter the value a:")
b = input("Enter the value b:")
print("Value before swapping, a:",a,",b:",b)
a,b = b,a 
print("Value after swapping, a:",a,",b:",b)

# using third variable
x = input("Enter the value x:")
y = input("Enter the value y:")
print("Value before swapping, x:",x,",y:",y)
temp = x
x = y 
y = temp
print("Value after swapping, x:",x,",y:",y)

