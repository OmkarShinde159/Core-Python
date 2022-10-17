
# WAF to print fibonacci series 
def fibonacciSeries():
    num = int(input("Enter the num to print fibonacci series: "))
    x = 0
    y = 1
    z = 0
    for i in range(z,num):
        print(z)
        x = y
        y = z
        z = x+y
    
#ibonacciSeries()

        
# WAF to print Primenumber series
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

#primeSeries()


def isPalindrome()
    num = int(input("Enter the number to check: "))
    temp = num
    rn = 0
    while num>0:
        p = num%10
        rn = rn*10+p
        num = num//10
    print(rn)
    if temp == rn:
        print("yes",temp,"is a palindrome number")
    else:
        print("No",temp,"is not a palindrome number")
    
