def FooBar():
    for i in range (1,101):
        if i%3 ==0 and i%5==0 :
            print('FooBar')
        elif i%5 ==0:
            print('Foo')
        elif i%3==0:
            print('Bar')
        else:
            print(i)

#FooBar()

l = [2,1,0,-1,4,5]

def minimun(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min
    
#print(minimun(l))

def maximum(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

#print(maximum(l))

def additin():


def maxfrmNum(num):
    ld = 9
    hd = 0
    while num != 0:
        rem = num%10
        if rem > hd:
            hd = rem
        elif rem < ld:
            ld = rem
        num = num//10

    print("Lowest Num is: ", ld)
    print("Highest Num is: ", hd)

#maxfrmNum(7856)
























    
