# immutable objects
# every immuable object has a unique id
# its state or content can not be changed once an object is created

# Example
tuple1 = (0,1,2,3)
print(id(tuple1))
#x = tuple1.remove(2)    # tupe has no attribute remove
# print(tuple1)
# as its a sequence data type we can access its values but cant update
for i in tuple1:
    print(i)
# we can access the value by refering the index number inside the square bracket
print(tuple1[1:3])
# if we want to update the values of tuple it throws an error "type' object does not support item assignment"
# tuple[1] = 4
print(tuple1)

strn = "immutableobject"
print(id(strn))
# can access an objects using for loop
for i in strn:
    print(i)
# can access using indexing method
print(strn[2:9])
x = "abc"
# print(strn.append(x)) 


# Mutable objects
list1 = [0,1,2,3]
print(id(list1))
# list supports item assignment and it is ordered
list1[1] = 4
print(list1)
print(id(list1))    # id remains same but list updated



set1 = {0,1,2,3,4,5,6,7}
print(id(set1))
# set1[1] = 5   set does not support item assignment
print(set1)
print(id(set1))
print(set1)
#print(set1.append(8)) set has no attribute append
x = set1.remove(6)   # set removed object and id remain same
print(set1)
print(id(set1))

dict = {1:"omkar",
        2:"manish",
        3: "rohini"}

dict[4] = "Madhu"
for k,v in dict:
    
print(dict[3])
print(dict)


# list inside the tuple
tup = ([3,4,5], 'myname')
print(tup[0][2])
tup[0][0] = 2
print(tup)
print(tup)




