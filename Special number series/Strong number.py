'''
fact = 1
num = int(input("Enter number: "))
while num>= 1:
    fact = fact*num
    num-=1
print(fact)
print(s)


num = 5
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)

'''
num = int(input("Enter num: "))     # take input inter from user
temp = num                                    # store it in diff variable to compare in the end 
new = 0                                          # create a variable to store the factorial addition of each digit

while num>0: # 125                      # use condition to iterate 
    nm = num%10  #5, 2,1              # find the remainder to get the last digit from number
    '''
    fact = 1                                     # find factorial using while
    while nm>=1:
        fact = fact*nm
        nm -=1
    '''
    fact = 1                                    # or find factorial using for loop
    for i in range(1,nm+1):
        fact = fact*i
        
    new = new + fact                      # add and update fact value in new variable to store final value
    num= num//10                         # decrese the num value by dividing with 10 so we find next remainder value in next iteration
    
if temp == new:
    print(temp,"is strong number")
else:
    print(temp, "is not strong number")
    
print(new)
print(temp)
    

