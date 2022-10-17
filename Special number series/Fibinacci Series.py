# fibinacci series
'''
n = 0
num1 = 1
num2 = 1
print(num1)     # 1 
while n <50:  # 0 1 2 3 4
    n = num1+num2 
    num2 = num1 
    num1 = n    
    print(n)    #  2 3 

# using for loop
num = int(input("Enter the num: "))
num1 = 0
num2 = 1
for r in range(0,num):
    if r<=1:
        var = r
    else:
        var = num1 + num2
        num2 = num1
        num1 = var
    print(var)


# using for loop
num = int(input("Enter the num to check : "))
n = 0
num1 = 1
num2 = 1
while n < num:
    #print(n)
    n = num1 + num2
    num2 = num1
    num1 = n
#print(n)
if n==num:
    print(num,"present inside the fibo series")
else:
    print(num,"Not in fibo series")
    
'''

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
    
fibonacciSeries()

        
    
    
 
