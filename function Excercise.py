'''
# Q.1. Write a program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def findEven(lst):
    for num in lst:
        if num%2 == 0:
            print(num, end="  ")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
findEven(lst)


#Q.2. Write a function to find the Maximum of three numbers
print()
def findMax(n1,n2,n3):
    lst = [n1,n2,n3]
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max
    
num1 = 12
num2 = 22
num3 = 336

print(findMax(num1,num2,num3))

# Q.3. Write a function to multiply all the numbers in a list.

def mulAll(numList):
    num = 1
    for i in numList:
        num = num*i
    return num

numList = [2,3,5,6]
print(mulAll(numList))

# Q.4. Write a function to sum all the numbers in a list.

def mulAll(numList):
    num = 0
    for i in numList:
        num = num+i
    return num

numList = [2,3,5,6]
print(mulAll(numList))

# Q.5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def calFact(num):
    if num >= 1:
        fact = 1
        for n in range (num,0,-1):
            fact = fact*n
        return fact
    else:
        x = "Enter the positive number"
        return x

print(calFact(5))

print(calFact(-1))
'''

# Q.6 sort a list in ascending order without using builtin sort function


def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j],lst[i]
    print(lst)


lst = [1,3,5,6,4,0]
sort_list(lst)













