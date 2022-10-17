'1 D memoization'

# method 0

#  recursive code to find nth term of fibonacci series
# fibonacci series using recursion
def fib(n):
    # base case
    if n<=1:
        return n
    # recursive calls
    return fib(n-1)+fib(n-2)

# Driver code
if __name__=='__main__':
    n = 6
    print(fib(n))

# method 1
term = [0 for i in range(10000)]
# print(term)
# fibonacci series using memoized recursion
def fib1(n):
    if n<= 1:
        return n

# if fib(n) has already been computed
# we do not do further recursive calls
# hence reduce the number of repeated work

    if term[n] != 0:
        return term[n]
    else:
        # store the computed value of fib(n)
        # in an array tern at index n to
        #  so that it does not needs to be precomputed again
        term[n] = fib1(n-1) + fib1(n-2)
        # print(term)
        return term[n]
    

# Driver code
if __name__=='__main__':
    n = 6
    print(fib1(n))

# method 2

fibonacci_cache = {}

def fibonacci(n):
    # if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth tern
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n>1:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the alue and return it
    fibonacci_cache[n] = value
    return value

# for n in range(1,101):
# print(n,":",fibonacci(n))
print(fibonacci(6))

from array import array
from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci(n):

    # check that input is a positive integer
    if type(n) != int:
        raise TypeError("n must be positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # compute the nth tern
    if n==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# longest commom subsequence (lcs)
# naive approach
def lcs (X,Y,m,n):
    if (m == 0 or n == 0):
        return 0
    if (X[m-1] == Y[n-1]):
        return 1 + lcs(X,Y,m-1,n-1)
    else:
        return max(lcs(X,Y,m,n-1),lcs(X,Y,m-1,n))

# driver code
if __name__=='__main__':
    X = 'AGGTAB'
    Y = 'GXTXAYB'
    m = len(X)
    n = len(Y)
    print(f'length of LCS is: {lcs(X,Y,m,n)}')


# memoization applied in recursive solution
def lcS(X,Y,m,n):
    global arr

    # base case
    if (m==0 or n==0):
        return 0

    # if the same state has already been computed
    if (arr[m-1][n-1] != -1):
        return arr[m-1][n-1]

    # if equal then we store the value of the function call
    if (X[m-1] == Y[n-1]):

        # store it in arr to avoid durther repetitive work 
        arr[m-1][n-1] = 1+lcS(X,Y,m-1,n-1)
        return arr[m-1][n-1]

    else:
        arr[m-1][n-1] = max(lcS(X,Y,m,n-1),lcS(X,Y,m-1,n))
        return arr[m-1][n-1]

# driver code
arr = [[0]*1000]*1000

for i in range(0,1000):
    for j in range(0,1000):
        arr[i][j] = -1

X = 'AGGTAB'
Y = 'GXTXAYB'
m = len(X)
n = len(Y)

print("length of LCS is:- ", lcS(X,Y,m,n))

# 3d memoization

# def LCS(X,Y,Z,m,n,o):
#     # base case
#     if m==0 or n==0 or o==0:
#         return 0

#         # if equal, then check next combination
#         if X[m-1]== Y[n-1] and Y[n-1] == Z[o-1]:

