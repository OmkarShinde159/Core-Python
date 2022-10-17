# find the series of prime numbers frm given range
# number is only divisible by itself and 1

def primeSeries():
    num = int(input("Enter the number for printing prime number series: "))
    for i in range(1,num):
        if i > 1:
            #print(i)
            for j in range(2,i):
                if i % j ==0:
                    break
            else:
                print(i,end=" ")

primeSeries()
