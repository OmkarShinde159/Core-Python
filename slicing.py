l = [10,20,30,40,50,'python','developer']

# accessing a list using indexing, loop and slicing
# python provide negative indexing starts from -1

# using indexing
print(l[0])
print(l[2])
print(l[-5])
print(l[-3])

# using for loop
for i in l:
    print(i, end=" ")
print()


# using while loop
i = 0
while i < len(l):
    print(l[i], end=" ")
    i+=1
print()

# using slicing
# syntax: iterable[start:stop:step]
print(l[:])  # by default print from start to end by step 1
print(l[::])
print(l[2:]) # by default print from assignend start index value till end by step 1
print(l[:3]) # by default print values upto end index from start
print(l[2:5])
print(l[1:6:2])

# reverse order indexing
print(l[::-1])
print(l[3::-1])
print(l[5:2:-2])

# megative indexing
    # sequence from left to right
print(l[-7::1])
print(l[-5:-2:1]) 
print(l[:-1:1])

# updating the value using indexing
l[0] = 65
l[6] = 5
print(l)
l[-1] = 'updated'
l[2:4] = 0.55,0.95,'extra value','ev1','ev2'
print(l)