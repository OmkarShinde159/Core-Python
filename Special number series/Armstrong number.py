# armstrong number

num = int(input("Enter number: "))
count = len(str(num))

'''
count = 0
for i in str(num):
    count += 1
temp = num
cb = 0
'''

while num>0:
    rm = num%10  
    cb = rm**count + cb
    num = num//10   
# print(cb)
if cb==temp:    print(cb, "is armstrong")
else:   print(cb,"is not armstrong")


'''
num = 153
count = 0
for i in str(num):
    count += 1
print(count)
'''
